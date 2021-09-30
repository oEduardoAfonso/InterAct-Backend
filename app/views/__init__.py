from app import app
from marshmallow import ValidationError
from flask import make_response, jsonify

@app.errorhandler(ValidationError)
def handle_validation_error(error):
    return make_response(jsonify(error.messages), 400)