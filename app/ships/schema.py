from app.extensions import ma
from app.ships.model import Ship

class ShipSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Ship
        load_instance = True
        ordered = True
        strict = False