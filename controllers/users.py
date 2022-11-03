from init import db
from models.user import User, UserSchema

from flask import Blueprint
from flask_jwt_extended import jwt_required

users_bp = Blueprint('users', __name__, url_prefix='/users')

@users_bp.route('/')
@jwt_required()
def get_all_users():
    # authorize()
    stmt = db.select(User).order_by(User.id)
    users = db.session.scalars(stmt)
    return UserSchema(exclude=['password'], many=True).dump(users)
