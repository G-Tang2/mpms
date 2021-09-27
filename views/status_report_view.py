import tkinter as tk
from tkinter import ttk
from tkinter.constants import E, NO, W
from tkcalendar import *

class StatusReportView(tk.Frame):
    def __init__(self, master: tk.Tk) -> None:
        # Initialise frame and set controller
        tk.Frame.__init__(self, master, width=1200, height=800)
        self.pack_propagate(False)
        self.pack(side="top", fill="both", expand=True)

        self.__render_view(master)
        # for testing
        # self.show_appointment_reasons(master.main_controller.get_appointment_reasons())
       

    def __render_view(self, master: tk.Tk) -> None:
        # 'Monash Clinic' Header
        tk.Label(self, text="Monash Clinic", font=('Roboto',44), bg = '#67b9e6',width=500).pack()
        tk.Label(self, text = "").pack()

        # 'Start' Date
        tk.Label(self, text = "Start Date", width=18, height=1).pack()
        start_cal = Calendar(self,selectmode = "day", year = 2021, month = 5, day = 22, date_pattern ='yyyy-mm-dd')
        start_cal.pack()
        tk.Label(self, text = "", width=18, height= 2).pack()
    
        # End Date
        tk.Label(self, text = "End Date", width=18, height=1).pack()
        end_cal = Calendar(self,selectmode = "day", year = 2021, month = 5, day = 22, date_pattern ='yyyy-mm-dd')
        end_cal.pack()
        tk.Label(self, text = "", width=18, height= 2).pack()
        
        # Report Type
        report_options = ['Reason','GP','Clinic']
        report_type = tk.StringVar()
        report_type.set(report_options[0])

        tk.Label(self, text = "Report Type", width=18, height=1).pack()
        tk.OptionMenu(self,report_type,*report_options).pack()
        tk.Label(self, text = "").pack()

        tk.Button(self,text="Generate Report",command = lambda: self.display_reason_report(start_cal.get_date(),end_cal.get_date(),report_type.get())).pack()
    
    def display_reason_report(self, start_date, end_date, report_type):
        #Create table
        reason_dict = self.master.main_controller.get_report_statistic(start_date,end_date,report_type)
        reason_table = ttk.Treeview(self,height=5)
        reason_table['columns'] = ("Reason","Occurences")

        reason_table.column("#0",width=0,stretch=NO)
        reason_table.column("Reason",anchor=W, width = 120)
        reason_table.column("Occurences",anchor=E, width=120)

        reason_table.heading("#0", text = '', anchor=W)
        reason_table.heading("Reason", text = 'Reason', anchor=W)
        reason_table.heading("Occurences", text = 'Occurences', anchor=E)
        
        #Add values
        table_iid = 0
        for key,value in reason_dict.items():
            reason_table.insert(parent='',index='end',iid=table_iid,text="",values=(key,value))
            table_iid += 1
        reason_table.pack()
        

    # for testing
    def display_appointment_reasons(self, appointment_reasons):
        for reason in appointment_reasons:
            tk.Label(self, text = reason).pack()