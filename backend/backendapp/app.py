from flask import Flask

from backendapp import db
from backendapp.errorhandling import define_error_handlers_for
from backendapp.movies import bp as movies_bp


def create_app(test_config=None,
               secret_key="dev"):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY=secret_key,
    )

    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)

    app.register_blueprint(movies_bp)
    db.init_app(app)
    define_error_handlers_for(app)

    return app
