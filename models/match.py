from marshmallow import fields

from init import db, ma

class Match(db.Model):
    __tablename__ = 'matches'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    time = db.Column(db.Time, nullable=False)

    team_matches = db.relationship('TeamMatch', back_populates='match', cascade='all, delete')

class MatchSchema(ma.Schema):
    team_matches = fields.Nested('TeamMatchSchema', many=True, exclude=['match'])
    class Meta:
        fields = ('id', 'date', 'time', 'team_matches')
