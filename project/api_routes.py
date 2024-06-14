from flask import Blueprint, request, jsonify
from db import todos, users

bp = Blueprint('todos', __name__)

@bp.route('/todos', methods=['POST'])
def create_todo():
    data = request.json
    user_id = data.get('user_id')
    if not user_id:
        return jsonify({'error': 'User ID is required'}), 400
    todo = todos.create(data['title'], data.get('description', ''), user_id)
    return jsonify({
        'id': todo.id, 'title': todo.title, 
        'description': todo.description, 'done': todo.done, 
        'user_id': todo.user_id
    }), 201

@bp.route('/todos/<int:user_id>', methods=['GET'])
def get_todos(user_id):
    list_of_todos = todos.read_all()
    result = [
        {'id': todo.id, 'title': todo.title, 'description': todo.description, 
         'done': todo.done, 'user_id': todo.user_id} 
        for todo in list_of_todos if todo.user_id == user_id
    ]
    return jsonify(result), 200

@bp.route('/todos/<int:todo_id>', methods=['GET'])
def get_todo(todo_id):
    todo = todos.read_one(todo_id)
    if todo:
        return jsonify({
            'id': todo.id, 'title': todo.title, 
            'description': todo.description, 'done': todo.done, 
            'user_id': todo.user_id
        }), 200
    return jsonify({'error': 'Todo not found'}), 404

@bp.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo_put(todo_id):
    data = request.json
    user_id = data.get('user_id')
    todo = todos.read_one(todo_id)
    if not todo:
        return jsonify({'error': 'Todo not found'}), 404
    if todo.user_id != user_id:
        return jsonify({'error': 'Forbidden'}), 403

    todo = todos.update(todo_id, data.get('title'), data.get('description'), data.get('done'))
    return jsonify({
        'id': todo.id, 'title': todo.title, 
        'description': todo.description, 'done': todo.done, 
        'user_id': todo.user_id
    }), 200

@bp.route('/todos/<int:todo_id>', methods=['PATCH'])
def update_todo_patch(todo_id):
    data = request.json
    user_id = data.get('user_id')
    todo = todos.read_one(todo_id)
    if not todo:
        return jsonify({'error': 'Todo not found'}), 404
    if todo.user_id != user_id:
        return jsonify({'error': 'Forbidden'}), 403

    title = data.get('title', todo.title)
    description = data.get('description', todo.description)
    done = data.get('done', todo.done)

    updated_todo = todos.update(todo_id, title, description, done)
    return jsonify({
        'id': updated_todo.id, 'title': updated_todo.title, 
        'description': updated_todo.description, 'done': updated_todo.done, 
        'user_id': updated_todo.user_id
    }), 200

@bp.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    user_id = request.json.get('user_id')
    todo = todos.read_one(todo_id)
    if not todo:
        return jsonify({'error': 'Todo not found'}), 404
    if todo.user_id != user_id:
        return jsonify({'error': 'Forbidden'}), 403

    success = todos.delete(todo_id)
    if success:
        return '', 204
    return jsonify({'error': 'Todo not found'}), 404

@bp.route('/users', methods=['POST'])
def create_user():
    data = request.json
    password = data["password"]
    if len(password) < 6:
        return jsonify({"error": "Password must be at least 6 characters long"}), 400
    user = users.create(data['username'], password)
    return jsonify({'id': user.id, 'username': user.username}), 201

@bp.route('/login', methods=['POST'])
def login_user():
    data = request.json
    user_id = users.get_user(data["username"], data["password"])
    if not user_id:
        return jsonify({'error': 'Invalid username or password'}), 401
    return jsonify({'id': user_id}), 200

@bp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = users.read_one(user_id)
    if user:
        return jsonify({'id': user.id, 'username': user.username}), 200
    return jsonify({'error': 'User not found'}), 404
