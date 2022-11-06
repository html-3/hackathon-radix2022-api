from flask import make_response
from flask_jwt_extended import get_jwt, get_jwt_identity, verify_jwt_in_request
from app.users.model import User

# Recieves decorator arguments
def permission(permited : list = []):
    
    # Recieves function
    def wrapper_1(func):

        # Recieves function arguments
        def wrapper_2(*args, **kwargs):
            verify_jwt_in_request()
            claim = get_jwt()
            id = get_jwt_identity()
            user = User.query.get(id)
            user_type = user.user_type

            if not user_type in permited:
                make_response("User not authorized", 403)

            kwargs["id"] = id
            kwargs["user_type"] = user_type
            kwargs["name"] = user.name

            return func(*args, **kwargs)

        return wrapper_2

    return wrapper_1