import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, master):
        self.master = master
        self.title_font = tkFont.Font(family='Roboto', size=10)

        # the container is where we'll stack a bunch of frames 
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self.master, width=1200, height=800)
        container.grid_propagate(False)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # initialise frame dictionary
        self.frames = {}

        # enter frame names here
        frame_names = [LoginPage]

        for F in (frame_names):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location.
            # the one on the top of the stacking order 
            # will be the one that is visible
            frame.grid(row=0, column=0, sticky="nsew")

        # show login page
        self.show_frame("LoginPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        # initialise frame and set controller
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # declare variables
        username = tk.StringVar()
        password = tk.StringVar()

        # page title
        tk.Label(self, text="Log In").pack()
        tk.Label(self, text = "").pack()

        # email detail
        tk.Label(self, text = "Email").pack()
        tk.Entry(self, textvariable = username).pack()

        # password detail
        tk.Label(self, text = "Password").pack()
        tk.Entry(self, textvariable = password).pack()
        tk.Label(self, text = "").pack()
        # login button
        tk.Button(self, text = "Login", width=10, height=1, command = self.login).pack()

        # sign up button
        tk.Button(self, text = "Sign Up", width=10, height=1, command = self.registration).pack()

    def login(self):
        print("Logged in")

    def registration(self):
        print("Registration page hasn't been implemented!")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
