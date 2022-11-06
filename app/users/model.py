from app.utils.base import BaseModel
from app.extensions import db
import bcrypt


class User(BaseModel):
    __tablename__ = 'user'

    username = db.Column(db.String(100), unique=True)
    email = db.Column(db.String(100), unique=True)

    name = db.Column(db.String(100))
    surname = db.Column(db.String(100))

    pw_hash = db.Column(db.LargeBinary(128), nullable=False)

    user_type = db.Column(db.String(100))
    status = db.Column(db.String(100))

    #posts = db.relationship("Post", backref="user")

    @staticmethod
    def verify_token(self, token):

        try:
            data = bcrypt.decode_token(token)
        except:
            return None

        user = self.query.get(data.get("identity"))

        return user

    def verify_pw(self, pw: str) -> bool:
        return bcrypt.checkpw(pw.encode(), self.pw_hash)