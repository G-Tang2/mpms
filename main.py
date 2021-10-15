import tkinter as tk
from controllers.controller import Controller
from controllers.header_controller import HeaderController
from controllers.login_controller import LoginController

class App(tk.Tk):
    def __init__(self) -> None:
        tk.Tk.__init__(self)
        # set window title
        self.title("Monash Patient Management System (MPMS)")
        self.__center_window()
        self.__setup_styling()
        # login state
        self.login = None
        # set header frame
        self.header_controller = HeaderController(self)
        self.body_frame = None
        # default controller
        self.main_controller = None
        self.load_controller(LoginController)

    def __center_window(self) -> None:
        '''
        Set window dimension and center it on screen
        '''
        display_w, display_h = self.winfo_screenwidth(), self.winfo_screenheight()
        window_w, window_h = 1200, 850
        self.geometry("%dx%d+%d+%d" % (window_w, window_h, display_w/2 - window_w/2, display_h/2 - window_h/2))

    def __setup_styling(self) -> None:
        """
        Set default styling
        """
        # default font
        self.option_add("*Font", "Roboto 14")

    def load_controller(self, controller: Controller) -> None:
        """
        Instantiates controller
        """
        self.main_controller = controller(self)


if __name__ == "__main__":
    app = App()
    app.mainloop()
    