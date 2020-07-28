#!/usr/bin/env python3
import os

from flask import Flask, render_template
from datetime import datetime
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_heroku import Heroku
from flask_login import login_required
from flask_migrate import Migrate
from flask_security import SQLAlchemyUserDatastore, Security, url_for_security

from models import db, Event, User, Role


def create_app():
    app = Flask(__name__, instance_relative_config=True, static_url_path="")

    app.config.from_pyfile("default.py")
    app.config.from_envvar("APP_CONFIG_FILE", silent=True)

    db.init_app(app)

    migrate = Migrate(compare_type=True)
    migrate.init_app(app, db)

    admin = Admin(app)
    admin.add_view(ModelView(Event, db.session))

    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    security = Security(app, user_datastore)

    heroku = Heroku()
    heroku.init_app(app)

    @app.context_processor
    def inject_now():
        return {'now': datetime.utcnow()}

    # @login_required
    # @app.route('/admin')
    # def admin():
    #     return url_for_security('login')

    @app.route('/')
    @app.route('/index')
    def index():
        events = Event.query.order_by(Event.date.desc()).limit(3)
        return render_template('index.html', events=events)

    @app.route('/our_work')
    def our_work():
        current = "our_work"
        return render_template('our_work.html', current=current)

    return app


if __name__ == "__main__":
    flask_app = create_app()
    port = int(os.environ.get('PORT', 8080))
    flask_app.run(host="0.0.0.0", port=port)
