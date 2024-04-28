import os
from application.server import create_server
from externals.database.models.character import db
from application.rest.routes_handler import blueprint

app = create_server()

# App context config
app.app_context().push()
current_dir = os.path.abspath(os.path.dirname(__file__))

db_path = os.path.join(current_dir, '..', 'characters.sqlite')

# Database creation and schema creation
if os.path.exists(db_path):
    os.remove(db_path)

app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:////{db_path}'

db.init_app(app)
db.create_all()

# Configura el middleware con el manejador de endpoints
app.register_blueprint(blueprint)

# run server
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=4000, debug=True)
