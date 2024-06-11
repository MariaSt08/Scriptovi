from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=True, nullable=False)
    def __repr__(self):
        return f'<User {self.username}>'

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(120), nullable=True)
    done = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    user = db.relationship('User', backref=db.backref('todos', lazy=True))

    def __repr__(self):
        return f'<Todo {self.title}>'

class Todos:
        @staticmethod
        def create(title, description, user_id=None):
            new_todo = Todo(title=title, description=description, user_id=user_id)
            db.session.add(new_todo)
            db.session.commit()
            return new_todo

        @staticmethod
        def read_all(user_id=None):
            if user_id:
                return Todo.query.filter_by(user_id=user_id).all()
            return Todo.query.all()


        @staticmethod
        def read_one(todo_id):
            return Todo.query.get(todo_id)

        @staticmethod
        def update(todo_id, title=None, description=None, done=None):
            todo = Todo.query.get(todo_id)
            if todo:
                if title is not None:
                    todo.title = title
                if description is not None:
                    todo.description = description
                if done is not None:
                    todo.done = done
                db.session.commit()
                return todo
            return None

        @staticmethod
        def delete(todo_id):
            todo = Todo.query.get(todo_id)
            if todo:
                db.session.delete(todo)
                db.session.commit()
                return True
            return False

class Users:
        @staticmethod
        def create(username):
            new_user = User(username=username)
            db.session.add(new_user)
            db.session.commit()
            return new_user

        @staticmethod
        def read_all():
            return User.query.all()

        @staticmethod
        def read_one(user_id):
            return User.query.get(user_id)

users = Users
todos = Todos