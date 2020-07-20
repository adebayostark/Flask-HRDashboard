from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db, bcrypt, login


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(128), nullable=False)
    last_name = db.Column(db.String(128), nullable=False)
    my_id = db.Column(db.String(128), nullable=False, unique=True)
    password_hash = db.Column(db.String(255), nullable=False)
    creation_date = db.Column(db.DateTime, nullable=False,
        default=datetime.utcnow)
    active = db.Column(db.Boolean())
    is_admin = db.Column(db.Boolean())

    def get_id(self):
        return self.id
    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password,10).decode('utf8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)   

    def __repr__(self):
        return '<User #%s:%s>' % (self.id, self.email)

    

@login.user_loader
def load_user(id):
    return User.query.get(int(id))