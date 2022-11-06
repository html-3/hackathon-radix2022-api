from flask.views import MethodView

from app.ships.model import Ship

class ShipGeneral(MethodView):
    def post(self, **kwargs):
        pass

    def get(self, **kwargs):
        return Ship.query.all()

class ShipSpecific(MethodView):

    def get(self, **kwargs):
        pass

    def patch(self, **kwargs):
        pass

    def delete(self, **kwargs):
        pass