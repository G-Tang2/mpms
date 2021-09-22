import tkinter as tk

class PatientHomeView(tk.Frame):
    def __init__(self, master: tk.Tk) -> None:
        # Initialise frame and set controller
        tk.Frame.__init__(self, master, width=1200, height=800)
        self.pack_propagate(False)
        self.pack(side="top", fill="both", expand=True)
        self.__render_view(master)

    def __render_view(self, master: tk.Tk) -> None:
        # 'Monash Clinic' Header
        tk.Label(self, text="Monash Clinic", font=('Roboto',44), bg = '#67b9e6',width=500).pack()
        tk.Label(self, text = "").pack()

        # 'Book Appointment' Button
        tk.Button(self, text = "Book Appointment", width=18, height=5).pack()
        tk.Label(self, text = "").pack()

         # 'Upcoming Appointment' Button
        tk.Button(self, text = "Upcoming Appointment", width=18, height=5).pack()
        tk.Label(self, text = "").pack()

         # 'Favourites' Button
        tk.Button(self, text = "Favourites", width=18, height=5).pack()
