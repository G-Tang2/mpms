import tkinter as tk


class AppointmentView(tk.Frame):
    def __init__(self, master: tk.Tk, controller) -> None:
        # initialise frame and set controller
        tk.Frame.__init__(self, master, bg="#c1e4f7")
        self.controller = controller
        self._render_view(master)

    def _render_view(self, master: tk.Tk) -> None:

        outer_frame = tk.Frame(self, relief="solid", borderwidth=2, bg="white")
        inner_frame = tk.Frame(outer_frame, relief="flat", bg="white")
        outer_frame.pack(padx=350, pady=50, fill="x")
        inner_frame.pack(padx=50, fill="x")

        list_of_branches = self.controller.sort_branches()

        # label to ask selecting a clinic
        tk.Label(inner_frame, text='Please select a branch').pack()
        listbox = tk.Listbox(inner_frame)
        for branch in list_of_branches:
            listbox.insert('end', branch)
        listbox.pack()
        tk.Button(inner_frame, text='Show Info', width=15, height=2, command=lambda: self.show_info(listbox)).pack()
        tk.Button(inner_frame, text='next', width=15, height=2,
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

    def show_branch_info(self, branch):
        tk.messagebox.showinfo(title='branch info', message=branch.get_info())
