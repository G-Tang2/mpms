import tkinter as tk
from tkinter import Event, ttk
from typing import List
from tkcalendar import *
import datetime
from models.gp_list import GPList


class AppointmentDetailView(tk.Frame):
    def __init__(self, master: tk.Tk, controller) -> None:
        # initialise frame and set controller
        tk.Frame.__init__(self, master, bg="#c1e4f7")
        self.time_list = None
        self.controller = controller
        self.time_show = False

    def render_view(self, master: tk.Tk, list_of_gps: GPList, reasons: List[str]) -> None:
        '''
        decide how the appointment detail view is displayed
        '''

        # background frame
        outer_frame = tk.LabelFrame(self, relief="solid", borderwidth=2, bg="white")
        inner_frame = tk.LabelFrame(outer_frame, relief="flat", bg="white")

        # page title
        tk.Label(outer_frame, text="Appointment Details", font=('Roboto', 28, "bold"), bg="white").pack(pady=(50, 30))

        # patient status
        statue_frame = tk.Frame(outer_frame, width=200, bg="white")
        statue_frame.pack(pady=15)
        tk.Label(statue_frame, text='Please choose your status:', font=('Roboto',12), anchor="w", bg="white").pack(side='top', padx=30, fill='x')
        var = tk.StringVar(value="None")
        tk.Radiobutton(statue_frame, text='New patient', variable=var, value='True', bg="white").pack(side='left', padx=30, fill='x')
        tk.Radiobutton(statue_frame, text='Existing patient', variable=var, value='False', bg="white").pack(side='right',padx=30, fill='x')

        # appointment reason
        reason_frame = tk.Frame(outer_frame, width=200, bg="white")
        reason_frame.pack(pady=15)
        tk.Label(reason_frame, text='Please choose the reason for appointment:', font=('Roboto', 12), anchor="w", bg="white").pack(side='top', padx=30, fill='x')
        rea = tk.StringVar()
        reason_box = ttk.Combobox(reason_frame, textvariable=rea, width=30)
        reason_box['value'] = reasons
        reason_box.bind('<<ComboboxSelected>>', self.callback)
        reason_box.pack(padx=30, fill='x')

        # date and time
        dt_frame = tk.Frame(outer_frame, width=200, bg="white")
        dt_frame.pack(pady=15)
        tk.Label(dt_frame, text='Please choose the date and time:', font=('Roboto', 12), anchor="w",
                 bg="white").pack(side='top', fill='x')
        app_date = DateEntry(dt_frame, date_pattern='dd/mm/y', selectmode='day', showweeknumbers=False, width=14)
        app_date.pack(side='left', fill='x')

        tm = tk.StringVar()
        self.time_list = ttk.Combobox(dt_frame, textvariable=tm, state='disabled', width=14)
        self.time_list.pack(side='right')

        # GP
        gp_frame = tk.Frame(outer_frame, width=200, bg="white")
        gp_frame.pack(pady=15)
        tk.Label(gp_frame, text='GP preference (Optional):', font=('Roboto', 12), anchor="w",
                 bg="white").pack(side='top', padx=30, fill='x')
        gp = tk.StringVar(value='None')
        gp_box = ttk.Combobox(gp_frame, textvariable=gp, width=30)
        gps = ['None']
        for each_gp in list_of_gps.get_gps():
            gps.append(each_gp.get_full_name())
        gp_box['value'] = gps
        gp_box.pack(padx=30, fill='x')

        # button to the next page
        tk.Button(inner_frame, text='Next', borderwidth=2, relief="solid", bg="#99d2f2", activebackground="#81c8f0",
            command=lambda: self.next(master, gp.get(), rea.get(), var.get(), app_date.get(), tm.get())).pack(side = 'right', ipadx=10)
        tk.Button(inner_frame, text='Back', borderwidth=2, relief="solid", bg="#99d2f2", activebackground="#81c8f0",
            command=self.controller.back).pack(side = 'left',ipadx=10, pady=20)

        # pack the buttons
        outer_frame.pack(pady=50, fill="x", ipady=30, ipadx=30)
        inner_frame.pack(padx=200, fill="x")

    def reload_values(self):
        pass

    def callback(self, e: Event) -> None:
        '''
        define what will happen when patient change the reason
        '''
        if e.widget.get() == '':
            self.time_list['state'] = tk.DISABLED
        else:
            self.time_list['state'] = tk.NORMAL

            # display the time list based on the reason
            self.controller.get_time(e.widget.get())

    def set_time_list(self, times: List[str]) -> None:
        self.time_list['value'] = times

    def next(self, master, gp: str, reason: str, patient_status: str, date: str, time: str) -> None:
        '''
        check if the details is well completed
        :return:
        '''

        # check the gp box status
        if gp == 'None':
            gp = self.controller.find_gp_with_least_appointment()

        # check the patient status
        if patient_status == 'None':
            tk.messagebox.showerror(title='Patient Status Incomplete', message='Please select one patient status.')
            return

        # check the reason box status
        if reason == '':
            tk.messagebox.showerror(title='Reason For Appointment Incompleted',
                                    message='Please select one reason for appointment.')
            return

        # check the date format
        try:
            date_datetime = datetime.datetime.strptime(date, '%d/%m/%Y')
        except ValueError:
            self.display_input_error("Incorrect date format input \n(Use DD/MM/YYYY)\nE.g. 01/03/2021 for 2021 March 1st")
            return

        # check if the date is in the past
        if date_datetime.date() <= datetime.date.today():
            tk.messagebox.showerror(title='Date Error', message='Please choose a date after today.')
            return

        # check the time box status
        if time == '':
            tk.messagebox.showerror(title='Time Incompleted', message='Please choose a time.')
            return

        # save user input
        self.controller.save_values(gp, reason, patient_status, date_datetime, time)

        # display the next view
        self.controller.display_questionnaire_view()

    def display_input_error(self, err_str: str) -> None:
        '''
        display the error message for the wrong date format
        '''
        tk.messagebox.showerror(title='Date Format Error', message=err_str)