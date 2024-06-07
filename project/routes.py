from flask import Blueprint, request, jsonify
from db import db
DB = db
bp = Blueprint('todos', __name__)

@bp.route('/todos', methods=['POST'])

@bp.route('/todos', methods=['GET'])

@bp.route('/todos/<int:todo_id>', methods=['GET'])

@bp.route('/todos/<int:todo_id>', methods=['PUT'])

@bp.route('/todos/<int:todo_id>', methods=['DELETE'])

@bp.route('/users', methods=['POST'])

@bp.route('/users', methods=['GET'])

@bp.route('/users/<int:user_id>', methods=['GET'])
