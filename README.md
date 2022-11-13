## R1

The problem this application will solve is to keep track of the results of games played throughout an Esports tournament. Users will be able to see how well teams are playing by viewing their scores on a leaderboard. They can also view additional information such as which players are on each team. Players involved in the tournament will create an account which will allow them to register with their team and provide information about themselves for fans to view. They can keep track of their standing in the tournament.

## R2

This problem is important because the organisers of the tournament can use it to register players and keep track of their information such as which team they belong to and as a way to contact them if required as they will provide contact details. This information will be stored securely with information interesting to the public viewable by users and information useful for the organisers, such as email address, kept private and protected.

It also allows them to keep track of how teams are doing within the tournament which will be important not just for deciding the next matches, but to promote and update fans on social media. It will also allow fans, who may not always be able to watch the tournament matches, to keep up to date with the results of their favourite team through viewing the leaderboard and individual team pages. The application can be adapted to suit a variety of different tournament formats.

## R3

PostgreSQL has been chosen as the database management system (DBMS). It has been chosen because it is free and open source and integrates well with Flask. Therefore there is a large amount of documentation and help from the community available online. Other benefits of PostgreSQL are that it is an object-relational DBMS, which allows custom functions and data types to be defined if needed. It also integrates with other popular web frameworks such as Django, Node.js and Ruby on Rails (PostgreSQL, 2022; geeksforgeeks, 2022).

PostgreSQL integrates well with Python, the language that will be used to write this application, as well as many other major languages. It supports JSON data, which will be the data type primarily returned by the application. It also runs on all major operating systems, making the application easier to collaborate on and share (Ionos, 2022).

The drawbacks of PostgreSQL are that not all hosts have it by default. It also performs slower than alternatives such as MySQL and potentially requires more work and cost to improve the speed if required (Sharda, 2021).

## R4

ORM stands for "Object-relational mapping" which means writing queries to the database using the object-oriented paradigm of a programming language, such as Python, rather than querying the database directly using SQL statements (Hoyos, 2018). An ORM mapper is a library which executes this mapping technique using any of the languages which it supports.

A benefit of using an ORM is that it is more user friendly than writing SQL statements. Writing in the same language used to write the application and that the user is fluent in may allow composition of better queries. This, along with writing smaller amounts of cleaner code, will speed up development (Abba, 2022).

ORM's often come with useful built-in features to support tasks such as seeds, connections, transactions, migrations etc. This makes certain tasks easier to carry out without needing a deep understanding of what is going on in the database.

Another advantage of using an ORM is that if the database changes, very few changes need to be made to the code. This is because the ORM abstracts the database system away, therefore as long as the new DBMS works with the same language it's easy to change.

Using SQL directly also increases the risk of making the database vulnerable to SQL injection attacks. An ORM adds sanitizes the input and therefore removes the possibility of SQL injection (Abba, 2022).

## R5

### Login

/auth/login/

- Methods: POST
- Arguments: None
- Description: Creates a bearer token for the user
- Authentication method: None
- Authorization: None
- HTTP response code: 200
- Request body:
  <img width="777" alt="route_auth_login_request_body" src="https://user-images.githubusercontent.com/110761232/201519791-95286a40-235a-401d-8d2c-729d22911dbb.png">
- Response body:
  <img width="777" alt="route_auth_login_response_body" src="https://user-images.githubusercontent.com/110761232/201519762-10034175-445d-4aec-952d-0b1579a99ad4.png">

### Create a match

/matches/

- Methods: POST
- Arguments: None
- Description: Creates a match
- Authentication method: jwt_required()
- Authorization: headers Authorization: Bearer {token}
- HTTP response code: 201
- Request body: 
  ![route_match_create_request_body](https://user-images.githubusercontent.com/110761232/201519759-3967fd7a-d96d-424a-b889-b337058e5c76.png)
- Response body:
  ![route_match_create_response_body](https://user-images.githubusercontent.com/110761232/201519751-e027d234-c505-4b1d-90c4-5da1fdcce948.png)

### Get a match

/matches/\<int:id>/

- Methods: GET
- Arguments: id
- Description: Returns match details
- Authentication method: None
- Authorization: None
- HTTP response code: 200
- Request body: None
- Response body:
  ![route_match_get_one_response_body](https://user-images.githubusercontent.com/110761232/201519748-16502b5a-f12a-46a8-8b50-ea86d223539e.png)

### Get all matches

/matches/

- Methods: GET
- Arguments: None
- Description: Returns details for all matches
- Authentication method: None
- Authorization: None
- HTTP response code: 200
- Request body: None
- Response body:
  ![route_match_get_all_response_body](https://user-images.githubusercontent.com/110761232/201519769-37d1492b-ad27-4016-b968-9a3ceccb31b7.png)

### Update a match

/matches/\<int:id>/

- Methods: PUT, PATCH
- Arguments: id
- Description: Edits the attributes of a match
- Authentication method: jwt_required()
- Authorization: headers Authorization: Bearer {token}
- HTTP response code: 200
- Request body:
  ![route_match_update_request_body](https://user-images.githubusercontent.com/110761232/201519781-0b024af2-a692-4698-b9a4-7e80058fbc2a.png)
- Response body:
  ![route_match_update_response_body](https://user-images.githubusercontent.com/110761232/201519796-acc6381a-277c-4665-86da-cfc7a8509b7e.png)

### Delete a match

/matches/\<int:id>/

- Methods: DELETE
- Arguments: id
- Description: Deletes a match
- Authentication method: jwt_required()
- Authorization: headers Authorization: Bearer {token}
- HTTP response code: 200
- Request body: None
- Response body:
  ![route_match_delete_response_body](https://user-images.githubusercontent.com/110761232/201519806-2858fba9-05dc-4200-b7a8-3f6794cb0c8b.png)

### Create a team

/teams/

- Methods: POST
- Arguments: None
- Description: Creates a team
- Authentication method: jwt_required()
- Authorization: headers Authorization: Bearer {token}
- HTTP response code: 201
- Request body:
  ![route_team_create_request_body](https://user-images.githubusercontent.com/110761232/201519774-2b9c6fcd-bed1-4122-92d3-9294f3cb8e32.png)
- Response body:
  ![route_team_create_response_body](https://user-images.githubusercontent.com/110761232/201519757-a6714323-07f0-4521-8d65-1d8ddd011eb0.png)

### Get a team

/teams/\<int:id>/

- Methods: GET
- Arguments: id
- Description: Returns team details
- Authentication method: None
- Authorization: None
- HTTP response code: 200
- Request body: None
- Response body:
  ![route_team_get_one_response_body](https://user-images.githubusercontent.com/110761232/201519755-521a49c5-257f-4d6f-9106-6128c08acfca.png)

### Get all teams

/teams/

- Methods: GET
- Arguments: None
- Description: Returns details for all teams ordered alphabetically
- Authentication method: None
- Authorization: None
- HTTP response code: 200
- Request body: None
- Response body:
  ![route_team_get_all_response_body](https://user-images.githubusercontent.com/110761232/201519778-58000bf1-93cf-4542-ac92-8e29c2f219ba.png)

### Get leaderboard

/teams/leaderboard/

- Methods: GET
- Arguments: None
- Description: Returns teams ordered by number of matches won, drawn and lost
- Authentication method: None
- Authorization: None
- HTTP response code: 200
- Request body: None
- Response body:
  ![route_team_leaderboard_response_body](https://user-images.githubusercontent.com/110761232/201519818-929c2bdc-8fe9-461d-8f9d-1b3d891e5f66.png)

### Update a team

/matches/\<int:id>/

- Methods: PUT, PATCH
- Arguments: id
- Description: Edits the attributes of a team
- Authentication method: jwt_required()
- Authorization: headers Authorization: Bearer {token}
- HTTP response code: 200
- Request body:
  ![route_team_update_request_body](https://user-images.githubusercontent.com/110761232/201519749-1b4149ea-5b34-49d8-b9ac-256bb0e27037.png)
- Response body:
  ![route_team_update_response_body](https://user-images.githubusercontent.com/110761232/201519802-5effab93-59ca-4418-b6d3-1bfbc2117ff1.png)

### Delete a team

/teams/\<int:id>/

- Methods: DELETE
- Arguments: id
- Description: Deletes a team
- Authentication method: jwt_required()
- Authorization: headers Authorization: Bearer {token}
- HTTP response code: 200
- Request body: None
- Response body:
  ![route_team_delete_response_body](https://user-images.githubusercontent.com/110761232/201519788-a3539931-6f7c-40c2-96cf-5d2e7d6bfa70.png)

### Create a result

/results/

- Methods: POST
- Arguments: None
- Description: Creates a match result
- Authentication method: jwt_required()
- Authorization: headers Authorization: Bearer {token}
- HTTP response code: 201
- Request body:
  ![route_result_create_request_body](https://user-images.githubusercontent.com/110761232/201519752-9ed44155-e8a3-4cb9-bfeb-bada3e5c3a79.png)
- Response body:
  ![route_result_create_response_body](https://user-images.githubusercontent.com/110761232/201519767-c4fd71eb-dde6-4b8b-8faf-50e8e4a55889.png)

### Get a result

/results/\<int:match_id>/

- Methods: GET
- Arguments: match_id
- Description: Returns the results of a match
- Authentication method: jwt_required()
- Authorization: headers Authorization: Bearer {token}
- HTTP response code: 200
- Request body: None
- Response body:
  ![route_result_get_one_response_body](https://user-images.githubusercontent.com/110761232/201519753-1bc58d26-9c53-4220-808e-be37cb3f7b15.png)

### Get all results

/results/

- Methods: GET
- Arguments: None
- Description: Returns details for all results
- Authentication method: jwt_required()
- Authorization: headers Authorization: Bearer {token}
- HTTP response code: 200
- Request body: None
- Response body:
  ![route_result_get_all_response_body](https://user-images.githubusercontent.com/110761232/201519777-e5d08acd-8af0-4652-9e80-0ee2e8115e5f.png)

### Update a result

/results/\<int:id>/

- Methods: PUT, PATCH
- Arguments: id
- Description: Edits the attributes of a result
- Authentication method: jwt_required()
- Authorization: headers Authorization: Bearer {token}
- HTTP response code: 200
- Request body:
  ![route_result_update_request_body](https://user-images.githubusercontent.com/110761232/201519775-aafafe90-233e-4e0a-b839-91d57020a4a4.png)
- Response body:
  ![route_result_update_response_body](https://user-images.githubusercontent.com/110761232/201519809-130bcefd-43b2-46e1-abb3-065dfc591984.png)

### Delete a result

/results/\<int:id>/

- Methods: DELETE
- Arguments: id
- Description: Deletes a match
- Authentication method: jwt_required()
- Authorization: headers Authorization: Bearer {token}
- HTTP response code: 200
- Request body: None
- Response body:
  ![route_result_delete_response_body](https://user-images.githubusercontent.com/110761232/201519795-eea604b5-f57f-40fc-9106-3401f3b3cc2e.png)

### Create a user

/users/register/

- Methods: POST
- Arguments: None
- Description: Creates a user
- Authentication method: None
- Authorization: None
- HTTP response code: 201
- Request body:
  ![route_user_create_request_body](https://user-images.githubusercontent.com/110761232/201519821-8dca52fb-2730-4b4c-b22c-b34d98edf155.png)
- Response body:
  ![route_user_create_response_body](https://user-images.githubusercontent.com/110761232/201519744-68b04159-b60d-477d-8938-f346b7526c06.png)

### Get a user

/users/\<int:id>/

- Methods: GET
- Arguments: id
- Description: Returns the details of the user except password
- Authentication method: jwt_required()
- Authorization: headers Authorization: Bearer {token}
- HTTP response code: 200
- Request body: None
- Response body:
  ![route_user_get_one_response_body](https://user-images.githubusercontent.com/110761232/201519790-3531b14a-ea80-4876-aacd-3df3383ef632.png)

### Get all users

/users/

- Methods: GET
- Arguments: None
- Description: Returns details for all users except password
- Authentication method: jwt_required()
- Authorization: headers Authorization: Bearer {token}
- HTTP response code: 200
- Request body: None
- Response body:
  ![route_user_get_all_response_body](https://user-images.githubusercontent.com/110761232/201519811-008afe21-babc-4482-8082-4b344d00b30f.png)

### Update a user

/users/\<int:id>/

- Methods: PUT, PATCH
- Arguments: id
- Description: Edits the attributes of a user
- Authentication method: jwt_required()
- Authorization: headers Authorization: Bearer {token}
- HTTP response code: 200
- Request body:
  ![route_user_update_request_body](https://user-images.githubusercontent.com/110761232/201519810-b81b0443-064b-4926-a32b-c680f4c5584a.png)
- Response body:
  ![route_user_update_response_body](https://user-images.githubusercontent.com/110761232/201519793-cd67d464-0d8f-4ed4-b994-545327995689.png)

### Delete a user

/users/\<int:id>/

- Methods: DELETE
- Arguments: id
- Description: Deletes a user
- Authentication method: jwt_required()
- Authorization: headers Authorization: Bearer {token}
- HTTP response code: 200
- Request body: None
- Response body:
  ![route_user_delete_response_body](https://user-images.githubusercontent.com/110761232/201519800-adbf8feb-ad3d-4ab8-9ae8-38fe46c4cecb.png)

## R6

![ERD_T2A2](https://user-images.githubusercontent.com/110761232/201519817-58c82b8e-bfae-4cb2-b473-f6f6e8e02c8e.png)

## R7

### Flask-JWT-Extended

A Flask extension which can be used to create JSON Web Tokens, check the identity of a user before they can access a route and get the identity of a user from the token.

Available here: <https://pypi.org/project/Flask-JWT-Extended/>

### PyJWT

A Python implementation of a JSON Web Token and a dependent of the Flask JWT Extended extension.

Available here: <https://pypi.org/project/PyJWT/>

### Flask-Bcrypt

A Flask extension which can be used to hash sensitive data such as passwords using the bcrypt algorithm. Bcrypt hashes slowly, protecting functions such as logging in from brute force attacks.

Available here: <https://pypi.org/project/Flask-Bcrypt/>

### SQLAlchemy

An object-relational mapper for the python language. Allows access to the database using queries written in Python instead of SQL. SQLAlchemy is database-agnostic, therefore can be linked to any supported database such as MySQL or PostgreSQL.

Available here: <https://pypi.org/project/SQLAlchemy/>

### Psycopg

As SQLAlchemy is database-agnostic an adapter is required to link it to a PostgreSQL database. Psycopg is an adapter that works with the Python language.

Available here : <https://pypi.org/project/psycopg2/>

### Marshmallow

A library which converts objects to and from Python data types. Marshmallow is framework-agnostic and can be used with.

Available here: <https://pypi.org/project/marshmallow/>

## R8

R8 is about the models, which is a bit different to the database. The models will likely have methods/behaviour to explain, which are independent of the database representation. In some cases, the way you represent things in the models will be different to how it's represented in the database, so that can be worth explaining too.

The models within the project are User, Team, Match and TeamMatch.

### User

The User model is a python object which represents the users entity and maps to the users table. It has the following attributes: id, first_name, last_name, email, password, bio, country, is_admin, team_id. It has a optional many to optional one relationship with the Team model where Team is the parent and User is the child. This is created through the presence of the id attribute from the Team model within the User model as 'team_id'.

```py
team = db.relationship('Team', back_populates='users')
```

The User object is mapped to the relational schema UserSchema. Within the schema the relationship is present as a nested field 'team' which allows the name of the team the user belongs to be returned alongside the schema.

```py
team = fields.Nested('TeamSchema', only=['name'])
```

### Team

The Team model is a python object which represents the teams entity and maps to the teams table. It has the following attributes: id, team_name, won_order, drawn_order, lost_order. It also has three hybrid properties 'total_won', 'total_drawn' and 'total_lost' which calculate the number of matches the team has won, drawn and lost respectively.

It has a optional one to optional many relationship with the User model where User is the child and Team is the parent. This is created through the presence of the id attribute from the Team model within the User model as 'team_id'. It has a mandatory one to optional many relationship with the TeamMatches association object where TeamMatch is the child and Team is the parent. This is created through the presence of the id attribute from the Team model within the TeamMatch model as 'team_id'. The relationship is set to cascade on deletion, therefore if the team is deleted the team_match will also be deleted.

```py
users = db.relationship('User', back_populates='team')
team_matches = db.relationship('TeamMatch', back_populates='team', cascade='all, delete')
```

The Team object is mapped to the relational schema TeamSchema. Within the schema the relationships are present as nested fields 'users' and 'team_matches' which allows selected details about the players within the team and the results of the teams matches to be returned alongside the schema.

```py
users = fields.Nested('UserSchema', many=True, exclude=['email', 'password', 'is_admin', 'team'])
team_matches = fields.Nested(lambda: 'TeamMatchSchema', many=True, exclude=['team'])
```

### Match

The Match model is a python object which represents the matches entity and maps to the users table. It has the following attributes: id, date, time. It has a mandatory one to optional many relationship with the TeamMatch association object where Match is the parent and TeamMatch is the child. This is created through the presence of the id attribute from the Match model within the TeamMatch model as 'match_id'. The relationship is set to cascade on deletion, therefore if the match is deleted the team_match will also be deleted.

```py
team_matches = db.relationship('TeamMatch', back_populates='match', cascade='all, delete')
```

The Match object is mapped to the relational schema MatchSchema. Within the schema the relationship is present as a nested field 'team_matches' which allows the results of the match to be returned alongside the schema.

```py
team_matches = fields.Nested(lambda: 'TeamMatchSchema', many=True, exclude=['match'])
```

### TeamMatch

TeamMatch is an association object which represents the many to many relationship which exists between Team and Match. Each team can have many matches and each match will involve more that one team. It has the following attributes: id, score, status, team_id, match_id. It has an optional many to mandatory one relationship to both the Team and Match models where they are the parents and TeamMatch is the child. These relationships are created through the presence of the id attributes from the Team and Match models within the TeamMatch model as 'team_id' and 'match_id' respectively.

``` py
team = db.relationship('Team', back_populates='team_matches')
match = db.relationship('Match', back_populates='team_matches')
```

The TeamMatch association object is mapped to the relational schema TeamMatchSchema. Within the schema the relationships are present as nested fields 'team' and 'match' allowing the name of the team as well as the date and time of the match to be returned alongside the schema.

``` py
team = fields.Nested(lambda: 'TeamSchema', only=['name'])
match = fields.Nested(lambda: 'MatchSchema', only=['date', 'time'])
```

## R9

Entities represented within the database are: users, team_matches, teams and matches.

### users

Represents player users and admin users. The users entity has the following attributes represented by columns within the table: id, first_name, last_name, email, password, bio, country, is_admin, team_id.

Each user may belong to zero or one team, and each team will have zero or many players - a optional one to optional many relationship. This relation is formed by the presence of the foreign key constraint 'team_id' which references the primary key 'id' column within the teams table. The presence of a value in the 'team_id' column is optional as administrative users would not belong to a team.

<img width="777" alt="users_table" src="https://user-images.githubusercontent.com/110761232/201519814-07dfb3ce-2382-41a8-84ee-b3d8613c7be7.png">

### team_matches

Represents the final score for a team for a particular match. The team_matches entity has the following attributes represented by columns within the table: id, score, status, team_id, match_id.

Each team match will correspond to one and only one team and each team will have zero or many team matches - a mandatory one to optional many relationship. This relation is formed by the presence of the foreign key constraint 'team_id' which references the primary key 'id' column within the teams table. The presence of a value in the 'team_id' column is mandatory as a team match requires the teams playing in the match to be known.

Each team match will correspond to one and only one match but each match will have zero or many team matches - a mandatory one to optional many relationship. This relation is formed by the presence of the foreign key constraint 'match_id' which references the primary key 'id' column within the matches table. The presence of a value in the 'match_id' column is mandatory as a team match requires the match time and date to be known before its creation.

<img width="777" alt="team_matches_table" src="https://user-images.githubusercontent.com/110761232/201519798-7e2b236c-cda6-4047-8129-ea84dc25ae42.png">

### teams

Represents teams enrolled in the tournament. The teams entity has the following attributes represented by columns within the table: id, team_name, won_order, drawn_order, lost_order.

Each team will have zero or many users as its team members and each user may belong to zero or one team - a optional many to optional one relationship. This relation is formed by the referencing of the teams primary key 'id' column as the 'team_id' foreign key constraint within the users table.

Each team will have zero or many team matches and each team match will relate to one and only one team - a optional many to mandatory one relationship. This relation is formed by the referencing of the teams primary key 'id' column as the 'team_id' foreign key constraint within the team_matches table.

<img width="886" alt="teams_table" src="https://user-images.githubusercontent.com/110761232/201519804-219b8f13-afed-4a09-9e8e-b051c60972c5.png">

### matches

Represents the timings for matches that have taken place or will take place in the tournament. The matches entity has the following attributes represented by columns within the table: id, date, time.

Each match will relate to zero or many teams and each team match will relate to one and only one match - an optional many to mandatory one relationship. This relation is formed by the referencing of the matches primary key 'id' column as the 'match_id' foreign key constraint within the team_matches table.

<img width="886" alt="matches_table" src="https://user-images.githubusercontent.com/110761232/201519776-d1c25048-e664-477c-b225-d56d4a46623a.png">

## R10

I undertook an agile approach to manage tasks within the project aided by the use of a Trello board. The Trello board had four columns labelled 'To Do', 'In Progress', 'Ready for Review/Testing' and 'Complete'. Cards within the Trello board represented user stories which outlined an action a user may want to take with the application. Under each user story was a checklist of tasks that would need to be carried out to implement that feature.

![3_Trello_updated_cover_design](https://user-images.githubusercontent.com/110761232/201519819-e633a3c6-cb83-4c8b-8a0f-0c5989d34497.png)

Cards were also created to represent each area required for the documentation of the project. Each of these also had an associated checklist of tasks to complete in order to satisfy that element of the documentation. Each Card was given a priority label and a rough date for completion based on its complexity and when it would be ideal to have it finished. They were also given different covers to differentiate easily between tasks related to coding or documentation.

<img width="1129" alt="4_Trello_in_progress" src="https://user-images.githubusercontent.com/110761232/201519783-1e6d9db0-2a84-4d56-9843-7337b46edbe1.png">

As the period for the completion of the project was approximately 2 weeks sprints were completed every two days. Each morning the tasks for completion were reviewed on the Trello board to establish progress and any blockers. Then at the end of the sprint the Trello board was updated with any tasks started or completed moved to the appropriate column. Any features completed within the sprint were manually tested to make sure they worked as expected.

At the end of each sprint whether the tasks were on track or ahead of schedule and any blockers were taken into account and used to adjust the tasks to be completed in the next sprint. Blockers may be noted down as comments if they were not resolved during the desired sprint. This process was iterated over until completion of the project.

![5_Trello_comments](https://user-images.githubusercontent.com/110761232/201519772-f46ca10f-0632-44b8-a7b9-c01fc3c69338.png)

The Trello board can be viewed here: <https://trello.com/b/pTojjvB2/siannonsteelt2a2>

---

### References

Abba, I, R, *What is an ORM - The Meaning of Object Relational Mapping Database Tools*, freeCodeCamp website, viewed: November 9th 2022 <https://www.freecodecamp.org/news/what-is-an-orm-the-meaning-of-object-relational-mapping-database-tools/>

Hoyos, M, 2018, *What is an ORM and Why You Should Use it*, Medium blog, viewed: November 9th 2022 <https://blog.bitsrc.io/what-is-an-orm-and-why-you-should-use-it-b2b6f75f5e2a>

Geeksforgeeks, 2022, Difference between RDBMS and OODBMS, geeksforgeeks website, viewed 11 November 2022 <https://www.geeksforgeeks.org/difference-between-rdbms-and-oodbms/>

Ionos, 2022, PostgreSQL: a closer look at the object-relational database management system, Ionos website, viewed 11 November 2022 <https://www.ionos.com/digitalguide/server/know-how/postgresql/>

PostgreSQL, 2022, About, PostgreSQL website, viewed 21 October 2022 <https://www.postgresql.org/ about/>

Sharda, A, 2021, What is PostgreSQL? Introduction, Advantages & Disadvantages, LinkedIn website, viewed 11 November 2022 <https://www.linkedin.com/pulse/what-postgresql-introduction-advantages- disadvantages-ankita-sharda/>
