import tkinter as tk


class BookView(tk.Frame):
    def __init__(self, master: tk.Tk, controller) -> None:
        # initialise frame and set controller
        tk.Frame.__init__(self, master)
        self.controller = controller

    def render_view(self, master: tk.Tk, list_of_branches) -> None:

        # label to ask selecting a clinic
        tk.Label(self, text='Please select a branch').pack()
        listbox = tk.Listbox(self)
        for branch in list_of_branches:
            listbox.insert('end', branch)
        listbox.pack()
        tk.Button(self, text='Show Info', width=15, height=2, command=lambda: self.show_info(listbox)).pack()
        tk.Button(self, text='next', width=15, height=2,
                  command=lambda: self.next(master, listbox)).pack()

    def next(self, master: tk.Tk, listbox):
        if listbox.curselection():
            value = listbox.get('active')
            self.controller.display_gp_view(master, value)
        else:
            tk.messagebox.showerror(title='no branch', message='please select a branch')

    def show_info(self, listbox):
        if listbox.curselection():
            value = listbox.get('active')
            self.controller.show_info(value)
        else:
            tk.messagebox.showerror(title='no branch', message='please select a branch')
