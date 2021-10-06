
from typing import List
from models.gp import GP

class GPList():
    def __init__(self, gps: List[GP]) -> None:
        self.gps = gps

    def get_gps(self) -> List[GP]:
        return self.gps

    @staticmethod
    def create_from_json(json_info):
        gp_list = []
        for gp_json in json_info["gps"]:
            gp_list.append(GP.create_from_json(gp_json))
        return GPList(gp_list)