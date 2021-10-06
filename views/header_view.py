import tkinter as tk

class Header(tk.Frame):
    def __init__(self, master: tk.Tk):
        tk.Frame.__init__(self, master)
        # header
        tk.Label(self, text="   Monash Clinic", font=('Roboto',38, "bold"), anchor="w", bg="white").pack(ipady=10, fill="x")      
        # divider
        tk.Frame(self, bg="black", height=2).pack(fill="x")