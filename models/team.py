from init import db, ma

class Team(db.Model):
    __tablename__ = 'teams'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    total_won = db.Column(db.Integer, default=0)
    total_drawn = db.Column(db.Integer, default=0)
    total_lost = db.Column(db.Integer, default=0)

    users = db.relationship('User', back_populates='team')
    team_matches = db.relationship('TeamMatch', back_populates='team', cascade='all, delete')

class TeamSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'total_won', 'total_drawn', 'total_lost')
