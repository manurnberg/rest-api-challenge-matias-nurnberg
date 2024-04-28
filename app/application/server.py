from flask import Flask, jsonify

## create server instance instance
def create_server():
    app = Flask(__name__)
    return app