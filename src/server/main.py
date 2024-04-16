from flask import Flask
from flask_cors import CORS

from .blueprints.upload import bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(bp)