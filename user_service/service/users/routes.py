from flask import Blueprint

users = Blueprint('users', __name__)

@users.route('/api/v1/users', methods=['GET'])
def register():
    return 'Hello World!'
