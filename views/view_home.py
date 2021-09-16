import tkinter as tk

class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        # Initialise frame and set controller
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # 'Monash Clinic' Header
        tk.Label(self, text="Monash Clinic", font=('Roboto',44), bg = '#67b9e6',width=500).pack()
        tk.Label(self, text = "").pack()

        tk.Label(self, text = "").pack()
        # 'Book Appointment' Button
        tk.Button(self, text = "Book Appointment", width=18, height=5, command = self.book_appointment).pack()
        tk.Label(self, text = "").pack()
         # 'Upcoming Appointment' Button
        tk.Button(self, text = "Upcoming Appointment", width=18, height=5, command = self.upcoming_appointments).pack()
        tk.Label(self, text = "").pack()
         # 'Favourites' Button
        tk.Button(self, text = "Favourites", width=18, height=5, command = self.favourites).pack()
        
    # Functions
    def book_appointment(self):
        print("Booking an appointment")
        #show_frame(BookingView)

    def favourites(self):
        print("Favourites page hasn't been implemented!")

    def upcoming_appointments(self):
        print("Upcoming appointments page hasn't been implemented!")