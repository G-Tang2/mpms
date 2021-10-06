import tkinter as tk


class GPView(tk.Frame):
    def __init__(self, master: tk.Tk, controller) -> None:
        # initialise frame and set controller
        tk.Frame.__init__(self, master)
        self.controller = controller

    def render_view(self, master: tk.Tk, list_of_gps) -> None:

        # select GP
        tk.Label(self, text='Please select a GP (optional)').pack()
        listbox = tk.Listbox(self)
        for gp in list_of_gps.get_gps():
            listbox.insert('end', gp.get_full_name())
        listbox.pack()
        tk.Button(self, text='select_clear', width=15, height=2, command=lambda: self.selection_clear(listbox)).pack()

        # new:  patient status
        tk.Label(self, text='Please choose your status').pack()
        var = tk.StringVar()
        var.set('None')
        tk.Radiobutton(self, text='New patient', variable=var, value='New patient').pack()
        tk.Radiobutton(self, text='Existing patient', variable=var, value='Existing patient').pack()

        # new: appointment reason
        tk.Label(self, text='Please choose your reason for appointment').pack()
        rea = tk.StringVar()
        tk.OptionMenu(self, rea, "Long", "Standard", "Tele").pack()

        tk.Button(self, text='next', width=15, height=2,
                  command=lambda: self.next(listbox, rea.get(), var.get())).pack()

    def selection_clear(self, listbox):
        listbox.selection_clear(0, 'end')

    def next(self, listbox, reason, patient_status):
        if listbox.curselection():
            value = listbox.get('active')
        else:
            value = ''

        self.controller.make_appointment(value, reason, patient_status)



