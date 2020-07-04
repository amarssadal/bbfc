#!/usr/bin/env python3

from flask import Flask, render_template


def create_app():
    app = Flask(__name__, instance_relative_config=True, static_url_path="")

    app.config.from_pyfile("default.py")
    app.config.from_envvar("APP_CONFIG_FILE", silent=True)

    @app.route('/')
    def index():
        return render_template('index.html')
    return app


if __name__ == "__main__":
    flask_app = create_app()
    flask_app.run(host="0.0.0.0", port=80, debug=True)
