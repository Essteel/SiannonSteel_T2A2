from init import db
from models.team import Team, TeamSchema

from flask import Blueprint

teams_bp = Blueprint('teams', __name__, url_prefix='/teams')

@teams_bp.route('/')
def get_all_teams():
    stmt = db.select(Team).order_by(Team.team_name)
    teams = db.session.scalars(stmt)
    return TeamSchema(many=True).dump(teams)
