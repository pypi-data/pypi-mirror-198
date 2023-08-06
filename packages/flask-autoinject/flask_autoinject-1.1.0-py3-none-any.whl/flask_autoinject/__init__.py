import flask
from autoinject import injector
from .contexts import FlaskContextInformant


def init_app(app: flask.Flask):
    """Initialize the Flask context handling."""
    fci = FlaskContextInformant()
    injector.register_informant(fci)

    @app.teardown_appcontext
    def clean_context(exc=None):
        fci.destroy_self()

__version__ = "1.1.0"
