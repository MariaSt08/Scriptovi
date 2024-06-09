from flask import Blueprint, request, jsonify
from db import DB

bp = Blueprint('todos', __name__)

@bp.route('/todos', methods=['POST'])
def create_todo():
    data = request.json
    user_id = data.get('user_id')
    todo = DB.TodoDB.create(data['title'], data.get('description', ''), user_id)
    return jsonify({'id': todo.id, 'title': todo.title, 'description': todo.description, 'done': todo.done, 'user_id': todo.user_id}), 201

@bp.route('/todos', methods=['GET'])
def get_todos():
    todos = DB.TodoDB.read_all()
    result = [{'id': todo.id, 'title': todo.title, 'description': todo.description, 'done': todo.done, 'user_id': todo.user_id} for todo in todos]
    return jsonify(result)

@bp.route('/todos/<int:todo_id>', methods=['GET'])
def get_todo(todo_id):
    todo = DB.TodoDB.read_one(todo_id)
    if todo:
        return jsonify({'id': todo.id, 'title': todo.title, 'description': todo.description, 'done': todo.done, 'user_id': todo.user_id})
    return jsonify({'error': 'Todo not found'}), 404

@bp.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    data = request.json
    todo = DB.TodoDB.update(todo_id, data.get('title'), data.get('description'), data.get('done'))
    if todo:
        return jsonify({'id': todo.id, 'title': todo.title, 'description': todo.description, 'done': todo.done, 'user_id': todo.user_id})
    return jsonify({'error': 'Todo not found'}), 404

@bp.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    success = DB.TodoDB.delete(todo_id)
    if success:
        return '', 204
    return jsonify({'error': 'Todo not found'}), 404

@bp.route('/users', methods=['POST'])
def create_user():
    data = request.json
    user = DB.UserDB.create(data['username'])
    return jsonify({'id': user.id, 'username': user.username}), 201

@bp.route('/users', methods=['GET'])
def get_users():
    users = DB.UserDB.read_all()
    result = [{'id': user.id, 'username': user.username} for user in users]
    return jsonify(result)

@bp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = DB.UserDB.read_one(user_id)
    if user:
        return jsonify({'id': user.id, 'username': user.username})
    return jsonify({'error': 'User not found'}), 404
