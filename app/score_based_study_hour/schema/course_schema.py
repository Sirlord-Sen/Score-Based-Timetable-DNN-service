from marshmallow import Schema
from marshmallow.fields import UUID, Number

class PredictionSchema(Schema):
    """The Prediction Schema"""
    id = Number(attribute = 'id', required= False)
    user_id = UUID(attribute='user_id')
    cwa = Number(attribute="cwa")
    course_id = UUID(attribute='course_id')
    credits = Number(attribute="credits")
    course_diff = Number(attribute="course_diff")
    pred_score = Number(attribute="pred_score")
    study_hour = Number(attribute="study_hour", required=False)

class UpdatePredSchema(Schema):
    """The Update Prediction Schema"""
    user_id = UUID(attribute='user_id')
    cwa = Number(attribute="cwa")
    credits = Number(attribute="credits")
    course_diff = Number(attribute="course_diff")
    pred_score = Number(attribute="pred_score")
    act_score = Number(attribute = "act_score", required=False)
