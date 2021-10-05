from controllers.MPMS import MPMS
from views.patient_home_view import PatientHomeView
from controllers.appointment_controller import BookController


class PatientHomeController(MPMS):
    def __init__(self, master, view=PatientHomeView):
        MPMS.__init__(self, master, view)

    def book_appointment(self):
        self._master.load_controller(BookController)
        pass
