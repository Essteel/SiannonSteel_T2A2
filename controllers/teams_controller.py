""" CRUD functionality for teams data

Functions for viewing, creating, editing and deleting
matches data.

Functions
---------
create_team()
get_all_teams()
get_one_team()
get_leaderboard()
update_one_team()
delete_one_team()
"""

from flask import Blueprint, request
from flask_jwt_extended import jwt_required

from init import db
from models.team import Team, TeamSchema
from controllers.auths_controller import authorize

teams_bp = Blueprint('teams', __name__, url_prefix='/teams')

# CREATE
@teams_bp.route('/', methods=['POST'])
@jwt_required()
def create_team():
    """ Creation of one team

    Checks if user logged in and has administrative rights. If
    successful, team attributes provided in json format. New
    team added and committed to database.

    Returns:
        json: If the team creation is successful, all attributes
        will be returned.
    """    
    authorize()
    data = TeamSchema().load(request.json)
    team = Team(
        name = data['name']
    )
    db.session.add(team)
    db.session.commit()
    return TeamSchema().dump(team), 201

# READ
@teams_bp.route('/')
def get_all_teams():
    """ Selects all teams ordered by name

    Returns:
        json: A list of team dictionaries ordered
        by the name attribute.
    """    
    stmt = db.select(Team).order_by(Team.name)
    teams = db.session.scalars(stmt)
    return TeamSchema(many=True, exclude=['users', 'team_matches', 'won_order', 'drawn_order', 'lost_order']).dump(teams)

@teams_bp.route('/<int:id>/')
def get_one_team(id):
    """ Selects one team by its 'id' attribute

    Args:
        id (int): primary key and unique identifier for
        the match.

    Returns:
        json: If the id exists, attributes for the team
        are returned.

        json: If the id does not exist then an error message and
        a 401 HTTP status code are returned.
    """    
    stmt = db.select(Team).filter_by(id=id)
    team = db.session.scalar(stmt)
    if team:
        return TeamSchema(exclude=['won_order', 'drawn_order', 'lost_order']).dump(team)
    else:
        return {'error': f'The team you requested with id {id} cannot be found.'}, 404

@teams_bp.route('/leaderboard/')
def get_leaderboard():
    """ A list of all teams ordered by matches won

    Selects all teams and assigns the current number of
    games each team has won, drawn and lost to the order
    attributes. The order attributes 'won_order', 'drawn_order'
    and 'lost_order' are then used to rank the teams by how
    well they are doing.

    Used to get around issue of not being able to order by
    hybrid properties 'total_won', 'total_drawn' and
    'total_lost'.

    Returns:
        json: An ordered list of teams ordered by teams
        with the most games won, then drawn then lost.
    """    
    stmt = db.select(Team)
    _teams = db.session.scalars(stmt)
    for team in _teams:
        team.won_order = team.total_won
        team.drawn_order = team.total_drawn
        team.lost_order = team.total_lost

    stmt = db.select(Team).order_by(Team.won_order.desc(), Team.drawn_order.desc(), Team.lost_order.desc())
    teams = db.session.scalars(stmt)
    return TeamSchema(many=True, exclude=['users', 'team_matches', 'won_order', 'drawn_order', 'lost_order']).dump(teams)

# UPDATE
@teams_bp.route('/<int:id>/', methods=['PUT', 'PATCH'])
@jwt_required()
def update_one_team(id):
    """ Edits one team

    Checks if the current user is logged in and has
    administrative rights. If successful, team selected by
    its 'id' attribute, new values are provided in json format
    and the changes are committed to the database.

    Args:
        id (int): primary key and unique identifier for
        the team.

    Returns:
        json: If the id exists, all attributes for the team
        are returned.

        json: If the id does not exist then an error message and
        a 404 HTTP status code are returned.
    """
    authorize()
    stmt = db.select(Team).filter_by(id=id)
    team = db.session.scalar(stmt)
    if team:
        team.name = request.json.get('name') or team.name
        team.total_won = request.json.get('total_won') or team.total_won
        team.total_drawn = request.json.get('total_drawn') or team.total_drawn
        team.total_lost = request.json.get('total_lost') or team.total_lost
        db.session.commit()
        return TeamSchema(exclude=['won_order', 'drawn_order', 'lost_order']).dump(team)
    else:
        return {'error': f'The team you requested with id {id} cannot be found.'}, 404

# DELETE
@teams_bp.route('/<int:id>/', methods=['DELETE'])
@jwt_required()
def delete_one_team(id):
    """ Deletes a team from the database

    Checks if the current user is logged in and has administrative
    rights. If successful, selects team by id, deletes the team
    and commits the change to the database.

    Args:
        id (int): primary key and unique identifier for
        the match.

    Returns:
        json: If the id exists, a message is returned confirming
        deletion of the team.

        json: If the id does not exist, a message is returned
        and a 404 HTTP status code.
    """
    authorize()
    stmt = db.select(Team).filter_by(id=id)
    team = db.session.scalar(stmt)
    if team:
        db.session.delete(team)
        db.session.commit()
        return {'message': f'\'{team.name}\' was deleted successfully.'}
    else:
        return {'error': f'The team you requested with id {id} cannot be found.'}, 404
