# Requiring service dependencies
from app import db
from ..model import User
from ..handlers import DatabaseError

class UserRepository: 
    @staticmethod
    def saveUser(user_id: str) -> User:
        try:
            new_user = User(user_id)
            db.session.add(new_user)
            db.session.commit()

            return new_user
        except Exception as err:
            raise DatabaseError(str(err.orig), status_code=406)

    def get_by_id(user_id: str) -> User:
        try:
            return User.query.get(user_id)
        except Exception as err:
            raise DatabaseError(str(err.orig), status_code=406)