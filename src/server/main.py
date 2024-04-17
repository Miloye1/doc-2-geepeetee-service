from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv

from .blueprints.upload import bp

load_dotenv()

app = Flask(__name__)
CORS(app)

app.register_blueprint(bp)
