from flask import jsonify, request, Blueprint

from domain.entities.character import Character
from externals.repository.repository import Repository
from serializers.DTOs.characterDTO import CharacterDTO
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
            return jsonify(characters), 200
        else:
            return jsonify({'message': 'No characters stored'}), 404
    except Exception as e:
        return jsonify({'message': f'Error retrieving characters: {e}'}), 500


## get character by id route
@blueprint.route('/characters/<int:id>', methods=['GET'])
def get_character(id):
    try:
        character = use_case.get_by_id(id)
        if character:
            return jsonify(character), 200
        else:
            return jsonify({'message': 'Character not found'}), 404
    except Exception as e:
        return jsonify({'message': f'Error retrieving character: {e}'}), 500


## add new character route
@blueprint.route('/characters', methods=['POST'])
def add_character():
    try:
        data = request.json
        db_character = use_case.get_by_attribute(data['name'])
        if db_character:
            return jsonify({'message': 'Character already exists'}), 400
        else:     
            new_character = Character.to_dict(use_case.add(data))
            return jsonify(new_character), 201
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
