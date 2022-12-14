""" Classes for team_matches association table

Classes
-----
TeamMatch: object that represents the team_matches table.
TeamMatchSchema: relational schema of mapped object TeamMatch.
"""

from marshmallow import fields, validates
from marshmallow.validate import And, Length, Range, OneOf
from marshmallow.exceptions import ValidationError

from init import db, ma

VALID_STATUSES = ('won', 'drawn', 'lost')

class TeamMatch(db.Model):
    __tablename__ = 'team_matches'

    id = db.Column(db.Integer, primary_key=True)
    score = db.Column(db.Integer, nullable=True)
    status = db.Column(db.String, nullable=True)

    team_id = db.Column(db.Integer, db.ForeignKey('teams.id', ondelete='cascade'), nullable=False)
    match_id = db.Column(db.Integer, db.ForeignKey('matches.id', ondelete='cascade'), nullable=False)

    team = db.relationship('Team', back_populates='team_matches')
    match = db.relationship('Match', back_populates='team_matches')

class TeamMatchSchema(ma.Schema):
    id = fields.Integer(required=True)
    score = fields.Integer(required=False, validate=Range(min=0, max=1000,
        error='Score cannot be negative or greater than 1000.'
        ))
    status = fields.String(required=False,validate=OneOf(VALID_STATUSES,
        error='Please enter value: \'won\', \'drawn\' or \'lost\''
        ))

    team_id = fields.Integer(required=True)
    match_id = fields.Integer(required=True)

    team = fields.Nested(lambda: 'TeamSchema', only=['name'])
    match = fields.Nested(lambda: 'MatchSchema', only=['date', 'time'])
    
    @validates('match_id')
    def validate_match(self, match_id):
        """ Checks whether two team_matches already exist

        Selects all team_matches and counts how many have the same
        match_id provided as a parameter. If there are more than two
        team_matches with the same match_id a ValidationError is
        raised.

        Args:
            match_id (int): primary key and unique identifier for
            the team_match.

        Raises:
            ValidationError: Error raised if two team_matches with
            the same match_id already exist. As only two teams go
            against each other in a match at a time.
        """        
        stmt = db.select(db.func.count()).select_from(TeamMatch).filter_by(match_id=match_id)
        count = db.session.scalar(stmt)
        if count > 2:
            raise ValidationError('You already have two team match records for that match.')

    class Meta:
        fields = ('id', 'score', 'status', 'team_id', 'match_id', 'team', 'match')
        ordered = True
