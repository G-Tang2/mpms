import tkinter as tk


class BranchView(tk.Frame):
    def __init__(self, master: tk.Tk, controller) -> None:
        # initialise frame and set controller
        tk.Frame.__init__(self, master, bg="#c1e4f7")
        self.controller = controller
        self._branch_listbox = None
        self._selected_clinic_index = 0

    def render_view(self, master: tk.Tk, list_of_branches) -> None:
        '''
        decide how the branch view is
        '''

        # background frame
        outer_frame = tk.Frame(self, relief="solid", borderwidth=2, bg="white")
        inner_frame = tk.Frame(outer_frame, relief="flat", bg="white")

        # title label
        tk.Label(outer_frame, text="Branches", font=('Roboto', 28, "bold"), bg="white").pack(pady=(50, 30))

        # selecting a clinic
        tk.Label(outer_frame, text='Please select a branch:', font=('Roboto',12), anchor="w", bg="white").pack(padx=100, pady=10, fill='x')
        listbox = tk.Listbox(outer_frame, font=('Roboto',15))
        for branch in list_of_branches:
            listbox.insert('end', branch)
        listbox.pack(padx=100, fill='x')

        # Buttons
        button_frame = tk.Frame(outer_frame, bg='white')
        button_frame.pack(pady=20)
        tk.Button(button_frame, text='Show Info', font=('Roboto',14), borderwidth=2, relief="solid", bg="#99d2f2", activebackground="#81c8f0",
            command=lambda: self.show_info(listbox)).pack(side='left', ipadx=10, padx=10)
        tk.Button(button_frame, text='Next', font=('Roboto',14), borderwidth=2, relief="solid", bg="#99d2f2", activebackground="#81c8f0",
         command=lambda: self.next(listbox)).pack(side='right',ipadx=10, padx=10)

        # pack the frames
        outer_frame.pack(pady=50, fill='x', ipadx=30, ipady=30)
        inner_frame.pack(padx=150, fill="x")

        # store listbox for data load reference
        self._branch_listbox = listbox

    def reload_values(self):
        '''
        reload branch selection
        '''

        if self._branch_listbox is not None:
            self._branch_listbox.select_set(self._selected_clinic_index)


    def next(self, listbox):
        '''
        check if the listbox is selected, if yes, display the next view, if not, show the message to remind patient
        '''

        if listbox.curselection():
            branch_name = listbox.get('active')
            # save index of selected branch
            self._selected_clinic_index = listbox.curselection()
            self.controller.display_detail_view(branch_name)
        else:
            tk.messagebox.showerror(title='No Branch Selected', message='Please select a branch.')

    def show_info(self, listbox):
        '''
        check if the listbox is selected, if yes, show the information of the selected branch,
        if not, show the message to remind patient
        '''

        if listbox.curselection():
            value = listbox.get('active')
            self.controller.show_info(value)
        else:
            tk.messagebox.showerror(title='No Branch Selected', message='Please select a branch.')

    def show_branch_info(self, branch):
        '''
        show the information of the selected branch
        '''
        tk.messagebox.showinfo(title='Branch Info', message=branch.get_info())
