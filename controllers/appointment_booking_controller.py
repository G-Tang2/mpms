import tkinter as tk
from controllers.MPMS import MPMS
from views.appointment_view import AppointmentView
from views.appointment_detail_view import AppointmentDetailView
from models.branch_list import BranchList


class AppointmentBookingController(MPMS):
    def __init__(self, master: tk.Tk) -> None:
        MPMS.__init__(self, master, AppointmentView)

        self.branch = 'None'
        self.gp = 'None'

    def sort_branches(self):
        # new: sort branch list based on branch name (alphabetical order)
        self.list_of_branches = BranchList.create_from_csv()

        sorted_branches = []
        for branch in self.list_of_branches.get_branch_list():
            sorted_branches.append(branch.get_name())

        # sorted_branches = self.selection_sort(sorted_branches)
        sorted_branches.sort()

        return sorted_branches

    def display_gp_view(self, master: tk.Tk, branch) -> None:
        self.branch = branch

        self._view = AppointmentDetailView(master, self)

        new_frame = AppointmentDetailView(master, self)

        list_of_gps = []
        for branch in self.list_of_branches.get_branch_list():
            if self.branch == branch.get_name():
                list_of_gps = branch.get_gps()
                break

        new_frame.render_view(master, list_of_gps)

        if master.body_frame is not None:
            master.body_frame.destroy()

        master.body_frame = new_frame
        master.body_frame.grid_propagate(False)
        master.body_frame.pack(side="top", fill="both", expand=True)

    def make_appointment(self, gp, reason, patient_status):

        confirm = self._view.show_confirm(self.branch, gp, reason, patient_status)

        if confirm:
            self.write_appointment()
            self._view.show_success_message()
    
    def show_info(self, branch):
        for each_branch in self.list_of_branches.get_branch_list():
            if branch == each_branch.get_name():
                self._view.show_branch_info(each_branch)

    def write_appointment(self):
        pass
