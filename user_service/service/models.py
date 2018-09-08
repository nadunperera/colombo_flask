from datetime import datetime
from flask_restplus import fields
from service.users.restplus import api

user_model = api.model('User Model', {
    'first_name': fields.String(required=True, description='First Name of the User'),
    'last_name': fields.String(required=True, description='Last Name of the User'),
    'email': fields.String(required=True, description='Email of the User')
})