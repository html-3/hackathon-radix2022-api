from app.extensions import ma
from app.oilrigs.model import OilRig

class OilRigSchema(ma.SQLAlchemySchema):
    class Meta:
        model = OilRig
        load_instance = True
        ordered = True
        strict = False
