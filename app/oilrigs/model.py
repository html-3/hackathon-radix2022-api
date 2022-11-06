from uuid import uuid4
from app.utils.base import BaseModel
from app.extensions import db
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import text as sa_text


class OilRig(BaseModel):
    __tablename__ = 'oilrig'

    transport_id = db.Column(db.String(100), default=lambda: str(uuid4))

    name = db.Column(db.String(200), unique=True)
    width = db.Column(db.Float, nullable=False)
    length = db.Column(db.Float, nullable=False)
    weight = db.Column(db.Float, nullable=False)

    items = db.relationship("Item", backref="oilrig")
    bundles = db.relationship("Bundle", backref="oilrig")