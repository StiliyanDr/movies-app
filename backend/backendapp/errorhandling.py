from flask import jsonify
from pydantic.error_wrappers import ValidationError


def define_error_handlers_for(app):
    @app.errorhandler(404)
    def resource_not_found(e):
        """
        An error-handler to ensure that 404 errors are returned as JSON.
        """
        return (jsonify(error=str(e)), 404)

    @app.errorhandler(500)
    def internal_server_error(e):
        """
        An error-handler to ensure that 500 errors are returned as JSON.
        """
        return (jsonify(error=str(e)), 500)

    @app.errorhandler(ValidationError)
    def validation_error(e):
        """
        An error-handler to ensure that request validation errors are
        returned as JSON.
        """
        return (jsonify(error=str(e)), 400)
