from app import db


class UserInfo(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    Login = db.Column(db.String(100), nullable=False)
    Name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    Password = db.Column(db.String(50), nullable=False)
