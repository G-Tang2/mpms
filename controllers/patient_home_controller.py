import tkinter as tk
from models.MPMS import MPMS
from controllers.controller import Controller
from views.patient_home_view import PatientHomeView
from controllers.appointment_booking_controller import AppointmentBookingController


class PatientHomeController(Controller):
    def __init__(self, master: tk.Tk) -> None:
        super().__init__(master)
        self.MPMS = MPMS.get_instance()
        self._view = PatientHomeView(master, self)
        self._initialise_view()
        self._load_view()

    def _initialise_view(self) -> None:
        login = self.MPMS.get_login()
        user_name = login.get_user_name()
        self._view.render_view(user_name)

    def book_appointment(self) -> None:
        '''
        Loads appointment booking view and controls
        '''
        self._master.load_controller(AppointmentBookingController)
        
