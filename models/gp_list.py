
from models.gp import GP

class GPList():
    def __init__(self, json):
        self.gps = self.__get_gps(json)
    
    def __get_gps(self, json):
        gp_list = []
        for gp in json["gps"]:
            gp_list.append(GP(gp))
        return gp_list

    def get_gps(self):
        return self.gps