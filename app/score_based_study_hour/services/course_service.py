# Requring Packages
# from tensorflow.keras.models import load_model
import numpy as np
from typing import List

# Requiring service dependencies
from ..model import Course, User
from ..repository import PredictionRepository, UserRepository
from ..interface import PredictHourInterface, SavePredictInterface
from ..handlers import InvalidPermissions, RecordNotFound, RecordAlreadyExists

class PredictionService:
    @staticmethod
    def hour_predict(predict) -> int:
        # file_name = 'app\prediction_model\Timetable_Prediction_model.h5'

        # model = load_model(os.path.abspath(file_name))
        
        data_prepared = np.array([
            predict["cwa"], 
            predict["credits"],
            predict["course_diff"], 
            predict["pred_score"]            
            ]).reshape(-1,4)

        # pred_study_hour = int(model.predict(data_prepared, verbose=1).reshape(-1, 1)[0][0])
        # return pred_study_hour  

        return 0.5

    @staticmethod
    def score_predict(predict) -> int:
        # file_name = 'app\prediction_model\Timetable_Prediction_model.h5'

        # model = load_model(os.path.abspath(file_name))
        
        data_prepared = np.array([
            predict["cwa"], 
            predict["credits"],
            predict["course_diff"], 
            predict["study_hour"]            
            ]).reshape(-1,4)

        # pred_score = int(model.predict(data_prepared, verbose=1).reshape(-1, 1)[0][0])
        # return pred_score  

        return 0.8

    @staticmethod
    def predict(predict : PredictHourInterface):
        if 'study_hour' in predict.keys(): 
            predict['pred_score'] = PredictionService.score_predict(predict)
            return predict

        if 'pred_score' in predict.keys(): 
            predict['study_hour'] = PredictionService.hour_predict(predict)
            return predict

    @staticmethod
    def createPredict(predict: SavePredictInterface):
        try:
            user = UserRepository.get_by_id(predict['user_id'])
            if not user: user = UserRepository.saveUser(predict["user_id"])
            course = PredictionRepository.get_by_id(predict['user_id'], predict['course_id'])
            if course: raise RecordAlreadyExists('Course already exist for user')
            
            predict['act_score'] = None
            predict['user'] = user
            
            del predict['user_id']
            savedPredict = PredictionRepository.savePredict(predict)

            return savedPredict

        except Exception as err: raise err   
    
    @staticmethod
    def update(predict):
        try:
            user = UserRepository.get_by_id(predict['user_id'])
            if not user: raise RecordNotFound('User not found')
            course = PredictionRepository.get_by_id(user.id, predict['course_id'])
            if not course: raise RecordNotFound('Course not found')
            if (course.act_score != None): raise InvalidPermissions('Data Restricted', status_code=451)

            course.act_score = None
            if 'act_score' in predict.keys(): course.act_score = predict['act_score']
    
            course.cwa          = predict['cwa']
            course.credits      = predict['credits']
            course.course_diff  = predict['course_diff']
            course.pred_score   = predict['pred_score']
            course.study_hour   = PredictionService.predict(predict)

            return PredictionRepository.update(course)
            
        except Exception as err: raise err  

    @staticmethod
    def get_all(user) -> List[Course]:
        try:
            user_id = user['auth']
            courses = PredictionRepository.get_all(user_id)

            return courses

        except Exception as err: raise err


    @staticmethod
    def get_courseid(course_id, user) -> Course:
        try:
            if user['auth'] != user['param']: raise InvalidPermissions('User does not match')
            user_id = user['auth']
            course = PredictionRepository.get_by_id(user_id, course_id)
            if course is None: raise RecordNotFound('Course not found')
            
            return course

        except Exception as err: raise err 