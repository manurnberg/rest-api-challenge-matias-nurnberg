from serializers.DTOs.characterDTO import CharacterDTO
from serializers.DTOs.new_characterDTO import NewCharacterDTO
from serializers.DTOs.charactersDTO import CharactersDTO
from externals.database.models.character import Character
from externals.database.models.character import db

#repository implementation for SQLAlchemy ORM 
class Repository:

    @staticmethod
    def get_all():
        try:
            characters = Character.query.all()
            serialized_characters = []
            for character in characters:
                serialized_character = CharactersDTO(
                    id=character.id,
                    name=character.name,
                    height=character.height,
                    mass=character.mass,
                    birth_year=character.birth_year,
                    eye_color=character.eye_color
                ).to_dict()
                serialized_characters.append(serialized_character)
            return serialized_characters
        except Exception as e:
            raise RuntimeError(f"Error al obtener todos los personajes: {e}")


    @staticmethod
    def get_by_id(id):
        try:
            character = Character.query.get(id)
            if character:
                character_dto = CharacterDTO(
                    id=character.id,
                    name=character.name,
                    height=character.height,
                    mass=character.mass,
                    birth_year=character.birth_year,
                    eye_color=character.eye_color,
                    hair_color=character.hair_color,
                    skin_color=character.skin_color,
                )
                return character_dto.to_dict()
            else:
                return None
        except Exception as e:
            raise RuntimeError(f"Error al obtener el personaje con ID {id}: {e}")


    @staticmethod
    def add(data):
        new_character_dto = NewCharacterDTO.from_dict(data)
        try:
            new_character = Character(
                name=new_character_dto.name,
                height=new_character_dto.height,
                mass=new_character_dto.mass,
                hair_color=new_character_dto.hair_color,
                skin_color=new_character_dto.skin_color,
                eye_color=new_character_dto.eye_color,
                birth_year=new_character_dto.birth_year
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


