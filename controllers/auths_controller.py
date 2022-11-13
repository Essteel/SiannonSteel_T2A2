""" Authorization for logging in and administrative operations

This module allows players to login, creating a bearer token if their
credentials are valid. It also contains the authorize function which
checks if the logged in user has administrative rights.

Functions
---------
login()
authorize()
"""

from datetime import timedelta

from flask import Blueprint, request, abort
from flask_jwt_extended import create_access_token, get_jwt_identity

from init import db, bcrypt
from models.user import User

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/login/', methods=['POST'])
def login():
    """ Creates a bearer token for the user if their credentials are valid

    Selects the user by their email address. If the user is valid the
    password is checked. If the email and password match then a token
    is created which identifies the user by their id. The token is valid
    for one hour, after which the user will have to log in again.

    Returns:
        json: If the user credentials are valid then the user email, token
        and admin status are returned.
        
        json: If the user credentials are invalid then an error message and
        a 401 HTTP status code are returned.
    """    
    stmt = db.select(User).filter_by(email=request.json['email'])
    user = db.session.scalar(stmt)
    if user and bcrypt.check_password_hash(user.password, request.json['password']):
        token = create_access_token(identity=str(user.id), expires_delta=timedelta(hours=1))
        return {'email': user.email, 'token': token, 'is_admin': user.is_admin}
    else:
        return {'error': 'Invalid email address or password.'}, 401

def authorize():
    """Checks if the logged in user has administrative rights

    Selects the id of the currently logged in user via their
    token. If the user linked to the token is not an admin,
    (that the Boolean attribute 'is_admin' is False), then the request
    is aborted with a 401 HTTP status code returned.

    """    
    user_id = get_jwt_identity()
    stmt = db.select(User).filter_by(id=user_id)
    user = db.session.scalar(stmt)
    if not user.is_admin:
        abort(401)
