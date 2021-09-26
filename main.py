from controllers.status_report_controller import StatusReportController
import tkinter as tk
from controllers.login_controller import LoginController
from controllers.MPMS import MPMS

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        # default frame
        self.main_frame = tk.Frame(self, width=1200, height=800)
        # default controller
        # self.main_controller = LoginController(self)
        # for testing status report
        self.main_controller = StatusReportController(self)

    def load_controller(self, controller: MPMS) -> None:
        self.main_controller = controller(self)

if __name__ == "__main__":
    app = App()
    app.mainloop()
    