from werkzeug.exceptions import Conflict, NotFound, Unauthorized, InternalServerError


class JSONException(Exception):
    """Custom JSON based exception.
    :param status_code: response status_code
    :param message: exception message
    """
    status_code = NotFound.code
    message = ''

    def __init__(self, message,status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        return {
            'status': 'error',
            'message': self.message,
            'code': self.status_code,
            'type': str(self.__class__.__name__)
        }

class InvalidContentType(JSONException):
    """Raised when an invalid Content-Type is provided."""
    pass


class InvalidPermissions(JSONException):
    status_code = Unauthorized.code


class InvalidAPIRequest(JSONException):
    """
    Raised when an invalid request has been made.
    (e.g. accessed unexisting url, the schema validation did
    not pass)
    """
    pass


class DatabaseError(JSONException):
    """Database Errors"""
    pass


class RecordNotFound(DatabaseError):
    """Raised when the record was not found in the database."""
    pass


class RecordAlreadyExists(DatabaseError):
    """Raised in the case of violation of a unique constraint."""
    status_code = Conflict.code


class InternalServerError(JSONException):
    status_code = InternalServerError.code