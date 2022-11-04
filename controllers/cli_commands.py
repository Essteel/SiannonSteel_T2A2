from init import db, bcrypt
from models.user import User
from models.team import Team
from models.match import Match
from models.team_match import TeamMatch

from flask import Blueprint

db_commands = Blueprint('db', __name__)

@db_commands.cli.command('create')
def create_db():
    print('Tables created successfully.')

@db_commands.cli.command('drop')
def drop_db():
    db.drop_all()
    print('All tables dropped successfully.')

@db_commands.cli.command('seed')
def seed_db():
    teams = [
        Team(
            team_name = 'Team Icicle'
        ),
        Team(
            team_name = 'Meteoroids'
        ),
        Team(
            team_name = 'Team Angular'
        ),
        Team(
            team_name = 'Purple Kangaroo'
        ),
        Team(
            team_name = 'Team Elevate'
        ),
        Team(
            team_name = 'Project Y'
        ),
        Team(
            team_name = 'Team Side Effect'
        ),
        Team(
            team_name = 'Team Victoria'
        ),
        Team(
            team_name = 'Frost Trolls'
        ),
        Team(
            team_name = 'Balance Team'
        )
    ]
    db.session.add_all(teams)
    db.session.commit()
    
    users = [
        User(
            first_name = 'Karl',
            last_name = 'Dandleton',
            email = 'karld@theesportsemail.com',
            is_admin = True,
            password = bcrypt.generate_password_hash('5uperK4rl99').decode('utf-8')
        ),
        User(
            first_name = 'Gin',
            last_name = 'Ginlons',
            email = 'ging@theplayeremail.com',
            password = bcrypt.generate_password_hash('g1ng0nnaw1n!').decode('utf-8'),
            bio = 'Two time world champion for the USA.',
            country = 'USA',
            team_id = 8
        ),
        User(
            first_name = 'Todd',
            last_name = 'Bonzalez',
            email = 'toddb@theplayeremail.com',
            password = bcrypt.generate_password_hash('US4esports4eva').decode('utf-8'),
            bio = 'Rookie taking the scene by storm with their natural skill.',
            country = 'USA',
            team_id = 1
        ),
        User(
            first_name = 'Sleve',
            last_name = 'McDichael',
            email = 'smcdichael@theplayeremail.com',
            password = bcrypt.generate_password_hash('29September*#').decode('utf-8'),
            bio = 'Was on the winning team of the tournament last year.',
            country = 'Scotland',
            team_id = 3
        ),
        User(
            first_name = 'Dwight',
            last_name = 'Escher',
            email = 'dbescher@theplayeremail.com',
            password = bcrypt.generate_password_hash('5lLiU89!Xyp2P').decode('utf-8'),
            bio = 'A new player to the tournament having only joined their team this year.',
            country = 'Germany',
            team_id = 1
        ),
        User(
            first_name = 'Leyla',
            last_name = 'Chen',
            email = 'lchen@theplayeremail.com',
            password = bcrypt.generate_password_hash('PurpleKangaroo95').decode('utf-8'),
            bio = 'First woman to be on the winning team in the tournament\'s history.',
            country = 'China',
            team_id = 3
        ),
        User(
            first_name = 'Mary',
            last_name = 'Oh',
            email = 'mary.oh@theplayeremail.com',
            password = bcrypt.generate_password_hash('winners8637nugget').decode('utf-8'),
            bio = 'Had the highest kill count in last year\'s tournament',
            country = 'South Korea',
            team_id = 8
        ),
        User(
            first_name = 'Anatolia',
            last_name = 'Jones',
            email = 'a.rhodini@theplayeremail.com',
            password = bcrypt.generate_password_hash('EsportsForever03856629').decode('utf-8'),
            bio = 'A new player to the tournament this year who impressed in the championship last month.',
            country = 'Italy',
            team_id = 1
        )
    ]
    db.session.add_all(users)
    db.session.commit()
    
    matches = [
        Match(
            date = '2022-12-01',
            time = '14:00:00'
        ),
        Match(
            date = '2022-12-01',
            time = '17:00:00'
        ),
        Match(
            date = '2022-12-04',
            time = '14:00:00'
        ),
        Match(
            date = '2022-12-04',
            time = '17:00:00'
        ),
        Match(
            date = '2022-12-07',
            time = '17:00:00'
        ),
        Match(
            date = '2022-12-07',
            time = '17:00:00'
        )
    ]
    db.session.add_all(matches)
    db.session.commit()

    team_matches = [
        TeamMatch(
            score = 24,
            team_id = 3,
            match_id = 0
        ),
        TeamMatch(
            score = 17,
            team_id = 8,
            match_id = 0
        ),
        TeamMatch(
            score = 28,
            team_id = 1,
            match_id = 1
        ),
        TeamMatch(
            score = 36,
            team_id = 3,
            match_id = 1
        ),
        TeamMatch(
            team_id = 1,
            match_id = 2
        ),
        TeamMatch(
            team_id = 8,
            match_id = 2
        )
    ]
    db.session.add_all(team_matches)
    db.session.commit()

    print('All tables seeded successfully.')
