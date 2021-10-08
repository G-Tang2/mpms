# Parent controller stub
from models.apppointment_list import AppointmentList
import tkinter as tk
# from views.login_view import LoginView
# from views.patient_home_view import PatientHomeView
from models.branch_list import BranchList

class MPMS():
    def __init__(self, master: tk.Tk, view) -> None:
        # master is an tk instance
        self._master = master
        self._view = view(master, self)
        self.list_of_branches = BranchList.create_from_csv()
        self.__load_view(master)
        instance = None
        # list_of_appointments = self.__fetch_appointment_list()

    def __load_view(self, master: tk.Tk) -> None:
        # remove frame if tk instance has a frame
        if master.body_frame is not None:
            master.body_frame.destroy()
        # assign new frame to tk instance
        master.body_frame = self._view
        master.body_frame.grid_propagate(False)
        master.body_frame.pack(side="top", fill="both", expand=True)  

    def __fetch_appointment_list(self):
        return AppointmentList()

    def get_list_of_branches(self):
        return self.list_of_branches

    @staticmethod
    def get_instance():
        if MPMS.instance is None:
            MPMS.instance = MPMS()
        return MPMS.instance
    