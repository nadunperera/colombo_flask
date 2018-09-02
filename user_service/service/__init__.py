from flask import Flask
from service.config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    from service.users.routes import users
    app.register_blueprint(users)

    return app