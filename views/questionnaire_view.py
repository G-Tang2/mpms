import tkinter as tk


class QuestionnaireView(tk.Frame):
    def __init__(self, master: tk.Tk, controller) -> None:
        # Initialise frame and set controller
        tk.Frame.__init__(self, master, bg="#c1e4f7")
        self.controller = controller
        # self.__render_view(master)

    def render_view(self, master: tk.Tk, questions) -> None:

        outer_label_frame = tk.LabelFrame(self, relief="solid", borderwidth=2, bg="white")

        inner_label_frame = tk.LabelFrame(outer_label_frame, relief="flat", bg="white")

        questions = questions.get_question_list()

        tk.Label(outer_label_frame, text=questions[0].get_question()[:104] + '\n' + questions[0].get_question()[104:], width=120, height=5, bg="white").pack()
        ans_1 = tk.StringVar()
        ans_1.set('None')
        q1_frame = tk.Frame(outer_label_frame)
        q1_frame.pack()
        tk.Radiobutton(q1_frame, text='Yes', variable=ans_1, value='Yes').pack(side='left')
        tk.Radiobutton(q1_frame, text='No', variable=ans_1, value='No').pack(side='right')

        tk.Label(outer_label_frame, text=questions[1].get_question()[:100] + '\n' + questions[1].get_question()[100:], width=120, height=5, bg="white").pack()
        ans_2 = tk.StringVar()
        ans_2.set('None')
        q2_frame = tk.Frame(outer_label_frame)
        q2_frame.pack()
        tk.Radiobutton(q2_frame, text='Yes', variable=ans_2, value='Yes').pack(side='left')
        tk.Radiobutton(q2_frame, text='No', variable=ans_2, value='No').pack(side='right')

        tk.Label(outer_label_frame, text=questions[2].get_question()[:100] + '\n' + questions[2].get_question()[100:], width=120, height=5, bg="white").pack()
        ans_3 = tk.StringVar()
        ans_3.set('None')
        q3_frame = tk.Frame(outer_label_frame)
        q3_frame.pack()
        tk.Radiobutton(q3_frame, text='Yes', variable=ans_3, value='Yes').pack(side='left')
        tk.Radiobutton(q3_frame, text='No', variable=ans_3, value='No').pack(side='left')

        tk.Button(inner_label_frame, text='Confirm',command=lambda: self.confirm_question(ans_1.get(), ans_2.get(), ans_3.get())).pack(side = 'right' ,pady=30, padx=150)
        tk.Button(inner_label_frame, text='Back', command=self.controller.back).pack(side = 'left', pady=30, padx = 150)

        
        # outer_label_frame.pack(fill="x")
        outer_label_frame.pack(padx=50, pady=50, fill="both")
        inner_label_frame.pack(padx=50, fill="x")

    def confirm_question(self, ans1, ans2, ans3):
        for i in [ans1, ans2, ans3]:
            if i == 'None':
                tk.messagebox.showerror(title='No', message='please complete all the questions', width=100)
                return

        for i in [ans1, ans2, ans3]:
            if i == 'Yes':
                tk.messagebox.showerror(title='No',
                                                  message='"Please search on health.gov.au and attend a free COVID-19 respiratory clinic"')
                return

        self.make_appointment()

    def make_appointment(self):
        branch = self.controller.get_branch()
        appointment_data = self.controller.get_data()

        confirm = tk.messagebox.askokcancel(title='Confirming',
                                            message='You are going to have an appointment at: '
                                                    + branch + '\nGP: ' + appointment_data[0] +
                                                    '\nReason: ' + appointment_data[1]
                                                    + '\nNew patient: ' + appointment_data[2] +
                                                    '\nDate: ' + appointment_data[3].strftime('%y-%m-%d') +
                                                    '\nTime: ' + appointment_data[4])

        if confirm:
            self.controller.write_appointment()
            tk.messagebox.showinfo(title='Successfully',
                                   message='You have made an appointment \nPlease attend on time')
