""" CRUD functionality for matches data

Functions for viewing, creating, editing and deleting
matches data.

Functions
---------
create_one_match()
get_one_match()
get_all_matches()
update_one_match()
delete_one_match()
"""

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
    """ Creation of one match

    Checks if user logged in and has administrative rights. If
    successful, match attributes provided in json format. New
    match added and committed to database.

    Returns:
        json: If the match creation is successful, all attributes
        will be returned.

        json: If the data is entered in the wrong format then a
        error message and a 400 HTTP status code are returned.
    """
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
        return {'error':
        'Please enter date in the format \'YYYY-MM-DD\' and time in the format \'HH:MM:SS\''
        }, 400

# READ
@matches_bp.route('/<int:id>/')
def get_one_match(id):
    """ Selects one match by its 'id' attribute

    Args:
        id (int): primary key and unique identifier for
        the match.

    Returns:
        json: If the id exists, all attributes for the match
        are returned.

        json: If the id does not exist then an error message and
        a 401 HTTP status code are returned.
    """
    stmt = db.select(Match).filter_by(id=id)
    match = db.session.scalar(stmt)
    if match:
        return MatchSchema().dump(match)
    else:
        return {'error': f'The match you requested with id {id} cannot be found.'}, 404

@matches_bp.route('/')
def get_all_matches():
    """ Selects all matches

    Selects all matches and orders them first by their 'date'
    attribute, then by their 'time' attribute.

    Returns:
        json: All attributes and nested attributes as a list.
    """
    stmt = db.select(Match).order_by(Match.date, Match.time)
    matches = db.session.scalars(stmt)
    return MatchSchema(many=True).dump(matches)

# UPDATE
@matches_bp.route('/<int:id>/', methods=['PUT', 'PATCH'])
@jwt_required()
def update_one_match(id):
    """ Edits one match

    Checks if the current user is logged in and has
    administrative rights. If successful, match selected by
    its 'id' attribute, new values are provided in json format
    and the changes are committed to the database.

    Args:
        id (int): primary key and unique identifier for
        the match.

    Returns:
        json: If the id exists, all attributes for the match
        are returned.

        json: If the id does not exist then an error message and
        a 401 HTTP status code are returned.

        json: If the date or time are entered in the wrong format
        a message is returned and a 400 HTTP status code.
    """
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
    """ Deletes a match from the database

    Checks if the current user is logged in and has administrative
    rights. If successful, selects match by id, deletes the match
    and commits the change to the database.

    Args:
        id (int): primary key and unique identifier for
        the match.

    Returns:
        json: If the id exists, a message is returned confirming
        deletion of the match.

        json: If the id does not exist, a message is returned
        and a 404 HTTP status code.
    """
    authorize()
    stmt = db.select(Match).filter_by(id=id)
    match = db.session.scalar(stmt)
    if match:
        db.session.delete(match)
        db.session.commit()
        return {'message': f'Match with id {id} was deleted.'}
    else:
        return {'error': f'The match you requested with id {id} cannot be found.'}, 404
