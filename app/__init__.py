from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
marshm = Marshmallow()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    marshm.init_app(app)

    from app.stations.routes import stations

    app.register_blueprint(stations)

    return app