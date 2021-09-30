import tkinter as tk


class GPView(tk.Frame):
    def __init__(self, master: tk.Tk) -> None:
        # initialise frame and set controller
        tk.Frame.__init__(self, master, width=1200, height=800)
        self.pack_propagate(False)
        self.pack(side="top", fill="both", expand=True)
        self.__render_view(master)

    def __render_view(self, master: tk.Tk) -> None:

        # page content
        tk.Label(self, text='Monash Clinic', width=800, height=2, bg='lightskyblue').pack()
        listbox = tk.Listbox(self)
        label = tk.Label(self, width=800, height=2, bg='lightskyblue')
        master.main_controller.show_gps(listbox)
        listbox.pack()
        tk.Button(self, text='show_selection', width=15, height=2,
                  command=lambda: master.main_controller.show_selection(listbox, label)).pack()
        label.pack()

