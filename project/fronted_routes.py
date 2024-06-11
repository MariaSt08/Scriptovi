from flask import Blueprint, render_template

frontend_bp = Blueprint('frontend', __name__)

@frontend_bp.route('/todos')
def todos_page():
    return render_template('todos.html')

@frontend_bp.route('/todos/<int:todo_id>')
def todo_page(todo_id):
    return render_template('todo.html')

@frontend_bp.route('/create_todo')
def create_todo_page():
    return render_template('create_todo.html')

@frontend_bp.route('/users')
def users_page():
    return render_template('users.html')

@frontend_bp.route('/users/<int:user_id>')
def user_page(user_id):
    return render_template('user.html')

@frontend_bp.route('/create_user')
def create_user_page():
    return render_template('create_user.html')