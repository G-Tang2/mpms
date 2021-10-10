import tkinter as tk

class Controller():
    def __init__(self, master: tk.Tk) -> None:
        self._master = master
        
    def _load_view(self) -> None:
        # remove frame if tk instance has a frame
        if self._master.body_frame is not None:
            self._master.body_frame.destroy()
        # assign new frame to tk instance
        self._master.body_frame = self._view
        self._master.body_frame.grid_propagate(False)
        self._master.body_frame.pack(side="top", fill="both", expand=True)  
