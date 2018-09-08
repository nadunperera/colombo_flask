from flask import Flask, Blueprint
from service.users.restplus import api
from service.users.routes import ns as user_namespace
import settings

flask_app = Flask(__name__)

def configure_app(flask_app):
    flask_app.config['SERVER_NAME'] = settings.FLASK_SERVER_NAME
    flask_app.config['SWAGGER_UI_DOC_EXPANSION'] = settings.RESTPLUS_SWAGGER_UI_DOC_EXPANSION
    flask_app.config['RESTPLUS_VALIDATE'] = settings.RESTPLUS_VALIDATE
    flask_app.config['RESTPLUS_MASK_SWAGGER'] = settings.RESTPLUS_MASK_SWAGGER
    flask_app.config['ERROR_404_HELP'] = settings.RESTPLUS_ERROR_404_HELP

def initialize_app(flask_app):
    #configure_app(app)
    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api.init_app(blueprint)
    api.namespaces.pop(0) #this is to remove default namespace from swagger doc
    api.add_namespace(user_namespace)
    flask_app.register_blueprint(blueprint)

def main():
    initialize_app(flask_app)
    flask_app.run(debug=settings.FLASK_DEBUG)


if __name__ == "__main__":
    main()