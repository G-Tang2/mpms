import tkinter as tk


class BookView(tk.Frame):
    def __init__(self, master: tk.Tk) -> None:
        # initialise frame and set controller
        tk.Frame.__init__(self, master)
        self.pack_propagate(False)
        self.pack(side="top", fill="both", expand=True)

    def _render_view(self, master: tk.Tk, list_of_branches) -> None:

        # page content
        tk.Label(self, text='Monash Clinic', width=800, height=2, bg='lightskyblue').pack()
        # show list of branches
        tk.Button(self, text='next', width=15, height=2,
                  command=lambda: master.main_controller.next()).pack()

