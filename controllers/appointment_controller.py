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
        self.branch = 'none'
        self.gp = 'none'

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

    def display_gp_view(self, master: tk.Tk, branch) -> None:
        self.branch = branch
        new_frame = GPView(master, self)
        list_of_gps = ['Dr Alice', 'Dr Brown', 'Dr Caman']
        new_frame.render_view(master, list_of_gps)

        if master.body_frame is not None:
            master.body_frame.destroy()

        master.body_frame = new_frame
        master.body_frame.grid_propagate(False)
        master.body_frame.pack(side="top", fill="both", expand=True)

    def make_appointment(self, gp):
        if not gp == '':
            self.gp = gp

        confirm = tk.messagebox.askokcancel(title='Successfully',
                                            message='You are going to have an appointment at'
                                                    + self.branch + '\nGP: ' + self.gp)

        if confirm:
            tk.messagebox.askokcancel(title='Successfully',
                                      message='You have made an appointment \nPlease attend on time')
