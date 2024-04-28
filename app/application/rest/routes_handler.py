from flask import jsonify, request, Blueprint
import json

from domain.entities.character import Character
from externals.repository.repository import Repository
from serializers.DTOs.characterDTO import CharacterDTO
from serializers.DTOs.charactersDTO import CharactersDTO
from serializers.DTOs.new_characterDTO import NewCharacterDTO
from domain.use_cases.use_cases import UseCases


blueprint = Blueprint('blueprint', __name__)
repository = Repository
use_case = UseCases(repository)



## sever status route health check
@blueprint.route('/', methods=['GET'])
def server_status():
    return jsonify({"response": "server running"}), 200

## get all characters route
@blueprint.route('/characters', methods=['GET'])
def get_characters():
    try:
        characters = use_case.get_all()
        if characters:
            serialized_characters = [CharactersDTO(
                id=character.id,
                name=character.name,
                height=character.height,
                mass=character.mass,
                birth_year=character.birth_year,
                eye_color=character.eye_color
            ).to_dict() for character in characters]
            return jsonify(serialized_characters), 200
        else:
            return jsonify({'message': 'No characters stored'}), 404
    except Exception as e:
        return jsonify({'message': f'Error retrieving characters: {e}'}), 500

## get character by id route
@blueprint.route('/characters/<int:id>', methods=['GET'])
def get_character(id) -> CharacterDTO:
    try:
        character = use_case.get_by_id(id)
        
        if character:
            character = Character.to_dict(character)
            character_dto = CharacterDTO.from_dict(character)
            return jsonify(character_dto.to_dict()), 200
        else:
            return jsonify({'message': 'Character not found'}), 404
    except Exception as e:
        return jsonify({'message': f'Error retrieving character: {e}'}), 500

## add new character route
@blueprint.route('/characters', methods=['POST'])
def add_character():
    try:
        data = request.json
        new_character_dto = NewCharacterDTO.from_dict(data)
        new_character_dto = new_character_dto.to_dict()
        db_character = use_case.get_by_attribute(new_character_dto['name'])
        if db_character:
            return jsonify({'message': 'Character already exists'}), 400
        else:     
            new_character = Character.to_dict(use_case.add(new_character_dto))
            serialized_character = CharacterDTO.from_dict(new_character)
            return jsonify(serialized_character.to_dict()), 201
    except Exception as e:
        return jsonify({'message': f'Error creating character: {e}'}), 500

## delete a character by id route
@blueprint.route('/characters/<int:id>', methods=['DELETE'])
def delete_character(id):
    try:
        result = use_case.delete(id)
        if result:
            return jsonify({'message': 'Character deleted'}), 200
    except Exception as e:
        return jsonify({'message': f'Error deleting character: {e}'}), 500
