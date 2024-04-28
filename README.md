# API-REST CHALLENGE (Matias Nürnberg)
## PYTHON 3.12 + FLASK 3.0.3 + FLASK-SQLALCHEMY 3.1.1 + SQLITE3
### USING CLEAN ARCHITECTURE

- Download and install Python 3.12 for your OS
- Create a project directory and move into
- Install virtualenv: `pip install virtualenv`
- Create the virtual env: `python3 -m venv venv`



- BOTH WAYS TO RUN THE SERVER NEEDS TO EXCUTE FROM THE PROJECT ROOT DIRECTORY

### RUN SERVER ON LOCAL VIRTUAL ENV - SERVER RUNS ON PORT 4000

- ACTIVATE VIRTUAL ENV: `source venv/bin/activate (mac/linux) - . venv\scripts\activate (Windows)`
- INSTALL DEPENDENCIES: `pip install -r requirements.txt`
- RUN SERVER: `python3 app/app.py`
 

### RUN SERVER FROM DOCKERFILE - SERVER RUNS ON PORT 4300

- CREATE DOCKER IMAGE : `docker build -t challenge .`
- RUN DOCKER CONTAINER : `docker run -it -p 4300:4000 --name challenge_container challenge`
- add -d flag, optional if want to run container detached

### API REST POSTMAN COLLECTIONS TO TRY ENDPOINTS 
- THE COLLECTIONS ARE JSON OBJECTS THAT CAN BE IMPORTED TO POSTMAN AND ARE STORAGE ON POSTMAN-COLLECTIONS DIRECTORY ON THE ROOT OF THE PROJECT

### ENDPOINTS ON DOCKER
- Server status - GET `http://localhost:4300/`
- Get all Characaters - GET `http://localhost:4300/characters`
- Get a Character by Id  - GET `http://localhost:4300/characters/{id}`
- Add new Character - POST `http://localhost:4300/characters`
- Delete a Character - DELETE `http://localhost:4300/characters/{id}`

- ON LOCAL VENV ONLY CHANGE THE PORT FOR 4000

### PROJECT STRUCTURE
- DIRECTORIES STRUCTURE INSIDE APP DIRECTORY:
- application - contain the server instance and the routes handler
- domain - contain the entities and the use cases
- externals - contain the db model and the repository 
- serializers - contain the DTOs 



