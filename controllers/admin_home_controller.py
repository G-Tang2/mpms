import tkinter as tk
from controllers.controller import Controller
from views.admin_home_view import AdminHomeView

class AdminHomeController(Controller):
    def __init__(self,master,view = AdminHomeView):
        Controller.__init__(self,master,view)