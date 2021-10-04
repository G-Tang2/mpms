import tkinter as tk

class AdminHomeView(tk.Frame):
    def __init__(self, master: tk.Tk) -> None:
        # Initialise frame and set controller
        tk.Frame.__init__(self, master,bg="#c1e4f7")
        self.pack_propagate(False)
        self.pack(side="top", fill="both", expand=True)
        self.__render_view(master)

    def __render_view(self, master: tk.Tk) -> None:
        # header
        tk.Label(self, text="   Monash Clinic", font=('Roboto',38, "bold"), anchor="w", bg="white").pack(ipady=10, fill="x")
        
        # divider
        tk.Frame(self, bg="black", height=2).pack(fill="x")

        # container for login details
        outer_label_frame = tk.LabelFrame(self, relief="solid", borderwidth=2, bg="white")

        inner_label_frame = tk.LabelFrame(outer_label_frame, relief="flat", bg="white")
        
        # 'Status Report' Button

        tk.Label(outer_label_frame, text = "", height = 4).pack()
        tk.Button(outer_label_frame, text = "Status Report",width=18, height=5,command = master.main_controller.status_report).pack()
        tk.Label(outer_label_frame, text = "", height = 4).pack()

        inner_label_frame.pack(padx=50, fill="x")
        outer_label_frame.pack(padx=350, pady=50, fill="x")

