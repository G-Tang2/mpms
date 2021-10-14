import tkinter as tk
from PIL import ImageTk, Image

class HeaderView(tk.Frame):
    def __init__(self, master: tk.Tk):
        tk.Frame.__init__(self, master)
        '''
        Generates the header 
        '''
        # Create image and assign to reference variable
        icon_logout = Image.open("images/icon_logout.png")
        resized = icon_logout.resize((55,50), Image.ANTIALIAS)
        self.logout_image = ImageTk.PhotoImage(resized)

        # Create header frame to contain the header
        self.header_frame = tk.Frame(self,bg='white')
        tk.Button(self.header_frame, text="   Monash Clinic", relief = 'flat',borderwidth= 0, highlightthickness = 0 , font=('Roboto',38, "bold"), anchor="w", bg="white", activebackground="white",
            command = lambda: master.header_controller.return_home()).pack(side = "left", ipady=5)
        self.header_frame.pack(fill = 'x')

        # Black line divider between header and body frame
        tk.Frame(self, bg="black", height=2).pack(side = "bottom", fill="x")

        # logout button
        self.logout_btn = tk.Button(self.header_frame, image = self.logout_image, relief = 'flat', 
            command = lambda: master.header_controller.logout(),borderwidth= 0, highlightthickness = 0, anchor="w", bg="#99d2f2")
    
    def display_logout_btn(self):
        '''
        Display the logout button from view
        '''
        self.logout_btn.pack(fill = 'x',side = "right", ipady=5, padx = 10) 
    
    def hide_logout_btn(self):
        '''
        Hides the logout button from view
        '''
        self.logout_btn.pack_forget()

    def return_confirmation(self):
        '''
        Asks confirmation when returning to home page or logging out
        '''
        confirmation = tk.messagebox.askyesno(title='Confirmation', message='Leave and Discard Changes?')
        return confirmation
