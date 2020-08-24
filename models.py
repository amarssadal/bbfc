import os

from flask_login import UserMixin
from flask_security import RoleMixin
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(80))
    active = db.Column(db.Boolean())
    roles = db.relationship('Role', secondary='user_roles', backref='user', lazy=True)


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))


class UserRoles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id", ondelete="CASCADE"))
    role_id = db.Column(db.Integer, db.ForeignKey("role.id", ondelete="CASCADE"))


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    date = db.Column(db.DateTime)
    duration = db.Column(db.Time)
    description = db.Column(db.String)
    image = db.Column(db.String)
    location = db.Column(db.String)

    @property
    def day_and_month(self):
        if self.date:
            return self.date.strftime("%d %B")

    @property
    def image_url(self):
        return os.path.join('/events', self.image)
