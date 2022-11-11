from marshmallow import fields
from sqlalchemy.ext.hybrid import hybrid_property

from init import db, ma

class Team(db.Model):
    __tablename__ = 'teams'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    @hybrid_property
    def total_won(self):
        total = 0
        for team_match in self.team_matches:
            if team_match.status == 'won':
                total += 1
        return total

    @hybrid_property
    def total_drawn(self):
        total = 0
        for team_match in self.team_matches:
            if team_match.status == 'drawn':
                total += 1
        return total

    @hybrid_property
    def total_lost(self):
        total = 0
        for team_match in self.team_matches:
            if team_match.status == 'lost':
                total += 1
        return total

    users = db.relationship('User', back_populates='team')
    team_matches = db.relationship('TeamMatch', back_populates='team', cascade='all, delete')

class TeamSchema(ma.Schema):
    users = fields.Nested('UserSchema', many=True, exclude=['email', 'password', 'is_admin', 'team'])
    team_matches = fields.Nested('TeamMatchSchema', many=True)
    class Meta:
        fields = ('id', 'name', 'total_won', 'total_drawn', 'total_lost', 'users', 'team_matches')
        ordered = True
