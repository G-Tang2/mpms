import tkinter as tk
from PIL import ImageTk, Image

class AdminHomeView(tk.Frame):
    def __init__(self, master: tk.Tk, controller) -> None:
        # Initialise frame and set controller
        tk.Frame.__init__(self, master,bg="#c1e4f7")
        self.controller = controller
        
        icon_report = Image.open("images/icon_status_report.png")
        resized = icon_report.resize((110,120), Image.ANTIALIAS)
        self.status_report_icon  = ImageTk.PhotoImage(resized)

    def render_view(self, user_name: str) -> None:
        # container for login details
        outer_label_frame = tk.LabelFrame(self, relief="solid", borderwidth=2, bg="white")
        
        # 'Status Report' Button
        tk.Label(outer_label_frame, text="Welcome, {}".format(user_name), font=('Roboto', 28, "bold"), bg="white").pack(pady=50)
        tk.Button(outer_label_frame, image = self.status_report_icon, bg="white", borderwidth= 0, 
            command = self.controller.status_report).pack(pady=(0,40))
        

        outer_label_frame.pack(padx=350, pady=50, fill="x")

