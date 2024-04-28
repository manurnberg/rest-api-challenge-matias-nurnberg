from externals.database.models.character import Character
from externals.database.models.character import db

#repository implementation for SQLAlchemy ORM 
class Repository:

    @staticmethod
    def get_all():
        try:
            return Character.query.all()
        except Exception as e:
            raise RuntimeError(f"Error al obtener todos los personajes: {e}")

    @staticmethod
    def get_by_id(id):
        try:
            return Character.query.get(id)
        except Exception as e:
            raise RuntimeError(f"Error al obtener el personaje con ID {id}: {e}")

    @staticmethod
    def add(data):
        try:
            new_character = Character(
                name=data['name'],
                height=data['height'],
                mass=data['mass'],
                hair_color=data['hair_color'],
                skin_color=data['skin_color'],
                eye_color=data['eye_color'],
                birth_year=data['birth_year']
            )
            db.session.add(new_character)
            db.session.commit()
            return new_character
        except KeyError as e:
            raise ValueError(f"Campo faltante en los datos: {e}")
        except Exception as e:
            raise RuntimeError(f"Error al agregar el personaje: {e}")

    @staticmethod
    def delete(id):
        try:
            character = Character.query.get(id)
            db.session.delete(character)
            db.session.commit()
            return True
        except Exception as e:
            raise RuntimeError(f"Error al eliminar el personaje con ID {id}: {e}")

    @staticmethod
    def get_by_attribute(attribute):
        try:
            character = Character.query.filter_by(name=attribute).first()
            return character
        except AttributeError:
            return None
        except Exception as e:
            raise RuntimeError(f"Error al obtener el personaje por atributo: {e}")


