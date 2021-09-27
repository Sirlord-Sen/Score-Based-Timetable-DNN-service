from flask import request, jsonify, g 
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource
from marshmallow.fields import UUID


from ..schema.course_schema import PredictionSchema, UpdatePredSchema
from ..services.course_service import PredictionService
from ..interface import BuildPredictResponse
from ..handlers import scalePredict, buildResponse, buildRes

api = Namespace("Course", description="Single namespace, single entity")


@api.route("/users/<user_id>/courses")
@api.param("user_id", "User database ID")
class PredictionController(Resource):
    """Timetable"""
    @responds(schema=PredictionSchema(many=True))
    def get(self, user_id: UUID):
        """Get all Courses"""
        user = {'param': user_id, 'auth': g.user_id}
        courses = PredictionService.get_all(user)
        response = buildRes(courses)
        
        return jsonify(response)


    @accepts(schema=PredictionSchema, api=api)
    @responds(schema=PredictionSchema)
    def post(self, user_id: UUID) -> BuildPredictResponse:
        """Creating Single Timetable"""
        predict             = request.parsed_obj
        predict['user_id']  = g.user_id
        scale_predict       = scalePredict(predict)
        predicted           = PredictionService.predict(scale_predict)
        saved_pred          = PredictionService.createPredict(predicted)
        response            = buildResponse(saved_pred)
        
        return jsonify(response)
        
    
@api.route("/users/<user_id>/courses/<course_id>")
@api.param("user_id", "Course database ID")
@api.param("course_id", "Course database ID")
class CourseIdController(Resource):
    @responds(schema=PredictionSchema)
    def get(self, user_id: UUID, course_id: UUID):
        """Get Single Timetable"""
        user    = {'param': user_id, 'auth': g.user_id}
        course  = PredictionService.get_courseid(course_id, user)
        response = buildResponse(course)
        
        return jsonify(response)
        
        
    @accepts(schema=UpdatePredSchema, api=api)
    @responds(schema=UpdatePredSchema)
    def put(self, user_id: UUID, course_id: UUID):
        """Update Single Timetable"""
        changes             = request.parsed_obj
        changes['user_id']  = g.user_id
        changes['course_id']= course_id
        scale_change        = scalePredict(changes)
        updated             = PredictionService.update(scale_change)
        response            = buildResponse(updated)

        return jsonify(response)
