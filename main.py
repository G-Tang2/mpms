import tkinter as tk
from controllers.login_controller import LoginController
from controllers.MPMS import MPMS

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        # set window title
        self.title("Monash Patient Management System (MPMS)")
        # center window on display
        self.__center_window()
        # set header frame
        # self.header = 
        # body frame
        self.body_frame = None
        # default controller
        LoginController(self)
        # login token
        self.login = None

    def __center_window(self):
        display_w, display_h = self.winfo_screenwidth(), self.winfo_screenheight()
        window_w, window_h = 1200, 800
        self.geometry("%dx%d+%d+%d" % (window_w, window_h, display_w/2 - window_w/2, display_h/2 - window_h/2))

    def load_controller(self, controller: MPMS) -> None:
        self.main_controller = controller(self)


if __name__ == "__main__":
    app = App()
    app.mainloop()
    