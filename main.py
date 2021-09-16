from controllers.login_controller import LoginController
import tkinter as tk
import tkinter.font as tkFont
from views.login_view import LoginView
from controllers.login_controller import LoginController

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.main_frame = tk.Frame(self, width=1200, height=800)
        self.main_controller = LoginController(self)

if __name__ == "__main__":
    app = App()
    app.mainloop()
