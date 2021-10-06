import tkinter as tk


class BookView(tk.Frame):
    def __init__(self, master: tk.Tk, controller) -> None:
        # initialise frame and set controller
        tk.Frame.__init__(self, master)
        self.pack_propagate(False)
        self.pack(side="top", fill="both", expand=True)
        self.controller = controller

    def render_view(self, master: tk.Tk, list_of_branches) -> None:

        # page content
        listbox = tk.Listbox(self)
        for branch in list_of_branches:
            listbox.insert('end', branch.get_name())
        listbox.pack()
        tk.Button(self, text='next', width=15, height=2,
                  command=lambda: self.next(master, listbox)).pack()

    def next(self, master: tk.Tk, listbox):
        if listbox.curselection():
            value = listbox.get('active')
            self.controller.display_gp_view(master, value)
        else:
            tk.messagebox.showerror(title='no branch', message='please select a branch')
