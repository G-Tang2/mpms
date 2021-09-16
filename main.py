from controllers.login_controller import LoginController
import tkinter as tk
import tkinter.font as tkFont
from views.login_view import LoginView
from controllers.login_controller import LoginController

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.main_frame = LoginView(self)
        self.main_frame.pack_propagate(False)
        self.main_frame.pack(side="top", fill="both", expand=True)

if __name__ == "__main__":
    app = App()
    app.mainloop()
