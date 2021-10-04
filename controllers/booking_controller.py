import tkinter as tk
from controllers.MPMS import MPMS
from views.booking_view import BookView
from controllers.gp_controller import GPController
from models.branch_list import BranchList


class BookController(MPMS):
    def __init__(self, master: tk.Tk) -> None:
        self.branches = BranchList()
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
        new_frame._render_view(master, self.branches.get_branch_list())
        # remove frame if tk instance has a frame
        if master.main_frame is not None:
            master.main_frame.destroy()
        # assign new frame to tk instance
        master.main_frame = new_frame
        master.main_frame.grid_propagate(False)
        master.main_frame.pack(side="top", fill="both", expand=True)

    def next(self, listbox):
        # create a StringVar value to store the value from listbox
        # var = tk.StringVar()

        # get value from the list
        # if listbox.curselection():
            # value = listbox.get('active')
        # else:
            # value = ''

        # display
        # label.config(textvariable=var)
        # var.set(value)

        if listbox.curselection():
            self.__master.load_controller(GPController)
        else:
            print('You do not select any branch')

    def show_branches(self):
        list_of_branches = self.branches.get_branch_list()
        self._view.display_branches(list_of_branches)
