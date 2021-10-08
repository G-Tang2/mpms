import tkinter as tk
from tkinter import ttk



class AppointmentDetailView(tk.Frame):
    def __init__(self, master: tk.Tk, controller) -> None:
        # initialise frame and set controller
        tk.Frame.__init__(self, master)
        self.controller = controller
        self.time_show = False

    def render_view(self, master: tk.Tk, list_of_gps) -> None:

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
        rea.set('Reason for seeing GP')
        tk.OptionMenu(self, rea, "Long", "Standard", "Tele").pack()

        tk.Button(self, text='next', command=lambda: self.next(listbox, rea.get(), var.get())).pack()

        self.__show_date()


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

        self.make_appointment(gp, reason, patient_status)

    def make_appointment(self, gp, reason, patient_status):
        branch = self.controller.get_branch()

        confirm = tk.messagebox.askokcancel(title='Successfully',
                                            message='You are going to have an appointment at'
                                                    + branch + '\nGP: ' + gp + '\nReason: ' + reason
                                                    + '\nNew patient: ' + patient_status)

        if confirm:
            # self.controller.write_appointment()
            tk.messagebox.askokcancel(title='Successfully',
                                      message='You have made an appointment \nPlease attend on time')

    def __show_date(self):
        dt = tk.StringVar()
        dt.set('None')
        date_list = ttk.Combobox(self, textvariable=dt)
        days = self.controller.get_days()
        date_list['value'] = days
        date_list.pack()
        date = '2020-01-01'
        self.__show_time(date)
        # tk.Button(self, text='show time', command=lambda: self.__show_time(dt.get())).pack()

    def __show_time(self, date):
        if not self.time_show:
            tm = tk.StringVar()
            time_list = ttk.Combobox(self, textvariable=tm)
            times = self.controller.get_time(date)
            # times = ['1', '2']
            time_list['value'] = times
            time_list.pack()
            self.time_show = True

