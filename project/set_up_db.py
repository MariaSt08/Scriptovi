from flask import Flask
from config import Config
from db import db

def init_db():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        db.create_all()
        print("Database initialized.")
print(__name__)
if __name__ == '__main__':
    init_db()