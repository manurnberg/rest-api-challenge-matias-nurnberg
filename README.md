# API-REST CHALLENGE (w)
## PYTHON + FLASK + SQLALCHEMY + SQLITE
### USING CLEAN ARCHITECTURE

### RUN SERVER ON LOCAL VIRTUAL ENV - SERVER RUNS ON PORT 4000

- ACTIVATE VIRTUAL ENV: `source venv/bin/activate`
- RUN SERVER: `python3 app/app.py`
 

### RUN SERVER FROM DOCKERFILE - SERVER RUNS ON PORT 4300

- CREATE DOCKER IMAGE : `docker build -t challenge .`
- RUN DOCKER CONTAINER : `docker run -it -p 4300:4000 --name challenge_container challenge`
