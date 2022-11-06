from app.utils.base import BaseModel
from app.extensions import db
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import text as sa_text
from uuid import uuid4


class Item(BaseModel):
    __tablename__ = 'item'

    transport_id = db.Column(db.String(100), default=lambda: str(uuid4))

    name = db.Column(db.String(200), unique=True)
    height = db.Column(db.Float, nullable=False)
    width = db.Column(db.Float, nullable=False)
    length = db.Column(db.Float, nullable=False)
    weight = db.Column(db.Float, nullable=False)

    bundle_id = db.Column(db.Integer, db.ForeignKey("bundle.id"))
    oilrig_id = db.Column(db.Integer, db.ForeignKey("oilrig.id"))