from init import db, ma

class TeamMatch(db.Model):
    __tablename__ = 'team_matches'
    
    id = db.Column(db.Integer, primary_key=True)
    score = db.Column(db.Integer)

    team_id = db.Column(db.Integer, db.ForeignKey('teams.id', nullable=False))
    match_id = db.Column(db.Integer, db.ForeignKey('matches.id', nullable=False))

    team = db.relationship('Team', back_populates='team_matches')
    match = db.relationship('Match', back_populates='team_matches')
