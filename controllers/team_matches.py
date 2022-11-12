from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from flask.json import jsonify
from sqlalchemy.orm import Bundle

from init import db
from models.team_match import TeamMatch, TeamMatchSchema
from models.match import Match, MatchSchema
from models.team import Team, TeamSchema
from controllers.auth import authorize

team_match_bp = Blueprint('results', __name__, url_prefix='/results')

# CREATE
@team_match_bp.route('/', methods=['POST'])
@jwt_required()
def create_one_result():
    authorize()
    data = TeamMatchSchema().load(request.json)
    result = TeamMatch(
        score = data['score'],
        status = data['status'],
        team_id = data['team_id'],
        match_id = data['match_id']
    )
    db.session.add(result)
    db.session.commit()
    return TeamMatchSchema().dump(result), 201

# READ
@team_match_bp.route('/<int:match_id>/')
def get_one_result(match_id):
    stmt = db.select(TeamMatch).filter_by(match_id=match_id)
    results = db.session.scalars(stmt)
    if results:
        return TeamMatchSchema(many=True).dump(results)
    else:
        return {'error': f'The team match you requested with id {id} cannot be found.'}, 404

@team_match_bp.route('/')
def get_all_results():
    stmt = db.select(TeamMatch).order_by(TeamMatch.match_id)
    results = db.session.scalars(stmt)
    return TeamMatchSchema(many=True).dump(results)

# UPDATE
@team_match_bp.route('/<int:id>/', methods=['PUT', 'PATCH'])
@jwt_required()
def update_one_result(id):
    authorize()
    stmt = db.select(TeamMatch).filter_by(id=id)
    result = db.session.scalar(stmt)

    data = TeamMatchSchema().load(request.json, partial=True)
    if result:
        result.score = request.json.get('score') or result.score
        result.status = request.json.get('status') or result.status
        db.session.commit()
        return TeamMatchSchema().dump(data)
    else:
        return {'error': f'The team match you requested with id {id} cannot be found.'}, 404

# DELETE
@team_match_bp.route('/<int:id>/', methods=['DELETE'])
@jwt_required()
def delete_one_result(id):
    authorize()
    stmt = db.select(TeamMatch).filter_by(id=id)
    result = db.session.scalar(stmt)
    if result:
        db.session.delete(result)
        db.session.commit()
        return {'message': f'Result with id {id} was deleted.'}
    else:
        return {'error': f'The team match you requested with id {id} cannot be found.'}, 404
