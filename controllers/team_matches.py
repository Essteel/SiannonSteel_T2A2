from init import db
from models.team_match import TeamMatch, TeamMatchSchema
from controllers.auth import authorize

from flask import Blueprint, request
from flask_jwt_extended import jwt_required

team_match_bp = Blueprint('results', __name__, url_prefix='/results')

# CREATE
@team_match_bp.route('/', methods=['POST'])
@jwt_required()
def create_one_result():
    authorize()
    result = TeamMatch(
    )
    db.session.add(result)
    db.session.commit()
    return TeamMatchSchema().dump(result), 201

# READ
@team_match_bp.route('/<int:id>/')
def get_one_result(id):
    stmt = db.select(TeamMatch).filter_by(id=id)
    result = db.session.scalar(stmt)
    if result:
        return TeamMatchSchema().dump(result)
    else:
        return {'error': f'The team match you requested with id {id} cannot be found.'}, 404

@team_match_bp.route('/')
def get_all_results():
    stmt = db.select(TeamMatch).order_by(TeamMatch.id)
    results = db.session.scalars(stmt)
    return TeamMatchSchema(many=True).dump(results)

# UPDATE
@team_match_bp.route('/<int:id>/', methods=['PUT', 'PATCH'])
@jwt_required()
def update_one_result(id):
    authorize()
    stmt = db.select(TeamMatch).filter_by(id=id)
    result = db.session.scalar(stmt)
    if result:
        result.score = request.json.get('score') or result.score
        db.session.commit()
        return TeamMatchSchema().dump(result)
    else:
        return {'error': f'The team match you requested with id {id} cannot be found.'}, 404

# DELETE
@team_match_bp.route('/', methods=['DELETE'])
@jwt_required()
def delete_one_result(id):
    authorize()
    stmt = db.select(TeamMatch).filter_by(id=id)
    result = db.session.scalar(stmt)
    if result:
        db.session.delete(result)
        db.session.commit()
    else:
        return {'error': f'The team match you requested with id {id} cannot be found.'}, 404
