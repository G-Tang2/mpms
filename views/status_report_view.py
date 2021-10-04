import tkinter as tk
from tkinter import Toplevel, ttk
from tkinter.constants import E, NO, W
from tkcalendar import *

from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class StatusReportView(tk.Frame):
    def __init__(self, master: tk.Tk, controller) -> None:
        # Initialise frame and set controller
        tk.Frame.__init__(self, master, bg="#c1e4f7")
        self.pack_propagate(False)
        self.pack(side="top", fill="both", expand=True)
        self.controller = controller
        self.__render_view(master)
       

    def __render_view(self, master: tk.Tk) -> None:
        # 'Monash Clinic' Header
        tk.Label(self, text="   Monash Clinic", font=('Roboto',38, "bold"), anchor="w", bg="white").pack(ipady=10, fill="x")
        
        # divider
        tk.Frame(self, bg="black", height=2).pack(fill="x")

        # container for login details
        outer_label_frame = tk.LabelFrame(self, relief="solid", borderwidth=2, bg="white")

        inner_label_frame = tk.LabelFrame(outer_label_frame, relief="flat", bg="white")

        # 'Start' Date
        tk.Label(inner_label_frame, text = "Start Date", width=18, height=1).pack()
        start_cal = Calendar(inner_label_frame,selectmode = "day", year = 2021, month = 5, day = 22, date_pattern ='yyyy-mm-dd', selectforeground ='#67b9e6')
        start_cal.pack()
        tk.Label(inner_label_frame, text = "", width=18, height= 2).pack()
    
        # End Date
        tk.Label(inner_label_frame, text = "End Date", width=18, height=1).pack()
        end_cal = Calendar(inner_label_frame,selectmode = "day", year = 2021, month = 5, day = 22, date_pattern ='yyyy-mm-dd', selectforeground ='#67b9e6')
        end_cal.pack()
        tk.Label(inner_label_frame, text = "", width=18, height= 2).pack()
        
        # Report Type
        report_options = ['Reason']
        report_type = tk.StringVar()
        report_type.set(report_options[0])

        tk.Label(inner_label_frame, text = "Report Type", width=18, height=1).pack()
        tk.OptionMenu(inner_label_frame,report_type,*report_options).pack()
        tk.Label(inner_label_frame, text = "").pack()

        tk.Button(inner_label_frame,text="Generate Report",command = lambda: self.display_reason_report(start_cal.get_date(),end_cal.get_date(),report_type.get())).pack()
    
        inner_label_frame.pack(padx=50, fill="x")
        outer_label_frame.pack(padx=350, pady=50, fill="x")

    def display_reason_report(self, start_date, end_date, report_type):
        
        if start_date >= end_date:
            tk.messagebox.showerror("Error", "Start date should be earlier than end date")
            return None
        
        reason_dict = self.controller.get_report_statistic(start_date,end_date,report_type)

        if len(reason_dict) == 0:
            tk.messagebox.showerror("Error", "No appointments within this period")
            return

        report = Toplevel(self)
        report.title("Reason Report")
        report.geometry("500x500")

        tk.Label(report,text = "Reason Pie Chart").pack()
        f = Figure(figsize=(5,4), dpi= 100)
        a = f.add_subplot(111)
        labels = reason_dict.keys()
        sizes = reason_dict.values()
        a.pie(sizes, labels = labels)
        canvas = FigureCanvasTkAgg(f,report)
        canvas.get_tk_widget().pack(fill=tk.BOTH)
        
        # Add reason table
        reason_table = ttk.Treeview(report, height = len(reason_dict))
        reason_table['columns'] = ("Reason","Occurences")

        reason_table.column("#0",width=0,stretch=NO)
        reason_table.column("Reason",anchor=W, width = 120)
        reason_table.column("Occurences",anchor=E, width=120)

        reason_table.heading("#0", text = '', anchor=W)
        reason_table.heading("Reason", text = 'Reason', anchor=W)
        reason_table.heading("Occurences", text = 'Occurence Percentage (%)', anchor=E)
    
        table_iid = 0
        for key,value in reason_dict.items():
            reason_table.insert(parent='',index='end',iid=table_iid,text="",values=(key,round(value,2)))
            table_iid += 1
        reason_table.pack(fill=tk.BOTH)