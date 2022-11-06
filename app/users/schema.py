from app.extensions import ma
from users.model import User
from marshmallow import EXCLUDE, post_dump, pre_load, validates
from flask import make_response

class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User
        load_instance = True
        ordered = True
        unknown = EXCLUDE
        strict = False

    id =  ma.Integer(dump_only=True)
    
    username = ma.String(required=True)
    email = ma.Email(required=True)
    pw = ma.String(required=True, load_only=True)

    name = ma.String(required=True)
    surname = ma.String(required=True)

    status = ma.String(dump_only=True)
    user_type = ma.String(dump_only=True)
    updated_at  = ma.DateTime(dump_only=True) 
    created_at  = ma.DateTime(dump_only=True) 

    #posts = ma.Nested("PostSchema", only=["id", "title", "updated_at"], many=True, dump_only=True)
    
    @pre_load 
    def pre_check(self, data, **kwargs):
        return data

    @validates("name") 
    def validate_name(self, name : str):
        # Zero length name
        if len(name) == name.count(" ") or len(name) >= 100:
            make_response(400, "Invalid name length, should be between 0 and 100")

    @validates("surname") 
    def validate_surname(self, surname : str):
        # Zero length surname
        if len(surname) == surname.count(" ") or len(surname) >= 100:
            make_response(400, "Invalid surname length, should be between 0 and 100")

    @validates("username") 
    def validate_username(self, username : str):
        # Zero length username
        if len(username) == username.count(" ") or len(username) >= 100:
            make_response(400, "Invalid username length, should be between 0 and 100")

    @validates("pw") 
    def validate_pw(self, pw : str):
        # Zero length pw
        if len(pw) == pw.count(" ") or len(pw) >= 100:
            make_response(400, "Invalid password length, should be between 0 and 100")    