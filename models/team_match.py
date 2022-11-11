from marshmallow import fields, validates
from marshmallow.validate import And, Length, Range
from marshmallow.exceptions import ValidationError

from init import db, ma

class TeamMatch(db.Model):
    __tablename__ = 'team_matches'

    id = db.Column(db.Integer, primary_key=True)
    score = db.Column(db.Integer, nullable=True)

    team_id = db.Column(db.Integer, db.ForeignKey('teams.id', ondelete='cascade'), nullable=False)
    match_id = db.Column(db.Integer, db.ForeignKey('matches.id', ondelete='cascade'), nullable=False)

    team = db.relationship('Team', back_populates='team_matches')
    match = db.relationship('Match', back_populates='team_matches')

class TeamMatchSchema(ma.Schema):
    score = fields.Integer(validate=And(
        Range(min=0, error='Score cannot be negative.'),
        Range(max=1000, error='Score cannot be greater than 1000.')
    ))
    # @validates('match_id')
    # def validate_match(self, match_id):
    #     stmt = db.select(db.func.count()).select_from(TeamMatch).filter_by(match_id=match_id)
    #     count = db.session.scalar(stmt)
    #     if count > 2:
    #         raise ValidationError('You already have two team match records for that match.')
    class Meta:
        fields = ('id', 'score', 'team_id', 'match_id')
        ordered = True
