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

    def get_reason_report(self, start_date, end_date, report_type):
        '''
        Validates the status-report view input. Returns errors message if invalid.
        Calls view function to display the reason report
        '''
        # Validate the format of date input
        try:
            start_date_check = datetime.datetime.strptime(start_date, '%d/%m/%Y')
            end_date_check = datetime.datetime.strptime(end_date, '%d/%m/%Y')
        except ValueError:
            self._view.display_input_error("Incorrect date format input \n(Use DD/MM/YYYY)")
            return
        # Validates start date occurs before end date
        if start_date >= end_date:
            
            self._view.display_input_error("Start date should be earlier than end date")
            return
        # Use MPMS instance and calls function to obtain reason statistic from MPMS
        mpms_instance = MPMS.get_instance()  
        reason_dict = mpms_instance.calculate_reason_statistic(start_date,end_date,report_type)
        # Returns error if no appointments occured with give time period 
        if len(reason_dict) == 0:
            self._view.display_input_error("No appointments within this period")
            return
        # Calls view function to display reason report
        self._view.display_reason_report(reason_dict)