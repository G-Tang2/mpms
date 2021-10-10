import tkinter as tk
from tkinter import ttk
from tkcalendar import *


class AppointmentDetailView(tk.Frame):
    def __init__(self, master: tk.Tk, controller) -> None:
        # initialise frame and set controller
        tk.Frame.__init__(self, master, bg="#c1e4f7")
        self.time_list = ''
        self.controller = controller
        self.time_show = False

    def render_view(self, master: tk.Tk, list_of_gps) -> None:

        outer_frame = tk.Frame(self, relief="solid", borderwidth=2, bg="white")
        inner_frame = tk.Frame(outer_frame, relief="flat", bg="white")
        outer_frame.pack(padx=350, pady=120, fill="x", ipady=30, ipadx=30)
        inner_frame.pack(padx=150, fill="x")

        tk.Button(inner_frame, text='back', command=self.controller.back).pack(pady=30)

        # new:  patient status
        statue_frame = tk.Frame(outer_frame, width=200)
        statue_frame.pack(pady=10)
        tk.Label(statue_frame, text='Please choose your status').pack(side='top')
        var = tk.StringVar()
        var.set('None')
        tk.Radiobutton(statue_frame, text='New patient', variable=var, value='True').pack(side='left')
        tk.Radiobutton(statue_frame, text='Existing patient', variable=var, value='False').pack(side='right')

        # new: appointment reason
        reason_frame = tk.Frame(outer_frame, width=200)
        reason_frame.pack(pady=10)
        tk.Label(reason_frame, text='Please choose your reason for appointment').pack()
        rea = tk.StringVar()
        rea.set('Select one reason for seeing GP')
        reason_box = ttk.Combobox(reason_frame, textvariable=rea, width=30)
        reasons = self.controller.get_reason_list()
        reason_box['value'] = reasons
        reason_box.bind('<<ComboboxSelected>>', self.callback)
        reason_box.pack()

        # for user to select date and time for appointment
        dt_frame = tk.Frame(outer_frame, width=200)
        dt_frame.pack(pady=10)
        app_date = DateEntry(dt_frame, date_pattern='mm/dd/y', selectmode='day', showweeknumbers=False)
        app_date.pack(side='left')

        tm = tk.StringVar()
        self.time_list = ttk.Combobox(dt_frame, textvariable=tm, state='disabled', width=15)
        self.time_list.pack(side='right')

        # for patient to select a GP
        gp_frame = tk.Frame(outer_frame, width=200)
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
        tk.Button(outer_frame, text='next', command=
        lambda: self.next(master, gp.get(), rea.get(), var.get(), app_date.get_date(), tm.get())).pack()
        # self.__show_date()

    def callback(self, e):
        if e.widget.get() == 'Select one reason for seeing GP':
            self.time_list['state'] = tk.DISABLED
        else:
            self.time_list['state'] = tk.NORMAL

            times = self.controller.get_time(e.widget.get())
            self.time_list['value'] = times
            self.time_show = True

    def next(self, master, gp, reason, patient_status, date, time):
        if gp == 'None':
            gp = self.controller.find_gp_with_least_appointment()

        if reason == 'Select one reason for seeing GP':
            tk.messagebox.showerror(title='reason for appointment', message='please select one reason for seeing GP')
            return

        if patient_status == 'None':
            tk.messagebox.showerror(title='Patient Status', message='please select one patient status')
            return

        tk.Button(self, text='complete',
                  command=lambda: self.make_appointment(gp, reason, patient_status))

        self.controller.display_questionnaire_view(master, gp, reason, patient_status, date, time)
