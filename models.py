from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    # password =


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
