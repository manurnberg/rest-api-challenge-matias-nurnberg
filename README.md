# API-REST CHALLENGE (Matias Nürnberg)
## PYTHON 3.12 + FLASK 3.0.3 + FLASK-SQLALCHEMY 3.1.1 + SQLITE3
### USING CLEAN ARCHITECTURE

- Download and install Python 3.12 for your OS
- Crete a project directory and move into
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
 `add -d flag, optional if want to run container detached`
