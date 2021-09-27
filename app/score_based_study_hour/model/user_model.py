from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column
from sqlalchemy.orm import relationship

from app import db 

class User(db.Model):  # type: ignore
    """The Users Database"""

    __tablename__ = "users"

    id      = Column(UUID(as_uuid=True), primary_key=True)
    courses = relationship('Course', backref='user', lazy=True)
    

    def __init__(self, user_id):
        self.id     = user_id
        

    def __repr__(self):
        return '<id {}>'.format(self.id)