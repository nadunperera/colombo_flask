from flask_restplus import Resource
from service.users.restplus import api
from service.models import user_model

ns = api.namespace('service/users', description='Operations related to users')

all_users = [
    {
        "first_name": "Jesus",
        "last_name": "Perera",
        "email": "nadun.perera@me.com",
    },
    {
        "first_name": "Prerana",
        "last_name": "Damn",
        "email": "prerana.magar@me.com",
    }
]

@ns.route('/')
class UserList(Resource):
    #GET a list of all Users and POST to add new User
    @api.marshal_with(user_model)
    def get(self):
        #List all Users
        return all_users