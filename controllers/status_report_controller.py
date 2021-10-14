from controllers.controller import Controller
from models.MPMS import MPMS
from views.status_report_view import StatusReportView
from datetime import datetime
import datetime

class StatusReportController(Controller):
    def __init__(self,master):
        super().__init__(master)
        self._view = StatusReportView(master, self)
        self._view.render_view()
        self._load_view()
        self.MPMS = MPMS.get_instance() 

    def get_reason_report(self, start_date: str, end_date: str, report_type: str):
        '''
        Validates the status-report view input. Returns errors message if invalid.
        Calls view function to display the reason report
        '''
        # Validate the format of date input
        try:
            start_datetime = datetime.datetime.strptime(start_date, '%d/%m/%Y')
            end_datetime = datetime.datetime.strptime(end_date, '%d/%m/%Y')
        except ValueError:
            self._view.display_input_error("Incorrect date format input \n(Use DD/MM/YYYY)")
            return
        # Validates start date occurs before end date
        if start_datetime > end_datetime:

            self._view.display_input_error("Start date should be earlier than end date")
            return
        # Use MPMS instance and calls function to obtain reason statistic from MPMS
        if report_type.lower() == "reason":
            reason_dict = self.MPMS.calculate_reason_statistic(start_datetime, end_datetime)
        # Returns error if no appointments occured with give time period 
        if len(reason_dict) == 0:
            self._view.display_input_error("No appointments within this period")
            return
        # Calls view function to display reason report
        self._view.display_reason_report(reason_dict, start_date, end_date)