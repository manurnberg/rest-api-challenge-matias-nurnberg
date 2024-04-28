
## New character data validation DTO for character creation, no id data validation before db storage

class NewCharacterDTO:
    def __init__(self, name, height, mass, birth_year, eye_color, hair_color, skin_color):
        self.name = name
        self.height = height
        self.mass = mass
        self.birth_year = birth_year
        self.eye_color = eye_color
        self.hair_color = hair_color
        self.skin_color = skin_color

    @classmethod
    def from_dict(cls, data):
        required_fields = {'name', 'height', 'mass', 'birth_year', 'eye_color', 'hair_color', 'skin_color'}
        if not all(field in data for field in required_fields):
            raise ValueError("Missing required fields in character data")
        if len(data) != len(required_fields):
            raise ValueError("Character data contains extra fields")
        return cls(**data)
    

    def to_dict(self):
        return {
            'name': self.name,
            'height': self.height,
            'mass': self.mass,
            'birth_year': self.birth_year,
            'eye_color': self.eye_color,
            'hair_color': self.hair_color,
            'skin_color': self.skin_color,
        }