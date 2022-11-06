import re
from flask import make_response
from app.extensions import ma
from marshmallow import EXCLUDE, pre_load

class LoginSchema(ma.Schema):
    class Meta:
        unknown = EXCLUDE

    email = ma.Email(load_only=True, required=True)
    pw = ma.String(load_only=True, required=True)

    @pre_load
    def pre_check(self, data, **kwargs):

        regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"

        if not (isinstance(data.get("pw", ""),str) and isinstance(data.get("email", ""),str)):
            make_response(400,"Senha ou e-mail incorretos!")

        if not re.fullmatch(regex, data.get("email", "")):
            make_response(400, "Insira seu e-mail para fazer login!")
        if not isinstance(data.get("pw",1),str) or not isinstance(data.get("email",1),str):
            make_response(400,"Senha ou e-mail incorretos!")
        return data

class RequerstPassowordResetSchema(ma.Schema):
    class Meta:
        unknown = EXCLUDE

    email = ma.Email(load_only=True, required=True)

class PassowordResetSchema(ma.Schema):
    class Meta:
        unknown = EXCLUDE

    pw = ma.String(load_only=True, required=True)