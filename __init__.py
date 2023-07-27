from flask import Flask


def create_app():
    """
    Function to run a application
    """
    app = Flask(__name__)

    from .app import index_blueprint, history_blueprint
    app.register_blueprint(index_blueprint)
    app.register_blueprint(history_blueprint)

    return app
