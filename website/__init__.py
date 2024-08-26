from flask import Flask

def create_app():
    app = Flask(__name__)

    from .view import homeRoute
    app.register_blueprint(homeRoute)

    return app