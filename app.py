#!/usr/bin/env python3

from flask import Flask, render_template
from datetime import datetime

def create_app():
    app = Flask(__name__, instance_relative_config=True, static_url_path="")

    app.config.from_pyfile("default.py")
    app.config.from_envvar("APP_CONFIG_FILE", silent=True)

    @app.context_processor
    def inject_now():
        return {'now': datetime.utcnow()}

    @app.route('/')
    @app.route('/index')
    def index():
        return render_template('index.html')

    @app.route('/our_work')
    def our_work():
        current = "our_work"
        return render_template('our_work.html', current = current)

    return app

if __name__ == "__main__":
    flask_app = create_app()
    flask_app.run(host="0.0.0.0", port=8080, debug=True)
