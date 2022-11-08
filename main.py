from init import db, ma, bcrypt, jwt
import os
from controllers.teams import teams_bp
from controllers.users import users_bp
from controllers.auth import auth_bp
from controllers.matches import matches_bp
from controllers.team_matches import team_match_bp
from controllers.cli_commands import db_commands

from flask import Flask

def create_app():
    app = Flask(__name__)

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
