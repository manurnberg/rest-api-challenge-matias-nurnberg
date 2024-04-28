
## Character validation DTO for all character properties

class CharacterDTO:
    def __init__(self, id, name, height, mass, birth_year, eye_color, hair_color, skin_color):
        self.id = id
        self.name = name
        self.height = height
        self.mass = mass
        self.birth_year = birth_year
        self.eye_color = eye_color
        self.hair_color = hair_color
        self.skin_color = skin_color

    @classmethod
    def from_dict(cls, data):
        required_fields = {'id', 'name', 'height', 'mass', 'birth_year', 'eye_color', 'hair_color', 'skin_color'}
        if not all(field in data for field in required_fields):
            raise ValueError("Missing required fields in character data")
        if len(data) != len(required_fields):
            raise ValueError("Character data contains extra fields")
        return cls(**data)
    

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'height': self.height,
            'mass': self.mass,
            'birth_year': self.birth_year,
            'eye_color': self.eye_color,
            'hair_color': self.hair_color,
            'skin_color': self.skin_color,
        }
