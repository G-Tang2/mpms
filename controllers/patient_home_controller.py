from controllers.MPMS import MPMS
from views.patient_home_view import PatientHomeView
from controllers.appointment_booking_controller import AppointmentBookingController


class PatientHomeController(MPMS):
    def __init__(self, master, view=PatientHomeView):
        MPMS.__init__(self, master, view)

    def book_appointment(self):
        self._master.load_controller(AppointmentBookingController)
        pass
