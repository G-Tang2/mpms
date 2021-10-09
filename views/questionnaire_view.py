import tkinter as tk


class QuestionnaireView(tk.Frame):
    def __init__(self, master: tk.Tk, controller) -> None:
        # Initialise frame and set controller
        tk.Frame.__init__(self, master, bg="#c1e4f7")
        self.controller = controller
        # self.__render_view(master)
        self.gp = 'gp'
        self.reason = 'reason'
        self.patient_status = 'status'
        self.date = 'date'
        self.time = 'time'

    def render_view(self, master: tk.Tk, gp, reason, patient_status, questions, date, time) -> None:

        self.gp = gp
        self.reason = reason
        self.patient_status = patient_status
        self.date = date
        self.time = time
        # container for login details
        outer_label_frame = tk.LabelFrame(self, relief="flat", borderwidth=2, bg="white")

        inner_label_frame = tk.LabelFrame(outer_label_frame, relief="flat", bg="white")

        questions = questions.get_question_list()

        # 'Status Report' Button
        tk.Label(outer_label_frame, text=questions[0].get_question(), width=18, height=10, bg="white").pack()
        ans_1 = tk.StringVar()
        ans_1.set('None')
        tk.Radiobutton(outer_label_frame, text='Yes', variable=ans_1, value='Yes').pack()
        tk.Radiobutton(outer_label_frame, text='No', variable=ans_1, value='No').pack()

        tk.Label(outer_label_frame, text=questions[1].get_question(), width=18, height=5, bg="white").pack()
        ans_2 = tk.StringVar()
        ans_2.set('None')
        tk.Radiobutton(outer_label_frame, text='Yes', variable=ans_2, value='Yes').pack()
        tk.Radiobutton(outer_label_frame, text='No', variable=ans_2, value='No').pack()

        tk.Label(outer_label_frame, text=questions[2].get_question(), width=18, height=5, bg="white").pack()
        ans_3 = tk.StringVar()
        ans_3.set('None')
        tk.Radiobutton(outer_label_frame, text='Yes', variable=ans_3, value='Yes').pack()
        tk.Radiobutton(outer_label_frame, text='No', variable=ans_3, value='No').pack()

        tk.Button(outer_label_frame, text='Confirm',
                  command=lambda: self.confirm_question(ans_1.get(), ans_2.get(), ans_3.get())).pack()

        inner_label_frame.pack(padx=5, fill="x")
        # outer_label_frame.pack(fill="x")
        outer_label_frame.pack(padx=350, pady=50, fill="x")

    def confirm_question(self, ans1, ans2, ans3):
        for i in [ans1, ans2, ans3]:
            if i == 'None':
                tk.messagebox.showerror(title='No', message='please complete all the questions')
                return

        for i in [ans1, ans2, ans3]:
            if i == 'Yes':
                tk.messagebox.showerror(title='No',
                                                  message='"Please search on health.gov.au and attend a free COVID-19 respiratory clinic"')
                return

        self.make_appointment(self.gp, self.reason, self.patient_status, self.date, self.time)

    def make_appointment(self, gp, reason, patient_status, date, time):
        branch = self.controller.get_branch()
        date = date.strftime('%y-%m-%d')

        confirm = tk.messagebox.askokcancel(title='Confirming',
                                            message='You are going to have an appointment at'
                                                    + branch + '\nGP: ' + gp + '\nReason: ' + reason
                                                    + '\nNew patient: ' + patient_status +
                                            '\nDate: ' + date + '\nTime: ' + time)

        if confirm:
            self.controller.write_appointment(patient_status, gp, date, time, reason)
            tk.messagebox.showinfo(title='Successfully',
                                   message='You have made an appointment \nPlease attend on time')
