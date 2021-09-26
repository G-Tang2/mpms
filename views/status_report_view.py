import tkinter as tk

class StatusReportView(tk.Frame):
    def __init__(self, master: tk.Tk) -> None:
        # Initialise frame and set controller
        tk.Frame.__init__(self, master, width=1200, height=800)
        self.pack_propagate(False)
        self.pack(side="top", fill="both", expand=True)
        self.__render_view(master)
        # for testing
        self.show_appointment_reasons(master.main_controller.get_appointment_reasons())

    def __render_view(self, master: tk.Tk) -> None:
        # 'Monash Clinic' Header
        tk.Label(self, text="Monash Clinic", font=('Roboto',44), bg = '#67b9e6',width=500).pack()
        tk.Label(self, text = "").pack()

        options = ['GP','Reason','Clinic']
        #valueinside = tk.StringVar(self)
        start_date = tk.StringVar()
        end_date = tk.StringVar()
        report_type = tk.StringVar()

        # 'Book Appointment' Button
        tk.Label(self, text = "Start Date", width=18, height=5).pack()
        tk.OptionMenu(self,start_date,*options).pack()
        tk.Label(self, text = "").pack()

        tk.Label(self, text = "End Date", width=18, height=5).pack()
        tk.OptionMenu(self,end_date,*options).pack()
        tk.Label(self, text = "").pack()

        tk.Label(self, text = "Report Type", width=18, height=5).pack()
        tk.OptionMenu(self,report_type,*options).pack()
        tk.Label(self, text = "").pack()

    # for testing
    def show_appointment_reasons(self, appointment_reasons):
        for reason in appointment_reasons:
            tk.Label(self, text = reason).pack()