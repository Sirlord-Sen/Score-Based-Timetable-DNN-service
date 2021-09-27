from flask import Flask, redirect
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
import os

from config.config import config_by_name
from .routes import timetable_routes


db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.config['JSON_SORT_KEYS'] = False
    app.config.from_object(config_by_name[config_name])
    api = Api(app, title="Prediction API", version="0.1.0")

    db.init_app(app)

    # from .score_based_study_hour.middlewares import AuthMiddleware
    from .score_based_study_hour.middlewares import after_request_middleware, before_request_middleware
    from .score_based_study_hour.middlewares import response_middleware as response

    before_request_middleware(app=app)
    after_request_middleware(app=app)
    
    # register custom error handler
    response.json_error_handler(app=app)

    @app.route('/')
    def index(): return     
    
    # Using routes
    timetable_routes(api, app)                     

    return app




