from flask import jsonify
from flask.views import MethodView

from app.bundles.model import Bundle
from app.bundles.schema import BundleSchema

class BundleGeneral(MethodView):
    def post(self, **kwargs):
        pass

    def get(self, **kwargs):
        schema = BundleSchema()
        return schema.dump(Bundle.query.all())

class BundleSpecific(MethodView):

    def get(self, **kwargs):
        pass

    def patch(self, **kwargs):
        pass

    def delete(self, **kwargs):
        pass