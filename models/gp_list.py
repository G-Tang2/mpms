
from typing import List
from models.gp import GP

class GPList():
    def __init__(self, gps: List[GP]) -> None:
        self.gps = gps

    def get_gps(self) -> List[GP]:
        return self.gps
    
    def get_gp(self, gp_name:str) -> GP:
        for gp in self.gps:
            if gp_name == gp.get_full_name():
                return gp

    @staticmethod
    def create_from_json(json_info):
        gp_list = []
        for gp_json in json_info["gps"]:
            gp_list.append(GP.create_from_json(gp_json))
        return GPList(gp_list)