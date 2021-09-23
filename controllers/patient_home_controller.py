import tkinter as tk
from controllers.MPMS import MPMS
from views.patient_home_view import PatientHomeView

class PatientHomeController(MPMS):
    def __init__(self,master,view = PatientHomeView):
        MPMS.__init__(self,master,view)

    def book_appointment(self):
        #self._master.load_controller()
        pass
        