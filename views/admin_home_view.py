import tkinter as tk

class AdminHomeView(tk.Frame):
    def __init__(self, master: tk.Tk, controller) -> None:
        # Initialise frame and set controller
        tk.Frame.__init__(self, master,bg="#c1e4f7")
        self.controller = controller
        self.__render_view(master)

    def __render_view(self, master: tk.Tk) -> None:
        # container for login details
        outer_label_frame = tk.LabelFrame(self, relief="solid", borderwidth=2, bg="white")

        inner_label_frame = tk.LabelFrame(outer_label_frame, relief="flat", bg="white")
        
        # 'Status Report' Button
        tk.Button(outer_label_frame, text="Status Report", width=18, height=5, bg="white", command = self.controller.status_report).pack(pady=50)

        inner_label_frame.pack(padx=50, fill="x")
        outer_label_frame.pack(padx=350, pady=50, fill="x")

