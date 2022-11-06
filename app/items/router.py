from flask import Blueprint
from app.items.controller import ItemGeneral, ItemSpecific

item_router = Blueprint("item_router", __name__)

item_router.add_url_rule(
    "/items",
    view_func=ItemGeneral.as_view("items"), 
    methods = ["GET", "POST"]
)

item_router.add_url_rule(
    "/item/<int:item_id>",
    view_func=ItemSpecific.as_view("item"), 
    methods = ["GET"]
)