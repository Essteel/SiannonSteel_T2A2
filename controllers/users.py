""" CRUD functionality for users data

Functions for viewing, creating, editing and deleting
users data.

Functions
---------
create_one_user()
get_one_user()
get_all_users()
update_one_user()
delete_one_user()
"""

from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from sqlalchemy.exc import IntegrityError

from init import db, bcrypt
from models.user import User, UserSchema
from controllers.auth import authorize

users_bp = Blueprint('users', __name__, url_prefix='/users')

# CREATE
@users_bp.route('/', methods=['POST'])
def create_one_user():
    """ Creation of one user

    User attributes provided in json format. New user added and
    committed to database. An IntegrityError is raised if the user
    attempt to use an email address already associated with another
    user.

    Returns:
        json: If the user creation is successful, all attributes
        of the user will be returned.
    """
    try:
        user = User(
            first_name = request.json['first_name'],
            last_name = request.json['last_name'],
            email = request.json['email'],
            password = bcrypt.generate_password_hash(request.json['password']).decode('utf-8')
        )
        db.session.add(user)
        db.session.commit()
        return UserSchema(exclude=['password']).dump(user), 201
    except IntegrityError:
        return {'error': 'That email address is already in use'}, 409

# READ
@users_bp.route('/<int:id>/')
@jwt_required()
def get_one_user(id):
    """ Selects one user by its 'id' attribute

    Args:
        id (int): primary key and unique identifier for
        the user.

    Returns:
        json: If the id exists, attributes for the user
        are returned as a json dictionary.

        json: If the id does not exist then an error message and
        a 401 HTTP status code are returned as a json dictionary.
    """
    authorize()
    stmt = db.select(User).filter_by(id=id)
    user = db.session.scalar(stmt)
    if user:
        return UserSchema(exclude=['password']).dump(user)
    else:
        return {'error': f'The user you requested with id {id} cannot be found.'}, 404

@users_bp.route('/')
@jwt_required()
def get_all_users():
    """ Selects all users ordered by id

    Returns:
        json: A list of user dictionaries ordered
        by the id attribute.
    """
    authorize()
    stmt = db.select(User).order_by(User.id)
    users = db.session.scalars(stmt)
    return UserSchema(exclude=['password'], many=True).dump(users)

# UPDATE
@users_bp.route('/<int:id>/', methods=['PUT', 'PATCH'])
@jwt_required()
def update_one_user(id):
    """ Edits one user

    Checks if the current user is logged in and has
    administrative rights. If successful, user selected by
    its 'id' attribute, new values are provided in json format
    and the changes are committed to the database.

    Args:
        id (int): primary key and unique identifier for
        the user.

    Returns:
        json: If the id exists, all attributes for the team
        are returned as a json dictionary.

        json: If the id does not exist then an error message and
        a 404 HTTP status code are returned as a json dictionary.
    """
    authorize()
    stmt = db.select(User).filter_by(id=id)
    user = db.session.scalar(stmt)
    if user:
        user.first_name = request.json.get('first_name') or user.first_name
        user.last_name = request.json.get('last_name') or user.last_name
        user.email = request.json.get('email') or user.email
        user.bio = request.json.get('bio') or user.bio
        user.country = request.json.get('country') or user.country
        user.is_admin = request.json.get('is_admin') or user.is_admin

        user.team_id = request.json.get('team_id') or user.team_id
        db.session.commit()
        return UserSchema(exclude=['password']).dump(user)
    else:
        return {'error': f'User not found with id {id}'}, 404

# DELETE
@users_bp.route('/<int:id>/', methods=['DELETE'])
@jwt_required()
def delete_one_user(id):
    """ Deletes a user from the database

    Checks if the current user is logged in and has administrative
    rights. If successful, selects user by id, deletes the user
    and commits the change to the database.

    Args:
        id (int): primary key and unique identifier for
        the user.

    Returns:
        json: If the id exists, a message is returned confirming
        deletion of the user as a json dictionary.

        json: If the id does not exist, a message is returned
        and a 404 HTTP status code as a json dictionary.
    """
    authorize()
    stmt = db.select(User).filter_by(id=id)
    user = db.session.scalar(stmt)
    if user:
        db.session.delete(user)
        db.session.commit()
        return {'message': f'User {user.first_name} {user.last_name} deleted successfully.'}
    else:
        return {'error': f'User not found with id {id}'}, 404
