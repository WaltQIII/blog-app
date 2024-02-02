from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_keys=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    # Add additional fields

class Post(db.Model):
    id = db.Column(db.Integer, primary_keys=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    # Add additional fields