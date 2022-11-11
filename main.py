import os

from flask import Flask
from marshmallow.validate import ValidationError
from sqlalchemy.exc import DataError

from init import db, ma, bcrypt, jwt
from controllers.teams import teams_bp
from controllers.users import users_bp
from controllers.auth import auth_bp
from controllers.matches import matches_bp
from controllers.team_matches import team_match_bp
from controllers.cli_commands import db_commands

def create_app():
    app = Flask(__name__)

    @app.errorhandler(400)
    def bad_request(err):
        return {'error': str(err)}, 400

    @app.errorhandler(401)
    def unauthorized(err):
        return {'error': str(err)}, 401

    @app.errorhandler(404)
    def not_found(err):
        return {'error': str(err)}, 404

    @app.errorhandler(KeyError)
    def key_error(err):
        return {'error': f'The field {err} is required.'}, 400

    @app.errorhandler(ValidationError)
    def validation_error(err):
        return {'error': err.messages}, 400

    # @app.errorhandler(DataError)
    # def data_error():
    #     return {'error': 'Wrong data type entered.'}, 400

    app.config['JSON_SORT_KEYS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
    app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY')

    db.init_app(app)
    ma.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    app.register_blueprint(teams_bp)
    app.register_blueprint(users_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(matches_bp)
    app.register_blueprint(team_match_bp)
    app.register_blueprint(db_commands)

    return app
