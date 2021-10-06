import tkinter as tk

class Header(tk.Frame):
    def __init__(self, master: tk.Tk):
        # header
        tk.Label(master, text="   Monash Clinic", font=('Roboto',38, "bold"), anchor="w", bg="white").pack(ipady=10, fill="x")
        
        # divider
        tk.Frame(master, bg="black", height=2).pack(fill="x")