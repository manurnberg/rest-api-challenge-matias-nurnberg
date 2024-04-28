FROM python:3.12-alpine

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the contents of the current directory into the container at /app
COPY . .

# Copy the SQLite database into the container
COPY characters.sqlite /app/db_data/characters.sqlite

# Specify the command to run on container start
CMD ["python3", "app/app.py"]
