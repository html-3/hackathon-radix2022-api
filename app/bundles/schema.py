from app.extensions import ma
from app.bundles.model import Bundle

class BundleSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Bundle
        load_instance = True
        ordered = True
        strict = False