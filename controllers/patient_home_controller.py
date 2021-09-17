from views.view_home import PatientHomeView

class PatientHomeController():
    def __init__(self, master):
        # master is an tk instance
        self.__set_controller(master)
        self.__load_view(master)

    def __set_controller(self, master):
        # set controller in tk instance
        master.main_controller = self

    def __load_view(self, master):
        # create new view
        new_frame = PatientHomeView(master)
        # remove frame if tk instance has a frame
        if master.main_frame is not None:
            master.main_frame.destroy()
        # assign new frame to tk instance
        master.main_frame = new_frame
        master.main_frame.grid_propagate(False)
        master.main_frame.pack(side="top", fill="both", expand=True)