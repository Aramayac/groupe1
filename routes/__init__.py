import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # Chemin vers la base SQLite dans le dossier instance
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.secret_key = "supersecret"

    db.init_app(app)

    # Import et enregistrement du Blueprint
    from routes.user_routes import user_bp
    app.register_blueprint(user_bp, url_prefix="/users")

    # Crée la base si elle n’existe pas
    with app.app_context():
        db.create_all()

    return app
