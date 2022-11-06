from flask import jsonify
from flask.views import MethodView

from app.oilrigs.model import OilRig
from app.oilrigs.schema import OilRigSchema

class OilRigGeneral(MethodView):
    def post(self, **kwargs):
        pass

    def get(self, **kwargs):
        schema = OilRigSchema()
        print(jsonify(schema.dump(OilRig.query.all())))
        return jsonify(schema.dump(OilRig.query.all()))

class OilRigSpecific(MethodView):

    def get(self, **kwargs):
        pass

    def patch(self, **kwargs):
        pass

    def delete(self, **kwargs):
        pass