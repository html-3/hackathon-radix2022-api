from flask import Blueprint
from app.users.controller import UserSpecific

user_router = Blueprint("user_router", __name__)

user_router.add_url_rule(
    "/user",
    view_func=UserSpecific.as_view("user"), 
    methods = ["GET", "POST", "UPDATE", "DELETE"]
)