from init import db, ma

class TeamMember(db.Model):
    __tablename__ = 'team_members'

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.relationship('User', back_populates='team_member')
    team_id = db.relationship('Team', back_populates='team_member')

class TeamMemberSchema(ma.Schema):
    
