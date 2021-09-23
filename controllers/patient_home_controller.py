import tkinter as tk
from controllers.controller import Controller
from views.patient_home_view import PatientHomeView

class PatientHomeController(Controller):
    def __init__(self,master,view = PatientHomeView):
        Controller.__init__(self,master,view)

    def book_appointment(self):
        #self._master.load_controller()
        pass
        