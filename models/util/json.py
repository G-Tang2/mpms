import json

class JSON():
    @staticmethod
    def to_JSON(obj):
        return json.dumps(obj, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)