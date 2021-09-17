from controllers.login_controller import LoginController
import tkinter as tk
from controllers.login_controller import LoginController

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        # default frame
        self.main_frame = tk.Frame(self, width=1200, height=800)
        # default controller
        self.main_controller = LoginController(self)

    def load_controller():
        pass

if __name__ == "__main__":
    app = App()
    app.mainloop()
