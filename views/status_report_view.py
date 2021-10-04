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
        tk.Frame.__init__(self, master, bg="#c1e4f7")
        self.pack_propagate(False)
        self.pack(side="top", fill="both", expand=True)
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

        tk.Button(inner_label_frame,text="Generate Report",command = lambda: master.main_controller.display_reason_report(start_cal.get_date(),end_cal.get_date(),report_type.get())).pack()
    
        inner_label_frame.pack(padx=50, fill="x")
        outer_label_frame.pack(padx=350, pady=50, fill="x")

    