from flask import Blueprint
from auth.controller import Login, RequestPasswordReset, PasswordReset

auth_api = Blueprint("auth_api", __name__)

auth_api.add_url_rule(
    "/login",
    view_func=Login.as_view("login"), 
    methods = ["POST"]
)

auth_api.add_url_rule(
    "/request-pw-reset",
    view_func=RequestPasswordReset.as_view("request-pw-reset"), 
    methods = ["POST"]
)

auth_api.add_url_rule(
    "/pw-reset",
    view_func=PasswordReset.as_view("pw-reset"), 
    methods = ["POST"]
)