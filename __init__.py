from flask import Flask


def create_app():
    app = Flask(__name__)

    from .app import index_blueprint, history_blueprint
    app.register_blueprint(index_blueprint)
    app.register_blueprint(history_blueprint)

    return app
