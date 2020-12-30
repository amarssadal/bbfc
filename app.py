#!/usr/bin/env python3
import json
import os

import requests
from flask import Flask, render_template, url_for, request, flash, redirect
from datetime import datetime
from flask_admin import Admin, helpers
from flask_admin.menu import MenuLink
from flask_heroku import Heroku
from flask_migrate import Migrate
from flask_security import SQLAlchemyUserDatastore, Security

from admin import AdminModelView
from instance.default import ADMIN_EMAIL, ADMIN_PASSWORD, LIST_ID
from models import db, Event, User, Role


def create_app():
    app = Flask(__name__, instance_relative_config=True, template_folder="templates", static_url_path="")

    app.config.from_pyfile("default.py")
    app.config.from_envvar("APP_CONFIG_FILE", silent=True)

    heroku = Heroku()
    heroku.init_app(app)

    db.init_app(app)

    migrate = Migrate(compare_type=True)
    migrate.init_app(app, db)

    admin = Admin(app)
    admin.add_view(AdminModelView(Event, db.session))
    admin.add_link(MenuLink(name="Website", endpoint="index"))
    admin.add_link(MenuLink(name="Login", url="/login"))
    admin.add_link(MenuLink(name="Logout", url='/logout'))

    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    security = Security(app, user_datastore)

    @app.context_processor
    def inject_now():
        return {'now': datetime.utcnow()}

    @security.context_processor
    def security_context_processor():
        return dict(
            admin_base_template=admin.base_template,
            admin_view=admin.index_view,
            get_url=url_for,
            h=helpers
        )

    @app.before_first_request
    def create_user():
        role = user_datastore.find_or_create_role("admin")
        if not User.query.filter_by(email=ADMIN_EMAIL).first():
            user = user_datastore.create_user(email=ADMIN_EMAIL, password=ADMIN_PASSWORD)
            user_datastore.add_role_to_user(user, role)
        db.session.commit()

    @app.route('/')
    @app.route('/index')
    def index():
        events = Event.query.order_by(Event.date.desc()).limit(3)
        return render_template('index.html', events=events)

    @app.route('/our_work')
    def our_work():
        current = "our_work"
        return render_template('our_work.html', current=current)

    @app.route('/signup', methods=['POST'])
    def signup():
        email = request.form.get('email')
        api_key = os.environ.get('MAILCHIMP_API_KEY')
        if not api_key or not email:
            flash('Sorry, there was an error during signup. Please come back later and try again!')
            return redirect(url_for('index'))
        server_number = api_key[-4:]
        url = f"https://{server_number}.api.mailchimp.com/3.0/lists/{LIST_ID}/members"
        headers = {'content-type': 'application/json', 'Authorization': f"Basic {api_key}"}
        data = {'email_address': email, 'status': 'subscribed'}
        response = requests.post(url, headers=headers, data=json.dumps(data))
        print(response.status_code)
        if response.ok:
            flash('Thanks for signing up to our newsletter!')
        else:
            flash('Sorry, there was an error during signup. Please come back later and try again!')
        return redirect(url_for('index'))

    return app


if __name__ == "__main__":
    flask_app = create_app()
    port = int(os.environ.get('PORT', 8080))
    flask_app.run(host="0.0.0.0", port=port)
