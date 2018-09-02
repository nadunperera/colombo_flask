from datetime import datetime
from flask_restplus import fields, Model

user_model = Model('User Model', {
    'first_name': fields.String(required=True, description='First Name of the User'),
    'last_name': fields.String(required=True, description='Last Name of the User'),
    'email': fields.String(required=True, description='Email of the User')
})