# Parent controller stub
import tkinter as tk
# from views.login_view import LoginView
# from views.patient_home_view import PatientHomeView
from models.branch_list import BranchList


class MPMS():
    def __init__(self, master: tk.Tk, view) -> None:
        # master is an tk instance
        self._master = master
        self.__view = view
        self.__set_controller(master)
        self.__load_view(master)
        list_of_branches = self.__fetch_branch_list()

        
    def __set_controller(self, master: tk.Tk) -> None:
        # set controller in tk instance
        master.main_controller = self

    def __load_view(self, master: tk.Tk) -> None:
        # create new view
        new_frame = self.__view(master)
        # remove frame if tk instance has a frame
        if master.main_frame is not None:
            master.main_frame.destroy()
        # assign new frame to tk instance
        master.main_frame = new_frame
        master.main_frame.grid_propagate(False)
        master.main_frame.pack(side="top", fill="both", expand=True)  

    def __fetch_branch_list(self):
        return BranchList()
    