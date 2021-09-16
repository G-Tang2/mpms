import tkinter as tk
import tkinter.font as tkFont
from views.login_view import LoginView

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
        frame_names = [LoginView]

        for F in (frame_names):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location.
            # the one on the top of the stacking order 
            # will be the one that is visible
            frame.grid(row=0, column=0, sticky="nsew")

        # show login page
        self.show_frame("LoginView")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
