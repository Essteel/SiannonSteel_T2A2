""" Classes for teams table

Classes
-----
Team: object that represents the teams table.
TeamSchema: relational schema of mapped object Team.
"""

from marshmallow import fields
from marshmallow.validate import Regexp
from sqlalchemy.ext.hybrid import hybrid_property

from init import db, ma

class Team(db.Model):
    __tablename__ = 'teams'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)

    @hybrid_property
    def total_won(self):
        """ Calculates total matches won by team

        Returns:
            int: count of teams matches with the status 'won'.
        """
        total = 0
        for team_match in self.team_matches:
            if team_match.status == 'won':
                total += 1
        return total

    @hybrid_property
    def total_drawn(self):
        """ Calculates total matches drawn by team

        Returns:
            int: count of teams matches with the status 'drawn'.
        """        
        total = 0
        for team_match in self.team_matches:
            if team_match.status == 'drawn':
                total += 1
        return total

    @hybrid_property
    def total_lost(self):
        """ Calculates total matches lost by team

        Returns:
            int: count of teams matches with the status 'lost'.
        """
        total = 0
        for team_match in self.team_matches:
            if team_match.status == 'lost':
                total += 1
        return total

    won_order = db.Column(db.Integer, nullable=True)
    drawn_order = db.Column(db.Integer, nullable=True)
    lost_order = db.Column(db.Integer, nullable=True)

    users = db.relationship('User', back_populates='team')
    team_matches = db.relationship('TeamMatch', back_populates='team', cascade='all, delete')

class TeamSchema(ma.Schema):
    id = fields.Integer(required=True)
    name = fields.String(required=True, validate=(Regexp('^[a-zA-Z0-9 ]+$', error='Only letters, numbers and spaces are valid.')))
    total_won = fields.Integer()
    total_drawn = fields.Integer()
    total_lost = fields.Integer()
    won_order = fields.Integer()
    drawn_order = fields.Integer()
    lost_order = fields.Integer()

    users = fields.Nested('UserSchema', many=True, exclude=['email', 'password', 'is_admin', 'team'])
    team_matches = fields.Nested(lambda: 'TeamMatchSchema', many=True, exclude=['team'])

    class Meta:
        fields = ('id', 'name', 'total_won', 'total_drawn', 'total_lost',
        'won_order', 'drawn_order', 'lost_order', 'users', 'team_matches')
        ordered = True
