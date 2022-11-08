from init import db, ma

team_match = db.Table('team_match',
    db.Column('team_id', db.Integer, db.ForeignKey('teams.id'), primary_key=True),
    db.Column('match_id', db.Integer, db.ForeignKey('matches.id'), primary_key=True)
)

class Result(db.Model):
    __tablename__ = 'results'

    id = db.Column(db.Integer, primary_key=True)
    score = db.Column(db.Integer)

    # team_id = db.Column(db.Integer, db.ForeignKey('teams.id'), nullable=False)
    # match_id = db.Column(db.Integer, db.ForeignKey('matches.id'), nullable=False)

class ResultSchema(ma.Schema):
    class Meta:
        fields = ('id', 'score')
        ordered = True
