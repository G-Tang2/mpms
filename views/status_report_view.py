import tkinter as tk
from tkinter import Toplevel, ttk
from tkinter.constants import E, NO, W
from tkcalendar import *

from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class StatusReportView(tk.Frame):
    def __init__(self, master: tk.Tk) -> None:
        # Initialise frame and set controller
        tk.Frame.__init__(self, master)
        self.pack_propagate(False)
        self.pack(side="top", fill="both", expand=True)
        self.__render_view(master)
        self.reason_table = None
       

    def __render_view(self, master: tk.Tk) -> None:
        # 'Monash Clinic' Header
        tk.Label(self, text="Monash Clinic", font=('Roboto',44), bg = '#67b9e6',width=500).pack()
        tk.Label(self, text = "").pack()

        # 'Start' Date
        tk.Label(self, text = "Start Date", width=18, height=1).pack()
        start_cal = Calendar(self,selectmode = "day", year = 2021, month = 5, day = 22, date_pattern ='yyyy-mm-dd', selectforeground ='#67b9e6')
        start_cal.pack()
        tk.Label(self, text = "", width=18, height= 2).pack()
    
        # End Date
        tk.Label(self, text = "End Date", width=18, height=1).pack()
        end_cal = Calendar(self,selectmode = "day", year = 2021, month = 5, day = 22, date_pattern ='yyyy-mm-dd', selectforeground ='#67b9e6')
        end_cal.pack()
        tk.Label(self, text = "", width=18, height= 2).pack()
        
        # Report Type
        report_options = ['Reason']
        report_type = tk.StringVar()
        report_type.set(report_options[0])

        tk.Label(self, text = "Report Type", width=18, height=1).pack()
        tk.OptionMenu(self,report_type,*report_options).pack()
        tk.Label(self, text = "").pack()

    

        tk.Button(self,text="Generate Report",command = lambda: self.display_reason_report(start_cal.get_date(),end_cal.get_date(),report_type.get())).pack()
    
    def display_reason_report(self, start_date, end_date, report_type):
        
        reason_dict = self.master.main_controller.get_report_statistic(start_date,end_date,report_type)

        report = Toplevel(self)
        report.title("Reason Report")
        report.geometry("700x700")
        
        tk.Label(report,text = "Reason Pie Chart").pack()
        f = Figure(figsize=(5,4), dpi= 100)
        a = f.add_subplot(111)
        labels = reason_dict.keys()
        sizes = reason_dict.values()
        a.pie(sizes, labels = labels)
        canvas = FigureCanvasTkAgg(f,report)
        canvas.get_tk_widget().pack(fill=tk.BOTH)
        
        
        #Create table
        if self.reason_table is not None:
            self.reason_table.destroy()
        
        # Add reason table
        self.reason_table = ttk.Treeview(report, height = len(reason_dict))
        self.reason_table['columns'] = ("Reason","Occurences")

        self.reason_table.column("#0",width=0,stretch=NO)
        self.reason_table.column("Reason",anchor=W, width = 120)
        self.reason_table.column("Occurences",anchor=E, width=120)

        self.reason_table.heading("#0", text = '', anchor=W)
        self.reason_table.heading("Reason", text = 'Reason', anchor=W)
        self.reason_table.heading("Occurences", text = 'Occurence Percentage (%)', anchor=E)
    
        table_iid = 0
        for key,value in reason_dict.items():
            self.reason_table.insert(parent='',index='end',iid=table_iid,text="",values=(key,round(value,2)))
            table_iid += 1
        self.reason_table.pack(fill=tk.BOTH)