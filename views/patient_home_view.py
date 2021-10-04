import tkinter as tk

class PatientHomeView(tk.Frame):
    def __init__(self, master: tk.Tk, controller) -> None:
        # Initialise frame and set controller
        tk.Frame.__init__(self, master)
        self.pack_propagate(False)
        self.pack(side="top", fill="both", expand=True)
        self.controller = controller
        self.__render_view(master)

    def __render_view(self, master: tk.Tk) -> None:
        # 'Monash Clinic' Header
        tk.Label(self, text="Monash Clinic", font=('Roboto',44), bg = '#67b9e6',width=500).pack()
        tk.Label(self, text = "").pack()

        # 'Book Appointment' Button
        tk.Button(self, text = "Book Appointment", width=18, height=5, command=self.controller.book_appointment).pack()
        tk.Label(self, text = "").pack()

