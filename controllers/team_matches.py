from init import db
from models.team_match import Result, ResultSchema
from controllers.auth import authorize

from flask import Blueprint, request
from flask_jwt_extended import jwt_required

results_bp = Blueprint('results', __name__, url_prefix='/results')

# CREATE
@results_bp.route('/', methods=['POST'])
@jwt_required()
def create_one_result():
    authorize()
    result = Result(
        score = request.json['score']
    )
    db.session.add(result)
    db.session.commit()
    return ResultSchema().dump(result), 201

# READ
@results_bp.route('/<int:id>/')
def get_one_result(id):
    stmt = db.select(Result).filter_by(id=id)
    result = db.session.scalar(stmt)
    if result:
        return ResultSchema().dump(result)
    else:
        return {'error': f'The team match you requested with id {id} cannot be found.'}, 404

@results_bp.route('/')
def get_all_results(id):
    stmt = db.select(Result).order_by(Result.id)
    results = db.session.scalars(stmt)
    return ResultSchema(many=True).dump(results)

# UPDATE
@results_bp.route('/<int:id>/', methods=['PUT', 'PATCH'])
@jwt_required()
def update_one_result(id):
    authorize()
    stmt = db.select(Result).filter_by(id=id)
    result = db.session.scalar(stmt)
    if result:
        result.score = request.json.get('score') or result.score
        db.session.commit()
        return ResultSchema().dump(result)
    else:
        return {'error': f'The team match you requested with id {id} cannot be found.'}, 404

# DELETE
@results_bp.route('/', methods=['DELETE'])
@jwt_required()
def delete_one_result(id):
    authorize()
    stmt = db.select(Result).filter_by(id=id)
    result = db.session.scalar(stmt)
    if result:
        db.session.delete(result)
        db.session.commit()
    else:
        return {'error': f'The team match you requested with id {id} cannot be found.'}, 404
