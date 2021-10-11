import tkinter as tk

class PatientHomeView(tk.Frame):
    def __init__(self, master: tk.Tk, controller) -> None:
        # Initialise frame and set controller
        tk.Frame.__init__(self, master, bg="#c1e4f7")
        self.controller = controller
        

    def render_view(self) -> None:
        outer_label_frame = tk.LabelFrame(self, relief="solid", borderwidth=2, bg="white")

        inner_label_frame = tk.LabelFrame(outer_label_frame, relief="flat", bg="white")
        
        # 'Book Appointment' Button
        tk.Label(outer_label_frame, text="Welcome", font=('Roboto',28, "bold"), bg="white").pack(pady=(30, 30))
        tk.Button(inner_label_frame, text = "Book Appointment", width=20, height=5,
                  command=self.controller.book_appointment).pack(padx=50, pady=30)

        
        inner_label_frame.pack(padx=50, fill="x")
        outer_label_frame.pack(padx=350, pady=50, fill="x")

        