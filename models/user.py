from init import db, ma

from marshmallow import fields

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    bio = db.Column(db.Text)
    country = db.Column(db.String)
    is_admin = db.Column(db.Boolean, default=False)

    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'))

    team = db.relationship('Team', back_populates='users')

class UserSchema(ma.Schema):
    team = fields.Nested('TeamSchema', only=['name'])
    class Meta:
        fields = ('id', 'first_name', 'last_name', 'email', 'password', 'bio', 'country', 'is_admin')
        ordered = True
