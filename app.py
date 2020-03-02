from flask_migrate import Migrate
from api import app
from api.models import db

migrate = Migrate(app, db)
