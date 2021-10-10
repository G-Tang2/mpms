from controllers.MPMS import MPMS
from controllers.controller import Controller
from views.patient_home_view import PatientHomeView
from controllers.appointment_booking_controller import AppointmentBookingController


class PatientHomeController(Controller):
    def __init__(self, master):
        super().__init__(master)
        self._view = PatientHomeView(master, self)
        self._view.render_view()
        self._load_view()

    def book_appointment(self):
        self._master.load_controller(AppointmentBookingController)
        
