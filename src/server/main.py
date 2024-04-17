import os

from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv

from .blueprints.upload import bp

load_dotenv()

_debug = True if os.environ.get("FLASK_DEBUG") else False
_host = os.environ.get("FLASK_HOST")

assert _host, "FLASK_HOST must be set in the .env file"

app = Flask(__name__)
CORS(app)

app.register_blueprint(bp)

app.run(host=_host, debug=_debug)
