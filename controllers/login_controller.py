from views.login_view import LoginView

class LoginController():
    # initialise frame dictionary
    def __init__(self, master):
        self.set_controller()
        self.load_view(master)

    def set_controller(self):
        self.main_controller = self

    def load_view(self, master):
        new_frame = LoginView(master)
        if master.main_frame is not None:
            master.main_frame.destroy()
        master.main_frame = new_frame
        master.main_frame.grid_propagate(False)
        master.main_frame.pack(side="top", fill="both", expand=True)
