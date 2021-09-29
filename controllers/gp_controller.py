import tkinter as tk
from controllers.MPMS import MPMS
from views.gp_view import GPView


class GPController(MPMS):
    def __init__(self, master: tk.Tk) -> None:
        # master is an tk instance
        self.__set_controller(master)
        self.__load_view(master)
        self.__master = master

    def __set_controller(self, master: tk.Tk) -> None:
        # set controller in tk instance
        master.main_controller = self

    def __load_view(self, master: tk.Tk) -> None:
        # create new view
        new_frame = GPView(master)
        # remove frame if tk instance has a frame
        if master.main_frame is not None:
            master.main_frame.destroy()
        # assign new frame to tk instance
        master.main_frame = new_frame
        master.main_frame.grid_propagate(False)
        master.main_frame.pack(side="top", fill="both", expand=True)

    def show_selection(self, listbox, label):
        var = tk.StringVar()

        if listbox.curselection():
            value = listbox.get('active')
        else:
            value = ''

        label.config(textvariable=var)
        var.set(value)

    def show_gps(self, listbox):
        listbox.insert('end', 'GP1\n')
        listbox.insert('end', 'GP2\n')
        listbox.insert('end', 'GP3\n')
