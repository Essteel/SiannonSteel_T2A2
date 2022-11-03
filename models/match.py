from init import db, ma

class Match(db.Model):
    __tablename__ = 'matches'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    time = db.Column(db.Time, nullable=False)

class MatchSchema(ma.Schema):
    class Meta:
        fields = ('id', 'date', 'time')
