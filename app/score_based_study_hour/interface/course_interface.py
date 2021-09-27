from marshmallow.fields import UUID
from mypy_extensions import TypedDict


class CourseInterface(TypedDict):
    cwa         = int
    credits     = int
    course_diff = int
    pred_score  = int
    act_score   = int
    study_hour  = int
    student_id  = int

class PredictionInterface(TypedDict):
    cwa         = int
    credits     = int
    course_diff = int
    pred_score  = int

class PredictHourInterface(TypedDict):
    cwa         = int
    credits     = int
    course_diff = int
    pred_score  = int
    student_id  = int
    user_id     = str
    course_id   = str

class SavePredictInterface(TypedDict): 
    cwa         = int
    credits     = int
    course_diff = int
    pred_score  = int
    student_id  = int
    user_id     = str
    course_id   = str

class PredictPayload(TypedDict):
    predicted_score: int

class BuildPredictResponse(TypedDict):
    message: str
    user: str
    data: SavePredictInterface