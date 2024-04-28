import json

class CharacterJsonEncoder(json.JSONEncoder):
    def default(self, o):
        try:
            to_serialize = {
                "id": o.id,
                "name": o.name,
                "height": o.height,
                "mass": o.mass,
                "hair_color": o.hair_color,
                "skin_color": o.skin_color,
                "eye_color": o.eye_color,
                "birth_year": o.birth_year,
            }
            return to_serialize
        except AttributeError:
            return super().default(o)