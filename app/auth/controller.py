from datetime import timedelta
from flask import request
from flask.views import MethodView
from flask_jwt_extended import create_access_token, create_refresh_token

from app.auth.schema import LoginSchema
from app.users.model import User


class Login(MethodView):
    
    def post(self):
        schema = LoginSchema()
        data = schema.load(request.json)

        user = User.query.filter_by(email=data.get("email")).first()

        token = create_access_token(    
            identity=user.id, 
            expires_delta=timedelta(hours=3), 
            fresh=True,
            additional_claims={"user_type" : user.user_type}
            )

        refresh_token = create_refresh_token(
            identity=user.id, 
            expires_delta=timedelta(hours=6),
            additional_claims={"user_type" : user.user_type}
            )

        return {    
                "user_type": user.user_type,
                "name": user.name,
                "id" : user.id,
                "token": token,
                "refresh_token": refresh_token
            }


class RequestPasswordReset(MethodView):
    
    def post(self, **kwargs):
        pass

class PasswordReset(MethodView):
    
    def post(self, **kwargs):
        pass