""" CRUD functionality for team matches data

Functions for admin users to view, create, edit
and delete team matches data.

Functions
---------
create_one_result()
get_one_result()
get_all_results()
update_one_result()
delete_one_result()
"""

from flask import Blueprint, request
from flask_jwt_extended import jwt_required

from init import db
from models.team_match import TeamMatch, TeamMatchSchema
from controllers.auths_controller import authorize

team_match_bp = Blueprint('results', __name__, url_prefix='/results')

# CREATE
@team_match_bp.route('/', methods=['POST'])
@jwt_required()
def create_one_result():
    """ Creation of one team match

    Checks current user is logged in and has administrative rights.
    Team match attributes provided in json format. New team match
    added and committed to database.

    Returns:
        json: If the team match creation is successful, all attributes
        will be returned.

        json: If the user credentials are invalid then an error
        message and a 401 HTTP status code are returned.
    """
    authorize()
    data = TeamMatchSchema().load(request.json, partial=True)
    result = TeamMatch(
        team_id = data['team_id'],
        match_id = data['match_id']
    )
    db.session.add(result)
    db.session.commit()
    return TeamMatchSchema().dump(result), 201

# READ
@team_match_bp.route('/<int:match_id>')
@jwt_required()
def get_one_result(match_id):
    """ View one team match

    Checks current user is logged in and has administrative rights.
    Team match selected by 'match_id'.

    Returns:
        json: If the match_id is valid, all attributes of the team
        match are returned.

        json: If the match_id value is invalid then an error
        message and a 404 HTTP status code are returned.
    """
    authorize()
    stmt = db.select(TeamMatch).filter_by(match_id=match_id)
    results = db.session.scalars(stmt)
    if results:
        return TeamMatchSchema(many=True).dump(results)
    else:
        return {'error': f'The match you requested with id {match_id} cannot be found.'}, 404

@team_match_bp.route('/')
@jwt_required()
def get_all_results():
    """ View all team matches

    Checks current user is logged in and has administrative rights.
    All team matches selected.

    Returns:
        json: All attributes of the team match are returned.
    """
    authorize()
    stmt = db.select(TeamMatch)
    results = db.session.scalars(stmt)
    return TeamMatchSchema(many=True).dump(results)

# UPDATE
@team_match_bp.route('/<int:id>/', methods=['PUT', 'PATCH'])
@jwt_required()
def update_one_result(id):
    """ Edits one team match

    Checks if the current user is logged in and has
    administrative rights. If successful, team match selected by
    its 'id' attribute, new values are provided in json format
    and the changes are committed to the database.

    Args:
        id (int): primary key and unique identifier for
        the team match.

    Returns:
        json: If the id exists, all attributes for the team match
        are returned.

        json: If the id does not exist then an error message and
        a 401 HTTP status code are returned.
    """
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
    """ Deletes a team match from the database

    Checks if the current user is logged in and has administrative
    rights. If successful, selects team match by id, deletes the
    team match and commits the change to the database.

    Args:
        id (int): primary key and unique identifier for
        the team match.

    Returns:
        json: If the id exists, a message is returned confirming
        deletion of the team match.

        json: If the id does not exist, a message is returned
        and a 404 HTTP status code.
    """
    authorize()
    stmt = db.select(TeamMatch).filter_by(id=id)
    result = db.session.scalar(stmt)
    if result:
        db.session.delete(result)
        db.session.commit()
        return {'message': f'Result with id {id} was deleted.'}
    else:
        return {'error': f'The team match you requested with id {id} cannot be found.'}, 404
