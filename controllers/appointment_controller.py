import tkinter as tk
from controllers.MPMS import MPMS
from views.booking_view import BookView
from views.gp_view import GPView
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
        new_frame = BookView(master, self)
        # sort branch list based on branch name (alphabetical order)
        # list_of_branch =
        new_frame.render_view(master, self.branches.get_branch_list())
        # remove frame if tk instance has a frame
        if master.body_frame is not None:
            master.body_frame.destroy()
        # assign new frame to tk instance
        master.body_frame = new_frame
        master.body_frame.grid_propagate(False)
        master.body_frame.pack(side="top", fill="both", expand=True)

    def next(self, master: tk.Tk) -> None:
        new_frame = GPView(master, self)
        new_frame.render_view(master)

        if master.body_frame is not None:
            master.body_frame.destroy()

        master.body_frame = new_frame
        master.body_frame.grid_propagate(False)
        master.body_frame.pack(side="top", fill="both", expand=True)

    def show_gps(self, listbox):
        # move to view
        listbox.insert('end', 'GP1\n')
        listbox.insert('end', 'GP2\n')
        listbox.insert('end', 'GP3\n')

    def next_appointment(self):
        tk.messagebox.askokcancel(title='Successfully', message='You have made an appointment')
