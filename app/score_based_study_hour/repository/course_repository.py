# Requiring service dependencies
from ..handlers import DatabaseError
from app import db
from ..model import Course
from ..interface import SavePredictInterface


class PredictionRepository: 
    @staticmethod
    def savePredict(predict: SavePredictInterface) -> Course:
        try:
            new_course = Course(predict)

            db.session.add(new_course)
            db.session.commit()

            return new_course
        except Exception as err:
            raise DatabaseError(str(err.orig), status_code=406)

    @staticmethod
    def update(course) -> Course:
        try:
            db.session.add(course)
            db.session.commit()
            return course
        except Exception as err: 
            raise DatabaseError(str(err.orig), status_code=406)

    @staticmethod
    def get_by_id(user_id, course_id) -> Course:
        try:
            return Course.query.filter(Course.course_id == course_id, Course.user_id == user_id).first()
        except Exception as err:
            raise DatabaseError(str(err.orig), status_code=406)

    @staticmethod
    def get_all(user_id) -> Course:
        try:
            return Course.query.filter(Course.user_id == user_id).all()
        except Exception as err:
            raise DatabaseError(str(err.orig), status_code=406)
        