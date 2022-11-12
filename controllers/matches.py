from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from sqlalchemy.exc import DataError

from init import db
from models.match import Match, MatchSchema
from controllers.auth import authorize

matches_bp = Blueprint('matches', __name__, url_prefix='/matches')

# CREATE
@matches_bp.route('/', methods=['POST'])
@jwt_required()
def create_one_match():
    authorize()
    try:
        match = Match(
            date = request.json['date'],
            time = request.json['time']
        )
        db.session.add(match)
        db.session.commit()
        return MatchSchema().dump(match), 201
    except DataError:
        return {'error': 'Please enter date in the format \'YYYY-MM-DD\' and time in the format \'HH:MM:SS\''}, 400

# READ
@matches_bp.route('/<int:id>/')
def get_one_match(id):
    stmt = db.select(Match).filter_by(id=id)
    match = db.session.scalar(stmt)
    if match:
        return MatchSchema().dump(match)
    else:
        return {'error': f'The match you requested with id {id} cannot be found.'}, 404

@matches_bp.route('/')
def get_all_matches():
    stmt = db.select(Match).order_by(Match.date, Match.time)
    matches = db.session.scalars(stmt)
    return MatchSchema(many=True).dump(matches)

# UPDATE
@matches_bp.route('/<int:id>/', methods=['PUT', 'PATCH'])
@jwt_required()
def update_one_match(id):
    authorize()
    stmt = db.select(Match).filter_by(id=id)
    match = db.session.scalar(stmt)
    try:
        if match:
            match.date = request.json.get('date') or match.date
            match.time = request.json.get('time') or match.time
            db.session.commit()
            return MatchSchema().dump(match)
        else:
            return {'error': f'The match you requested with id {id} cannot be found.'}, 404
    except DataError:
        return {'error': 'Please enter date in the format \'YYYY-MM-DD\' and time in the format \'HH:MM:SS\''}, 400

# DELETE
@matches_bp.route('/<int:id>/', methods=['DELETE'])
@jwt_required()
def delete_one_match(id):
    authorize()
    stmt = db.select(Match).filter_by(id=id)
    match = db.session.scalar(stmt)
    if match:
        db.session.delete(match)
        db.session.commit()
        return {'message': f'Match with id {id} was deleted.'}
    else:
        return {'error': f'The match you requested with id {id} cannot be found.'}, 404
