import tkinter as tk

class AdminHomeView(tk.Frame):
    def __init__(self, master: tk.Tk, controller) -> None:
        # Initialise frame and set controller
        tk.Frame.__init__(self, master,bg="#c1e4f7")
        self.controller = controller
        self.status_report_icon = tk.PhotoImage(file = 'images/icon_status_report.png')
        self.status_report_icon = self.status_report_icon .subsample(4,4)

    def render_view(self, user_name: str) -> None:
        # container for login details
        outer_label_frame = tk.LabelFrame(self, relief="solid", borderwidth=2, bg="white")
        
        # 'Status Report' Button
        tk.Label(outer_label_frame, text="Welcome, {}".format(user_name), font=('Roboto', 28, "bold"), bg="white").pack(pady=50)
        tk.Button(outer_label_frame, image = self.status_report_icon, bg="white", borderwidth= 0, 
            command = self.controller.status_report).pack()
        tk.Label(outer_label_frame, text = "Status Report", font=('Roboto',16), bg="white").pack(pady = (0, 40))

        outer_label_frame.pack(padx=350, pady=50, fill="x")

