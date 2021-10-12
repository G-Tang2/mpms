import tkinter as tk

class AdminHomeView(tk.Frame):
    def __init__(self, master: tk.Tk, controller) -> None:
        # Initialise frame and set controller
        tk.Frame.__init__(self, master,bg="#c1e4f7")
        self.controller = controller
        self.status_report_icon = tk.PhotoImage(file = 'images/icon_status_report.png')
        self.status_report_icon = self.status_report_icon .subsample(4,4)

    def render_view(self) -> None:
        # container for login details
        outer_label_frame = tk.LabelFrame(self, relief="solid", borderwidth=2, bg="white")

        inner_label_frame = tk.LabelFrame(outer_label_frame, relief="flat", bg="white")
        
        # 'Status Report' Button
        tk.Label(outer_label_frame, text="Welcome", font=('Roboto',28, "bold"), bg="white").pack(pady=(30, 30))
        tk.Button(outer_label_frame, image = self.status_report_icon, bg="white", borderwidth= 0, 
            command = self.controller.status_report).pack(pady=50)

        inner_label_frame.pack(padx=50, fill="x")
        outer_label_frame.pack(padx=350, pady=50, fill="x")

