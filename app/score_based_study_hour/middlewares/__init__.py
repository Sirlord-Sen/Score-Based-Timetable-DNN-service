# from .auth_middleware import AuthMiddleware

from . import request_middleware as request
from . import auth_middleware as auth

def before_request_middleware(app):
    app.before_request_funcs.setdefault(None, [
        request.ensure_content_type,
        request.ensure_public_unavailability,
        auth.authenticate_user
    ])

def after_request_middleware(app):
    app.after_request_funcs.setdefault(None, [
        request.enable_cors
    ])

