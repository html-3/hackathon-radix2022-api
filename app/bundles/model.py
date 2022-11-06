from uuid import uuid4
from app.utils.base import BaseModel
from app.extensions import db
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import text as sa_text


class Bundle(BaseModel):

    transport_id = db.Column(db.String(100), default=lambda: str(uuid4))

    height = db.Column(db.Float, nullable=False)
    width = db.Column(db.Float, nullable=False)
    length = db.Column(db.Float, nullable=False)
    weight = db.Column(db.Float, nullable=False)

    oilrig_id = db.Column(db.Integer, db.ForeignKey("oilrig.id"))

    items = db.relationship("Item", backref="bundle")
