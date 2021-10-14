import tkinter as tk

class PatientHomeView(tk.Frame):
    def __init__(self, master: tk.Tk, controller) -> None:
        # Initialise frame and set controller
        tk.Frame.__init__(self, master, bg="#c1e4f7")
        self.controller = controller
        self.book_appointment_icon = tk.PhotoImage(file='images/icon_book_appointment.png')
        self.book_appointment_icon = self.book_appointment_icon.subsample(4, 4)
        

    def render_view(self, user_name: str) -> None:
        '''
        decide how the patient homepage is displayed
        '''

        # background frame
        outer_label_frame = tk.LabelFrame(self, relief="solid", borderwidth=2, bg="white")
        inner_label_frame = tk.LabelFrame(outer_label_frame, relief="flat", bg="white")
        
        # 'Book Appointment' Button
        tk.Label(outer_label_frame, text="Welcome, {}".format(user_name), font=('Roboto',28, "bold"), bg="white").pack(pady=(30, 30))
        tk.Button(outer_label_frame, image = self.book_appointment_icon, bg="white", borderwidth= 0,
                  command=self.controller.book_appointment).pack(pady=50)

        # pack the frames
        inner_label_frame.pack(padx=50, fill="x")
        outer_label_frame.pack(padx=350, pady=50, fill="x")

        