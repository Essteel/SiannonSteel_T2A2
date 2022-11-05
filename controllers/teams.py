from init import db
from models.team import Team, TeamSchema

from flask import Blueprint, request
from flask_jwt_extended import jwt_required

teams_bp = Blueprint('teams', __name__, url_prefix='/teams')

# CREATE
@teams_bp.route('/', methods=['POST'])
@jwt_required
def create_team():
    # authorize()
    team = Team(
        name = request.json['name']
    )
    db.session.add(team)
    db.session.commit()

# READ
@teams_bp.route('/')
def get_all_teams():
    stmt = db.select(Team).order_by(Team.name)
    teams = db.session.scalars(stmt)
    return TeamSchema(many=True).dump(teams)

@teams_bp.route('/<int:id')
def get_one_team():
    stmt = db.select(Team).filter_by(id=id)
    team = db.session.scalar(stmt)
    if team:
        return TeamSchema().dump(team)
    else:
        return {'error': f'The team you requested with id {id} cannot be found.'}, 404

# UPDATE
@teams_bp.route('/<int:id>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_one_team(id):
    # authorize()
    stmt = db.select(Team).filter_by(id=id)
    team = db.session.scalar(stmt)
    if team:
        team.name = request.json.get('name') or team.name
        team.total_won = request.json.get('total_won') or team.total_won
        team.total_drawn = request.json.get('total_drawn') or team.total_drawn
        team.total_lost = request.json.get('total_lost') or team.total_lost
        db.session.commit()
        return TeamSchema().dump(team)
    else:
        return {'error': f'The team you requested with id {id} cannot be found.'}, 404

# DELETE
@teams_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required
def delete_one_team(id):
    # authorize()
    stmt = db.select(Team).filter_by(id=id)
    team = db.session.scalar(stmt)
    if team:
        db.session.delete(team)
        db.session.commit()
        return {'message': f'\'{team.name}\' was deleted successfully.'}
    else:
        return {'error': f'The team you requested with id {id} cannot be found.'}, 404
