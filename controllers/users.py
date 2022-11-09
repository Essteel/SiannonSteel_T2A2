from flask import Blueprint, request
from flask_jwt_extended import jwt_required

from init import db, bcrypt
from models.user import User, UserSchema
from controllers.auth import authorize

users_bp = Blueprint('users', __name__, url_prefix='/users')

# CREATE
@users_bp.route('/', methods=['POST'])
@jwt_required()
def create_one_user():
    authorize()
    user = User(
        first_name = request.json['first_name'],
        last_name = request.json['last_name'],
        email = request.json['email'],
        password = bcrypt.generate_password_hash(request.json['password']).decode('utf-8')
    )
    db.session.add(user)
    db.session.commit()
    return UserSchema(exclude=['password']).dump(user), 201

# READ
@users_bp.route('/<int:id>')
@jwt_required()
def get_one_user(id):
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
    authorize()
    stmt = db.select(User).order_by(User.id)
    users = db.session.scalars(stmt)
    return UserSchema(exclude=['password'], many=True).dump(users)

# UPDATE
@users_bp.route('/<int:id>/', methods=['PUT', 'PATCH'])
@jwt_required()
def update_one_user(id):
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
    authorize()
    stmt = db.select(User).filter_by(id=id)
    user = db.session.scalar(stmt)
    if user:
        db.session.delete(user)
        db.session.commit()
        return {'message': f'User {user.first_name} {user.last_name} deleted successfully.'}
    else:
        return {'error': f'User not found with id {id}'}, 404
