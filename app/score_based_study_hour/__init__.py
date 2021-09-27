from .model import Course, User
from .schema.course_schema import PredictionSchema  # noqa

BASE_ROUTE = "v1/prediction"


def timetable_routes(api, app, root="api"):
    from .controllers.course_controller import api as timetable_api

    api.add_namespace(timetable_api, path=f"/{root}/{BASE_ROUTE}")
