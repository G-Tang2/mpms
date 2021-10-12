import tkinter as tk
from tkinter import ttk
from tkcalendar import *
import datetime


class AppointmentDetailView(tk.Frame):
    def __init__(self, master: tk.Tk, controller) -> None:
        # initialise frame and set controller
        tk.Frame.__init__(self, master, bg="#c1e4f7")
        self.time_list = ''
        self.controller = controller
        self.time_show = False

    def render_view(self, master: tk.Tk, list_of_gps, reasons) -> None:
        '''
        decide how the appointment detail view is displayed
        '''

        # background frame
        outer_frame = tk.LabelFrame(self, relief="solid", borderwidth=2, bg="white")
        inner_frame = tk.LabelFrame(outer_frame, relief="flat", bg="white")

        # page title
        tk.Label(outer_frame, text="Appointment Detail", font=('Roboto', 28, "bold"), bg="white").pack(pady=(50, 30))

        # patient status
        statue_frame = tk.Frame(outer_frame, width=200, bg="white")
        statue_frame.pack(pady=10)
        tk.Label(statue_frame, text='Please choose your status', font=('Roboto', 15), bg="white").pack(side='top')
        var = tk.StringVar()
        var.set('None')
        tk.Radiobutton(statue_frame, text='New patient', variable=var, value='True', bg="white").pack(side='left')
        tk.Radiobutton(statue_frame, text='Existing patient', variable=var, value='False', bg="white").pack(side='right')

        # appointment reason
        reason_frame = tk.Frame(outer_frame, width=200, bg="white")
        reason_frame.pack(pady=10)
        tk.Label(reason_frame, text='Please choose your reason for appointment', font=('Roboto', 15), bg="white").pack()
        rea = tk.StringVar()
        rea.set('Select one reason for seeing GP')
        reason_box = ttk.Combobox(reason_frame, textvariable=rea, width=30)
        reason_box['value'] = reasons
        reason_box.bind('<<ComboboxSelected>>', self.callback)
        reason_box.pack()

        # date and time
        dt_frame = tk.Frame(outer_frame, width=200, bg="white")
        dt_frame.pack(pady=10)
        app_date = DateEntry(dt_frame, date_pattern='mm/dd/y', selectmode='day', showweeknumbers=False)
        app_date.pack(side='left')

        tm = tk.StringVar()
        tm.set('Time')
        self.time_list = ttk.Combobox(dt_frame, textvariable=tm, state='disabled', width=15)
        self.time_list.pack(side='right')

        # GP
        gp_frame = tk.Frame(outer_frame, width=200, bg="white")
        gp_frame.pack(pady=10)
        gp = tk.StringVar()
        gp.set('please choose a GP(optional)')
        gp_box = ttk.Combobox(gp_frame, textvariable=gp, width=30)
        gps = ['None']
        for each_gp in list_of_gps.get_gps():
            gps.append(each_gp.get_full_name())
        gp_box['value'] = gps
        gp_box.pack()

        # button to the next page
        tk.Button(inner_frame, text='Next', 
            command=lambda: self.next(master, gp.get(), rea.get(), var.get(), app_date.get(), tm.get())).pack(side = 'right')
        tk.Button(inner_frame, text='Back', command=self.controller.back).pack(side = 'left', pady=20)

        # pack the buttons
        outer_frame.pack(pady=50, fill="x", ipady=30, ipadx=30)
        inner_frame.pack(padx=150, fill="x")

    def reload_values(self):
        pass

    def callback(self, e):
        '''
        define what will happen when patient change the reason
        '''
        if e.widget.get() == 'Select one reason for seeing GP':
            self.time_list['state'] = tk.DISABLED
        else:
            self.time_list['state'] = tk.NORMAL

            # display the time list based on the reason
            times = self.controller.get_time(e.widget.get())
            self.time_list['value'] = times
            self.time_show = True

    def next(self, master, gp, reason, patient_status, date, time):
        '''
        check if the details is well completed
        :return:
        '''

        # check the gp box status
        if gp == 'None' or gp == 'please choose a GP(optional)':
            gp = self.controller.find_gp_with_least_appointment()

        # check the reason box status
        if reason == 'Select one reason for seeing GP':
            tk.messagebox.showerror(title='Reason for appointment Error', message='please select one reason for seeing GP')
            return

        # check the patient status
        if patient_status == 'None':
            tk.messagebox.showerror(title='Patient status Error', message='please select one patient status')
            return

        # check the date format
        try:
            date_check = datetime.datetime.strptime(date, '%d/%m/%Y')
        except ValueError:
            self.display_input_error("Incorrect date format input \n(Use dd/mm/YYYY)")
            return

        # check if the date is in the past
        if datetime.datetime.strptime(date, '%d/%m/%Y').date() < datetime.date.today():
            tk.messagebox.showerror(title='Date Error', message='please choose a date after today')
            return

        # check the time box status
        if time == 'Time':
            tk.messagebox.showerror(title='Time Error', message='please choose a time')
            return

        # display the next view
        self.controller.display_questionnaire_view(master, gp, reason, patient_status, date, time)

    def display_input_error(self, err_str):
        '''
        display the error message for the wrong date format
        '''
        tk.messagebox.showerror(title='date error', message=err_str)