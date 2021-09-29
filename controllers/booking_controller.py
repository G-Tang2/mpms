import tkinter as tk
from controllers.MPMS import MPMS
from views.booking_view import BookView


class BookController(MPMS):
    def __init__(self, master: tk.Tk) -> None:
        # master is an tk instance
        self.__set_controller(master)
        self.__load_view(master)
        self.__master = master
        # to represent if the branches is already shown
        self.branch_flag = False

    def __set_controller(self, master: tk.Tk) -> None:
        # set controller in tk instance
        master.main_controller = self

    def __load_view(self, master: tk.Tk) -> None:
        # create new view
        new_frame = BookView(master)
        # remove frame if tk instance has a frame
        if master.main_frame is not None:
            master.main_frame.destroy()
        # assign new frame to tk instance
        master.main_frame = new_frame
        master.main_frame.grid_propagate(False)
        master.main_frame.pack(side="top", fill="both", expand=True)

    def show_selection(self, listbox, label):
        # create a StringVar value to store the value from listbox
        var = tk.StringVar()

        # get value from the list
        if listbox.curselection():
            value = listbox.get('active')
        else:
            value = ''

        # display
        label.config(textvariable=var)
        var.set(value)

    def show_branches(self, listbox):
        #insert branches information
        if not self.branch_flag:
            listbox.insert('end', 'Branch1\n')
            listbox.insert('end', 'Branch2\n')
            listbox.insert('end', 'Branch3\n')
            self.branch_flag = True
