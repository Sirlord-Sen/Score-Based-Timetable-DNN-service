from ..interface import PredictionInterface
from ..schema.course_schema import PredictionSchema


def scalePredict(predict: PredictionInterface):
    predict['cwa']          = predict["cwa"]/100
    predict['credits']      = predict["credits"]/30
    predict['course_diff']  = predict["course_diff"]/10
    if 'study_hour' in predict.keys(): predict['study_hour']   = predict["study_hour"]/10
    if 'pred_score' in predict.keys(): predict['pred_score']   = predict["pred_score"]/100
    if 'act_score' in predict.keys(): predict['act_score'] = predict['act_score']/100

    return predict

def upScale(predict: PredictionInterface):
    # pred_schema = PredictionSchema()
    # predict = pred_schema.dump(data)
    predict['cwa']          = predict["cwa"] * 100
    predict['credits']      = predict["credits"]*30
    predict['course_diff']  = predict["course_diff"]*10
    predict['study_hour']   = predict["study_hour"]*10
    predict['pred_score']   = predict["pred_score"]*100
    if 'act_score' in predict.keys(): 
        predict['act_score'] = predict['act_score']*100
    
    else:
        predict['act_score'] = None

    return predict

def buildResponse(data):
    pred_schema = PredictionSchema()
    pred_dict = pred_schema.dump(data)

    pred_dict = upScale(pred_dict)
    response = {
        'message': 'success',
        'data': {
            "user": {
                "id": pred_dict['user_id'],
                'cwa': pred_dict['cwa'],
                "course": {
                    'id': pred_dict['course_id'],
                    'credits': pred_dict['credits'],
                    'course_diff': pred_dict['course_diff'],
                    'pred_score': pred_dict['pred_score'],
                    'study_hour': pred_dict['study_hour'],
                    'act_score': pred_dict['act_score']
                }
            }
        }
    }
    return response


def buildRes(data):

    pred_schema = PredictionSchema(many=True)
    pred_dict = pred_schema.dump(data) 

    array = []
    for x in pred_dict:
        x = upScale(x)
        obj = {
                'id': x['course_id'],
                'credits': x['credits'],
                'course_diff': x['course_diff'],
                'pred_score': x['pred_score'],
                'study_hour': x['study_hour'],
                'cwa': x['cwa'],
                'act_score': x['act_score']
            }
        array.append(obj)

    response = {
        'message': 'success',
        'data': {
            "user": {
                "id": pred_dict[0]['user_id'],
                "courses": array
            }
        }
    }

    return response
