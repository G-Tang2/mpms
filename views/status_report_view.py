from calendar import weekheader
import tkinter as tk
from tkinter import Toplevel, ttk
from tkinter.constants import E, NO, W
from tkcalendar import *
from datetime import date

from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class StatusReportView(tk.Frame):
    def __init__(self, master: tk.Tk, controller) -> None:
        # Initialise frame and set controller
        tk.Frame.__init__(self, master, bg="#c1e4f7")
        self.controller = controller

    def render_view(self) -> None:        
        # Container frames for status report input 
        outer_label_frame = tk.LabelFrame(self, relief="solid", borderwidth=2, bg="white")
        inner_label_frame = tk.LabelFrame(outer_label_frame, relief="flat", bg="white")
        date_label_frame = tk.LabelFrame(inner_label_frame, relief="flat", bg="white")
        
        # 'Start' Date Entry widget
        tk.Label(outer_label_frame, text="Status Report", font=('Roboto',28, "bold"), bg="white").pack(pady=(30, 30))
        start_date_label_frame = tk.LabelFrame(date_label_frame, relief="flat", bg="white")
        tk.Label(start_date_label_frame, text = "Start Date", width=18, height=1, bg="white").pack()
        start_cal = DateEntry(start_date_label_frame, date_pattern='dd/mm/y', selectmode = 'day', showweeknumbers = False)
        start_cal.pack()
        
        # 'End' Date Entry widget
        end_date_label_frame = tk.LabelFrame(date_label_frame, relief="flat", bg="white")
        tk.Label(end_date_label_frame, text = "End Date", width=18, height=1, bg="white").pack()
        end_cal = DateEntry(end_date_label_frame, date_pattern='dd/mm/y', selectmode = 'day', showweeknumbers = False)
        end_cal.pack()

        start_date_label_frame.pack(side="left")
        end_date_label_frame.pack(side="right")
        date_label_frame.pack()
        
        # Report Type Variables 
        report_options = ['Reason']
        report_type = tk.StringVar(value=report_options[0])

        # 'Report Type' Entry Option Menu Widget
        tk.Label(inner_label_frame, text = "Report Type", width=18, height=1, bg="white", pady = 5).pack(pady=(8,0))
        tk.OptionMenu(inner_label_frame,report_type,*report_options).pack()

        # 'Generate Report' Button (Gets input from previous widgets and calls StatusReportController 'get_reason_report' function)
        tk.Button(inner_label_frame,text="Generate Report", height = 4, width = 20,
            command = lambda: self.controller.get_reason_report(start_cal.get(),end_cal.get(),report_type.get())).pack(pady = 40)
    
        inner_label_frame.pack(padx=50, fill="x")
        outer_label_frame.pack(padx=350, pady=50, fill="x")
        

    def display_input_error(self, message):
        '''
        Displays error message about report input depending on controller validation
        '''
        tk.messagebox.showerror("Error", message)
    
    def display_reason_report(self, reason_dict):
        '''
        Creates window for reason report statistics
        '''
        # Create new window for reason report
        report = Toplevel(self)
        report.title("Reason Report")
        report.geometry("700x700")
        tk.Label(report,text = "Reason Pie Chart").pack()

        # Create figure to hold pie-chart
        f = Figure(figsize=(5,4), dpi= 100)
        a = f.add_subplot(111)
        # Generate pie chart using report statistic
        labels = reason_dict.keys()
        sizes = reason_dict.values()
        a.pie(sizes, labels = labels)
        # Add pie-chart to canvas   
        canvas = FigureCanvasTkAgg(f,report)
        canvas.get_tk_widget().pack(fill=tk.BOTH)
    
        # Generate reason table with TreeView widget
        reason_table = ttk.Treeview(report, height = len(reason_dict))
        reason_table['columns'] = ("Reason","Occurences")
        # Generate columns with reason table
        reason_table.column("#0",width=0,stretch=NO)
        reason_table.column("Reason",anchor=W, width = 120)
        reason_table.column("Occurences",anchor=E, width=120)
        # Give headers to reason table
        reason_table.heading("#0", text = '', anchor=W)
        reason_table.heading("Reason", text = 'Reason', anchor=W)
        reason_table.heading("Occurences", text = 'Occurence Percentage (%)', anchor=E)
        # Iterates through reason statistic, adding each reason to the table
        table_iid = 0
        for key,value in reason_dict.items():
            reason_table.insert(parent='',index='end',iid=table_iid,text="",values=(key,round(value,2)))
            table_iid += 1
        reason_table.pack(fill=tk.BOTH)