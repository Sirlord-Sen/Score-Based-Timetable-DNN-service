from marshmallow.fields import UUID
from mypy_extensions import TypedDict

class UserInterface(TypedDict):
    user_id = str