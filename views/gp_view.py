import tkinter as tk


class GPView(tk.Frame):
    def __init__(self, master: tk.Tk, controller) -> None:
        # initialise frame and set controller
        tk.Frame.__init__(self, master)
        self.pack_propagate(False)
        self.pack(side="top", fill="both", expand=True)
        self.controller = controller

    def render_view(self, master: tk.Tk, list_of_gps) -> None:

        # page content
        listbox = tk.Listbox(self)
        for gp in list_of_gps:
            listbox.insert('end', gp)
        listbox.pack()
        tk.Button(self, text='next', width=15, height=2, command=lambda: self.next(listbox)).pack()
        tk.Button(self, text='select_clear', width=15, height=2, command=lambda: self.selection_clear(listbox)).pack()

    def selection_clear(self, listbox):
        listbox.selection_clear(0, 'end')

    def next(self, listbox):
        if listbox.curselection():
            value = listbox.get('active')
        else:
            value = ''

        self.controller.make_appointment(value)



