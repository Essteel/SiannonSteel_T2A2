from init import db
from models.team_match import TeamMatch, TeamMatchSchema
from controllers.auth import authorize

from flask import Blueprint, request
from flask_jwt_extended import jwt_required

team_matches_bp = Blueprint('team_matches', __name__, url_prefix='/team_matches')

# CREATE
@team_matches_bp.route('/', methods=['POST'])
@jwt_required
def create_one_team_match():
    authorize()
    team_match = TeamMatch(
        score = request.json['score'],
        team_id = request.json['team_id'],
        match_id = request.json['match_id']
    )
    db.session.add(team_match)
    db.session.commit()
    return TeamMatchSchema().dump(team_match), 201

# READ
@team_matches_bp.route('/<int:id>/')
def get_one_team_match(id):
    stmt = db.select(TeamMatch).filter_by(id=id)
    team_match = db.session.scalar(stmt)
    if team_match:
        return TeamMatchSchema().dump(team_match)
    else:
        return {'error': f'The team match you requested with id {id} cannot be found.'}, 404

@team_matches_bp.route('/')
def get_all_team_matches(id):
    stmt = db.select(TeamMatch).order_by(TeamMatch.match_id)
    team_matches = db.session.scalars(stmt)
    return TeamMatchSchema(many=True).dump(team_matches)

# UPDATE
@team_matches_bp.route('/<int:id>/', methods=['PUT', 'PATCH'])
@jwt_required
def update_one_team_match(id):
    authorize()
    stmt = db.select(TeamMatch).filter_by(id=id)
    team_match = db.session.scalar(stmt)
    if team_match:
        team_match.score = request.json.get('score') or team_match.score
        team_match.team_id = request.json.get('team_id') or team_match.team_id
        team_match.match_id = request.json.get('match_id') or team_match.match_id
        db.session.commit()
        return TeamMatchSchema().dump(team_match)
    else:
        return {'error': f'The team match you requested with id {id} cannot be found.'}, 404

# DELETE
@team_matches_bp.route('/', methods=['DELETE'])
@jwt_required
def delete_one_team_match(id):
    authorize()
    stmt = db.select(TeamMatch).filter_by(id=id)
    team_match = db.session.scalar(stmt)
    if team_match:
        db.session.delete(team_match)
        db.session.commit()
    else:
        return {'error': f'The team match you requested with id {id} cannot be found.'}, 404
