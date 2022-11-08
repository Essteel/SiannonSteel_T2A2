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
    class Meta:
        fields = ('id', 'score', 'team_id', 'match_id')
        ordered = True
