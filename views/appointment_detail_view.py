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
        decide how the appointment detail view is
        '''

        # background frame
        outer_frame = tk.LabelFrame(self, relief="solid", borderwidth=2, bg="white")
        inner_frame = tk.LabelFrame(outer_frame, relief="flat", bg="white")

        # title
        tk.Label(outer_frame, text="Appointment Detail", font=('Roboto', 28, "bold"), bg="white").pack(pady=(50, 30))

        # patient status
        statue_frame = tk.Frame(outer_frame, width=200, bg="white")
        statue_frame.pack(pady=10)
        tk.Label(statue_frame, text='Please choose your status').pack(side='top')
        var = tk.StringVar()
        var.set('None')
        tk.Radiobutton(statue_frame, text='New patient', variable=var, value='True').pack(side='left')
        tk.Radiobutton(statue_frame, text='Existing patient', variable=var, value='False').pack(side='right')

        # appointment reason
        reason_frame = tk.Frame(outer_frame, width=200, bg="white")
        reason_frame.pack(pady=10)
        tk.Label(reason_frame, text='Please choose your reason for appointment').pack()
        rea = tk.StringVar()
        rea.set('Select one reason for seeing GP')
        reason_box = ttk.Combobox(reason_frame, textvariable=rea, width=30)
        reason_box['value'] = reasons
        reason_box.bind('<<ComboboxSelected>>', self.callback)
        reason_box.pack()

        # for user to select date and time for appointment
        dt_frame = tk.Frame(outer_frame, width=200, bg="white")
        dt_frame.pack(pady=10)
        app_date = DateEntry(dt_frame, date_pattern='mm/dd/yy', selectmode='day', showweeknumbers=False)
        app_date.pack(side='left')

        tm = tk.StringVar()
        tm.set('Time')
        self.time_list = ttk.Combobox(dt_frame, textvariable=tm, state='disabled', width=15)
        self.time_list.pack(side='right')

        # for patient to select a GP
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

        # pack the background frame
        outer_frame.pack(padx=100, pady=120, fill="x", ipady=30, ipadx=30)
        inner_frame.pack(padx=50, fill="x")

    def reload_values(self):
        pass

    def callback(self, e):
        '''
        if the reason box is selected or changed, change the mode of time
        '''

        # check the value of the reason box and do actions
        if e.widget.get() == 'Select one reason for seeing GP':
            self.time_list['state'] = tk.DISABLED
        else:
            self.time_list['state'] = tk.NORMAL

            times = self.controller.get_time(e.widget.get())
            self.time_list['value'] = times
            self.time_show = True

    def next(self, master, gp, reason, patient_status, date, time):
        '''
        check if every detail is well completed
        '''

        # check the status of gp box
        if gp == 'None' or gp == 'please choose a GP(optional)':
            gp = self.controller.find_gp_with_least_appointment()

        # check the status of the reason box
        if reason == 'Select one reason for seeing GP':
            tk.messagebox.showerror(title='Reason for appointment Error', message='please select one reason for seeing GP')
            return

        # check the status of the patient status
        if patient_status == 'None':
            tk.messagebox.showerror(title='Patient status Error', message='please select one patient status')
            return

        # check if the format of date is correct
        try:
            date_check = datetime.datetime.strptime(date, '%d/%m/%Y')
        except ValueError:
            self.display_input_error("Incorrect date format input \n(Use dd/mm/YYYY)")
            return

        # check if the date if in the future
        if datetime.datetime.strptime(date, '%d/%m/%Y').date() < datetime.date.today():
            tk.messagebox.showerror(title='Date Error', message='please choose a date after today')
            return

        # check if the time is completed
        if time == 'Time':
            tk.messagebox.showerror(title='Time Error', message='please choose a time')
            return

        # if everything is good, show the question view
        self.controller.display_questionnaire_view(master, gp, reason, patient_status, date, time)

    def display_input_error(self, err_str):
        '''
        display the error message for wrong date format
        '''
        tk.messagebox.showerror(title='date error', message=err_str)