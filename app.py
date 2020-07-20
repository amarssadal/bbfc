#!/usr/bin/env python3

from flask import Flask, render_template
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_migrate import Migrate

from models import db, Event


def create_app():
    app = Flask(__name__, instance_relative_config=True, static_url_path="")

    app.config.from_pyfile("default.py")
    app.config.from_envvar("APP_CONFIG_FILE", silent=True)

    db.init_app(app)

    migrate = Migrate(compare_type=True)
    migrate.init_app(app, db)

    admin = Admin(app)
    admin.add_view(ModelView(Event, db.session))

    @app.route('/')
    @app.route('/index')
    def index():
        events = Event.query.all()
        return render_template('index.html', events=events)

    @app.route('/our_work')
    def our_work():
        current = "our_work"
        return render_template('our_work.html', current=current)

    return app


if __name__ == "__main__":
    flask_app = create_app()
    flask_app.run(host="0.0.0.0", port=8080, debug=True)
