import tkinter as tk
from PIL import ImageTk, Image

class PatientHomeView(tk.Frame):
    def __init__(self, master: tk.Tk, controller) -> None:
        # Initialise frame and set controller
        tk.Frame.__init__(self, master, bg="#c1e4f7")
        self.controller = controller
        # Assisgn image to variable and resize
        icon_booking = Image.open("images/icon_book_appointment.png")
        resized = icon_booking.resize((100,120), Image.ANTIALIAS)
        self.book_appointment_icon  = ImageTk.PhotoImage(resized)
        
        
    def render_view(self, user_name: str) -> None:
        '''
        decide how the patient homepage is displayed
        '''

        # background frame
        outer_label_frame = tk.LabelFrame(self, relief="solid", borderwidth=2, bg="white")
        
        # 'Book Appointment' Button
        tk.Label(outer_label_frame, text="Welcome, {}".format(user_name), font=('Roboto',28, "bold"), bg="white").pack(pady=50)
        tk.Button(outer_label_frame, image = self.book_appointment_icon, bg="white", borderwidth= 0,
                  command=self.controller.book_appointment).pack()
        

        # pack the frames
        outer_label_frame.pack(padx=350, pady=50, fill="x")

        