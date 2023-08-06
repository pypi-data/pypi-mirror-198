"""Context handler for Flask."""
import flask
import uuid
from autoinject.informants import ContextInformant


class FlaskContextInformant(ContextInformant):
    """Provides a unique identifier for each request to the context manager."""

    def __init__(self):
        super().__init__("flask")

    def destroy_self(self):
        if flask.has_app_context() and hasattr(flask.g, "autoinject_id"):
            self.destroy(flask.g.autoinject_id)

    def get_context_id(self) -> str:
        """Provide a unique ID to the context manager."""
        if flask.has_app_context():
            if not hasattr(flask.g, "autoinject_id"):
                flask.g.autoinject_id = str(uuid.uuid4())
            return flask.g.autoinject_id
        return ""
