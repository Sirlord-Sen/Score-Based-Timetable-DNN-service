from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Integer, Column, ForeignKey, Float

from app import db 

class Course(db.Model):  # type: ignore
    """The course database"""

    __tablename__ = "courses"

    id          = Column(Integer(), primary_key=True, autoincrement=True)
    course_id   = Column(UUID(as_uuid=True))
    cwa         = Column(Float())
    credits     = Column(Float())
    course_diff = Column(Float())
    pred_score  = Column(Float())
    act_score   = Column(Float(), nullable = True)
    study_hour  = Column(Float())
    user_id     = Column(UUID(as_uuid=True), ForeignKey('users.id'))

    def __init__(self, predict):
        self.course_id      = predict['course_id']
        self.cwa            = predict['cwa']
        self.credits        = predict['credits']
        self.course_diff    = predict['course_diff']
        self.pred_score     = predict['pred_score']
        self.act_score      = predict['act_score']
        self.study_hour     = predict['study_hour']
        self.user           = predict['user']
        

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def update(self, changes):
        for key, val in changes.items():
            setattr(self, key, val)
        return self
