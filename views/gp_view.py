import tkinter as tk


class GPView(tk.Frame):
    def __init__(self, master: tk.Tk, controller) -> None:
        # initialise frame and set controller
        tk.Frame.__init__(self, master)
        self.pack_propagate(False)
        self.pack(side="top", fill="both", expand=True)
        self.controller = controller

    def render_view(self, master: tk.Tk) -> None:

        # page content
        tk.Label(self, text='Monash Clinic', width=800, height=2, bg='lightskyblue').pack()
        listbox = tk.Listbox(self)
        self.controller.show_gps(listbox)
        listbox.pack()
        tk.Button(self, text='next', width=15, height=2, command=self.controller.next_appointment).pack()
        tk.Button(self, text='select_clear', width=15, height=2, command=lambda: self.selection_clear(listbox)).pack()

    def selection_clear(self, listbox):
        listbox.selection_clear(0, 'end')

