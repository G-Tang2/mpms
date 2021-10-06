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
        self.branch = 'None'
        self.gp = 'None'
        self.patient_status = 'None'

    def __set_controller(self, master: tk.Tk) -> None:
        # set controller in tk instance
        master.main_controller = self

    def __load_view(self, master: tk.Tk) -> None:
        # create new view
        new_frame = BookView(master, self)
        # new: sort branch list based on branch name (alphabetical order)
        sorted_branches = []
        for branch in self.branches.get_branch_list():
            sorted_branches.append(branch.get_name())

        sorted_branches = self.selection_sort(sorted_branches)

        new_frame.render_view(master, sorted_branches)
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
        for branch in self.branches.get_branch_list():
            if self.branch == branch.get_name():
                list_of_gps = branch.get_gps()
                break

        new_frame.render_view(master, list_of_gps)

        if master.body_frame is not None:
            master.body_frame.destroy()

        master.body_frame = new_frame
        master.body_frame.grid_propagate(False)
        master.body_frame.pack(side="top", fill="both", expand=True)

    def make_appointment(self, gp, reason):
        if not gp == '':
            self.gp = gp

        confirm = tk.messagebox.askokcancel(title='Successfully',
                                            message='You are going to have an appointment at'
                                                    + self.branch + '\nGP: ' + self.gp + '\nReason: ' + reason
                                            + '\nPatient Status: ' + self.patient_status)

        if confirm:
            self.write_appointment()
            tk.messagebox.askokcancel(title='Successfully',
                                      message='You have made an appointment \nPlease attend on time')

    def change_status(self, var):
        self.patient_status = var.get()
        print(self.patient_status)

    def selection_sort(self, the_list):
        # obtain the length of the list
        n = len(the_list)
        # perform n-1 iterations
        for i in range(n - 1):
            # assume item at index i as the smallest
            smallest = i
            # check if any other item is smaller
            for j in range(i + 1, n):
                if the_list[j] < the_list[smallest]:
                    # update the current smallest item
                    smallest = j

            # place the current smallest item
            # in its correct position
            the_list[smallest], the_list[i] = the_list[i], the_list[smallest]

        return the_list

    def write_appointment(self):
        pass
