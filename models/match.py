from init import db, ma
from models.team_match import team_match

class Match(db.Model):
    __tablename__ = 'matches'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    time = db.Column(db.Time, nullable=False)

    results = db.relationship('Result', secondary=team_match, back_populates='matches')

class MatchSchema(ma.Schema):
    class Meta:
        fields = ('id', 'date', 'time')
