from datetime import datetime
import tkinter as tk
from typing import List, Tuple

from models.question import Question


class QuestionnaireView(tk.Frame):
    def __init__(self, master: tk.Tk, controller) -> None:
        # Initialise frame and set controller
        tk.Frame.__init__(self, master, bg="#c1e4f7")
        self.controller = controller

    def render_view(self, questions: List[Question], branch: str) -> None:
        '''
        decide how the questionnaire is displayed
        '''

        # background Frame
        outer_label_frame = tk.LabelFrame(self, relief="solid", width=1100, borderwidth=2, bg="white")
        outer_label_frame.grid_propagate(0)
        inner_label_frame = tk.LabelFrame(outer_label_frame, relief="flat", bg="white")

        # title
        tk.Label(outer_label_frame, text="COVID Questionnaire", font=('Roboto', 28, "bold"), bg="white").pack(pady=(50, 30))

        # get how many questions in the question
        question_count = len(questions)
        ans = []
        frames = []

        # create the variable and frames based on the count of the questions
        for _ in range(question_count):
            ans.append(tk.StringVar(value="None"))
            frames.append(tk.Frame(outer_label_frame, bg="white"))

        # display all the questions and radiobuttons
        for i in range(question_count):
            tk.Label(frames[i], text="{}. {}".format(i+1, questions[i].get_question()), justify='center', wraplength=700, bg="white").pack()
            radio_frame = tk.Frame(frames[i], bg="white")
            tk.Radiobutton(radio_frame, text='Yes', variable=ans[i], value='Yes', bg="white").pack(side='left',padx=(0, 30), pady=5)
            tk.Radiobutton(radio_frame, text='No', variable=ans[i], value='No', bg="white").pack(side='right',padx=(30, 0), pady=5)
            radio_frame.pack()
            frames[i].pack(padx=20,pady=10)
            tk.Frame(outer_label_frame, bg="black", height=1).pack(padx=50, fill="x")

        # Buttons
        tk.Button(inner_label_frame, text='Confirm', borderwidth=2, relief="solid", bg="#99d2f2", activebackground="#81c8f0",
            command=lambda: self.check_question(ans, self.controller.get_data(), branch)).pack(side = 'right', ipadx=10 ,pady=30, padx=(0,170))
        tk.Button(inner_label_frame, text='Back', borderwidth=2, relief="solid", bg="#99d2f2", activebackground="#81c8f0", 
            command=self.controller.back).pack(side = 'left',ipadx=10, pady=30, padx = (170,0))

        # pack the background frames
        outer_label_frame.pack(pady=50, ipadx=30)
        inner_label_frame.pack(padx=100, fill="x")

    def check_question(self, ans: List[tk.StringVar], appointment_data: Tuple[str, str, str, datetime, str], branch: str) -> bool:
        '''
        to check if the question is complete and if the patient meet the requirement
        '''

        # if some of the question is not complete, display the message to patient
        for each_answer in ans:
            if each_answer.get() == 'None':
                tk.messagebox.showerror(title='Incomplete Questionnaire', message='Please complete all the questions.')
                return False
            elif each_answer.get() == 'Yes':
                tk.messagebox.showerror(title='Requirement Not Meet',
                                                  message='Please search on health.gov.au and attend a free COVID-19 respiratory clinic')
                return False

        # if the questionnaire part is ok, to display the confirming message box
        return self.make_appointment(appointment_data, branch)

    def reload_values(self):
        pass

    def make_appointment(self, appointment_data: Tuple[str, str, str, datetime, str], branch: str) -> bool:
        '''
        display the confirmation message and write to the file
        '''

        # display the confirming message box
        confirm = tk.messagebox.askokcancel(title='Confirmation',
                                            message='You are going to have an appointment at: '
                                                    + branch + '\n\nGP: ' + appointment_data[0] +
                                                    '\n\nReason: ' + appointment_data[1]
                                                    + '\n\nNew patient: ' + appointment_data[2] +
                                                    '\n\nDate: ' + appointment_data[3].strftime("%d/%m/%Y") +
                                                    '     Time: ' + appointment_data[4])

        # if the patient click ok, display the appointment done message and write the details to the file
        if confirm:
            self.controller.write_appointment()
            tk.messagebox.showinfo(title='Successfully',
                                   message='You have made an appointment. \nPlease attend on time.')

            self.controller.return_home()
            return True
        else:
            return False
