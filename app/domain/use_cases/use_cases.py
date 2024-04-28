
## UseCase layer before repository implementations

class UseCases:
    def __init__(self, repository):
        self.repository = repository

    def get_all(self):
        try:
            return self.repository.get_all()
        except Exception as e:
            raise RuntimeError(f"Error al obtener todos los elementos: {e}")

    def get_by_id(self, id):
        try:
            return self.repository.get_by_id(id)
        except Exception as e:
            raise RuntimeError(f"Error al obtener el elemento con ID {id}: {e}")

    def add(self, data):
        try:
            return self.repository.add(data)
        except Exception as e:
            raise RuntimeError(f"Error al agregar un elemento: {e}")

    def delete(self, id):
        try:
            return self.repository.delete(id)
        except Exception as e:
            raise RuntimeError("Character not found")

    def get_by_attribute(self, attribute):
        try:
            return self.repository.get_by_attribute(attribute)
        except Exception as e:
            raise RuntimeError(f"Error al obtener elementos por atributo: {e}")
