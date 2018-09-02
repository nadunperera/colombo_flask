from flask import Blueprint
from flask_restplus import Api, Resource
from service.models import user_model

users_blueprint  = Blueprint('users', __name__)
users_api = Api(users_blueprint, version='1.0', title='Colombo Users API', description='An API for Colombo User Service')

all_users = [
    {
        "first_name": "Nadun",
        "last_name": "Perera",
        "email": "nadun.perera@me.com",
    },
    {
        "first_name": "Prerana",
        "last_name": "Thapa",
        "email": "prerana.magar@me.com",
    }
]

@users_api.route('/users', methods=['GET'])
class UserList(Resource):
    #GET a list of all Users and POST to add new User
    @users_api.marshal_list_with(user_model)
    def get(self):
        #List all Users
        return all_users