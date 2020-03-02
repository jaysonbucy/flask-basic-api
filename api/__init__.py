import os

from flask import Flask
from flask_cors import CORS

from .models import db


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(os.environ['APP_SETTINGS'])
    CORS(app)

    db.init_app(app)

    from .V1.routes import v1

    app.register_blueprint(v1, url_prefix='/v1/')

    return app


app = create_app()
