from app.extensions import ma
from app.items.model import Item

class ItemSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Item
        load_instance = True
        ordered = True
        strict = False