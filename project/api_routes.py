from flask import Blueprint, request, jsonify
from db import  todos,users

bp = Blueprint('todos', __name__)
    
@bp.route('/todos', methods=['POST'])
def create_todo():
    data = request.json
    user_id = data.get('user_id')
    todo = todos.create(data['title'], data.get('description', ''), user_id)
    return jsonify({'id': todo.id, 'title': todo.title, 'description': todo.description, 'done': todo.done, 'user_id': todo.user_id}), 201

@bp.route('/todos', methods=['GET'])
def get_todos():
    data = request.json
    user_id = data.get('user_id')
    if user_id is None:
        return jsonify({'error':'you must specify user id'}) # we dont want unauthorized access
    list_of_todos = todos.read_all()
    result = [{'id': todo.id, 'title': todo.title, 'description': todo.description, 'done': todo.done, 'user_id': todo.user_id} for todo in list_of_todos]
    return jsonify(result)

@bp.route('/todos/<int:todo_id>', methods=['GET'])
def get_todo(todo_id):
    todo = todos.read_one(todo_id)
    if todo:
        return jsonify({'id': todo.id, 'title': todo.title, 'description': todo.description, 'done': todo.done, 'user_id': todo.user_id})
    return jsonify({'error': 'Todo not found'}), 404

@bp.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    data = request.json
    todo = todos.update(todo_id, data.get('title'), data.get('description'), data.get('done'))
    if todo:
        return jsonify({'id': todo.id, 'title': todo.title, 'description': todo.description, 'done': todo.done, 'user_id': todo.user_id})
    return jsonify({'error': 'Todo not found'}), 404

@bp.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    success = todos.delete(todo_id)
    if success:
        return '', 204
    return jsonify({'error': 'Todo not found'}), 404

@bp.route('/users', methods=['POST'])
def create_user():
    data = request.json
    password = data["password"]
    if(len(password) > 5):
        return jsonify({"error":"password must be atleast 5 chars long"})
    user = users.create(data['username'],data["password"])
    return jsonify({'id': user.id, 'username': user.username}), 201

@bp.route('/users', methods=['GET'])
def get_users():
    users = users.read_all()
    result = [{'id': user.id, 'username': user.username} for user in users]
    return jsonify(result)

@bp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = users.read_one(user_id)
    if user:
        return jsonify({'id': user.id, 'username': user.username})
    return jsonify({'error': 'User not found'}), 404
