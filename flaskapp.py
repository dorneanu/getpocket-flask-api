from flask import Flask


def create_app():
    """ Flask app factory """
    app = Flask(__name__)
    app.config.from_envvar('FLASK_CONFIG_FILE')
    return app
