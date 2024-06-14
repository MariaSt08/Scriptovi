from flask import Flask
from db import db
from fronted_routes import frontend_bp
from api_routes import bp
from config import Config
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    app.register_blueprint(frontend_bp)
    app.register_blueprint(bp, url_prefix="/api")
    with app.app_context():
        db.create_all()

    return app




app = create_app()

if __name__ == '__main__':
    app.run(debug=True)