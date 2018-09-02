from flask import Flask
from service.config import Config
from service.users.routes import users_blueprint
from werkzeug.contrib.fixers import ProxyFix


def create_app(config_class=Config):
    app = Flask(__name__)
    app.wsgi_app = ProxyFix(app.wsgi_app)
    app.config.from_object(Config)

    app.register_blueprint(users_blueprint, url_prefix='/api/v1')

    return app