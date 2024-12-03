from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_db(app):
    db.init_app(app)  # Initialize the SQLAlchemy instance with the app
    with app.app_context():
        from models.all_models import Image  # Import your models
        db.create_all()  # Create tables
