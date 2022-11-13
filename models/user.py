""" Classes for users table

Classes
-----
User: object that represents the users table.
UserSchema: relational schema of mapped object User.
"""

from marshmallow import fields
from marshmallow.validate import Email, Length

from init import db, ma

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    bio = db.Column(db.Text)
    country = db.Column(db.String)
    is_admin = db.Column(db.Boolean, default=False)

    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'))

    team = db.relationship('Team', back_populates='users')

class UserSchema(ma.Schema):
    id = fields.Integer(required=True)
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)
    email = fields.String(required=True, unique=True, validate=Email(error='Email address does not conform to the expected format.'))
    password = fields.String(required=True)
    bio = fields.String(allow_none=True, validate=Length(max=255, error='Maximum length of bio reached.'))
    country = fields.String(allow_none=True)
    is_admin = fields.Boolean(default=False)

    team_id = fields.Integer(allow_none=True)
    
    team = fields.Nested('TeamSchema', only=['name'])
    class Meta:
        fields = ('id', 'first_name', 'last_name', 'email', 'password', 'bio', 'country', 'is_admin', 'team_id', 'team')
        ordered = True
