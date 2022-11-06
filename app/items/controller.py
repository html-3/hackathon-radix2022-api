from flask import request
from flask.views import MethodView

from app.items.model import Item
from app.items.schema import ItemSchema

class ItemGeneral(MethodView):
    def post(self, **kwargs):
        schema = ItemSchema
        item = schema.load(request.json)

        item.create()

        return item

    def get(self, **kwargs):
        schema = ItemSchema()
        return schema.dump(Item.query.all())

class ItemSpecific(MethodView):

    def get(self, **kwargs):
        pass

    def patch(self, **kwargs):
        pass

    def delete(self, **kwargs):
        pass