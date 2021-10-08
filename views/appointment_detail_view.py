import tkinter as tk
from tkinter import ttk
from tkcalendar import *


class AppointmentDetailView(tk.Frame):
    def __init__(self, master: tk.Tk, controller) -> None:
        # initialise frame and set controller
        tk.Frame.__init__(self, master)
        self.time_list = ''
        self.controller = controller
        self.time_show = False

    def render_view(self, master: tk.Tk, list_of_gps) -> None:

        tk.Button(self, text='back', command=self.controller.back).pack()
        # select GP
        tk.Label(self, text='Please select a GP (optional)').pack()
        listbox = tk.Listbox(self)
        for gp in list_of_gps.get_gps():
            listbox.insert('end', gp.get_full_name())
        listbox.pack()
        tk.Button(self, text='select_clear', command=lambda: self.selection_clear(listbox)).pack()

        # new:  patient status
        tk.Label(self, text='Please choose your status').pack()
        var = tk.StringVar()
        var.set('None')
        tk.Radiobutton(self, text='New patient', variable=var, value='True').pack()
        tk.Radiobutton(self, text='Existing patient', variable=var, value='False').pack()

        # new: appointment reason
        tk.Label(self, text='Please choose your reason for appointment').pack()
        rea = tk.StringVar()
        rea.set('Select one reason for seeing GP')
        reason_box = ttk.Combobox(self, textvariable=rea, width=30)
        reasons = self.controller.get_reason_list()
        reason_box['value'] = reasons
        reason_box.bind('<<ComboboxSelected>>', self.callback)
        reason_box.pack()

        app_date = DateEntry(self, date_pattern='mm/dd/y', selectmode='day', showweeknumbers=False)
        app_date.pack()

        tm = tk.StringVar()
        self.time_list = ttk.Combobox(self, textvariable=tm, state='disabled')
        self.time_list.pack()

        tk.Button(self, text='next', command=lambda: self.next(listbox, rea.get(), var.get())).pack()

        # self.__show_date()

    def callback(self, e):
        if e.widget.get() == 'Select one reason for seeing GP':
            self.time_list['state'] = tk.DISABLED
        else:
            self.time_list['state'] = tk.NORMAL

            times = self.controller.get_time(e.widget.get())
            self.time_list['value'] = times
            self.time_show = True

    def selection_clear(self, listbox):
        listbox.selection_clear(0, 'end')

    def next(self, listbox, reason, patient_status):
        if listbox.curselection():
            gp = listbox.get('active')
        else:
            gp = self.controller.find_gp_with_least_appointment()

        if reason == 'Reason for seeing GP':
            tk.messagebox.showerror(title='reason for appointment', message='please select one reason for seeing GP')
            return

        if patient_status == 'None':
            tk.messagebox.showerror(title='Patient Status', message='please select one patient status')
            return

        tk.Button(self, text='complete',
                  command=lambda: self.make_appointment(gp, reason, patient_status))

        self.make_appointment(gp, reason, patient_status)



    def make_appointment(self, gp, reason, patient_status):
        branch = self.controller.get_branch()

        confirm = tk.messagebox.askokcancel(title='Confirming',
                                            message='You are going to have an appointment at'
                                                    + branch + '\nGP: ' + gp + '\nReason: ' + reason
                                                    + '\nNew patient: ' + patient_status)

        if confirm:
            self.controller.write_appointment()
            tk.messagebox.showinfo(title='Successfully',
                                      message='You have made an appointment \nPlease attend on time')

    def __show_date(self):
        # dt = tk.StringVar()
        # dt.set('None')
        # date_list = ttk.Combobox(self, textvariable=dt)
        # days = self.controller.get_days()
        # date_list['value'] = days
        # date_list.pack()
        # date = '2020-01-01'
        # self.__show_time(date)
        app_date = DateEntry(self, date_pattern='mm/dd/y', selectmode='day', showweeknumbers=False)
        app_date.pack()
        # tk.Button(self, text='show time', command=lambda: self.__show_time(dt.get())).pack()

    def __show_time(self, reason):
        if not self.time_show:
            tm = tk.StringVar()
            time_list = ttk.Combobox(self, textvariable=tm, state='disabled')
            times = self.controller.get_time(reason)
            time_list['value'] = times
            time_list.pack()
            self.time_show = True
