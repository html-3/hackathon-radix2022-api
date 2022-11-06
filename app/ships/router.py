from flask import Blueprint
from app.ships.controller import ShipGeneral, ShipSpecific

ship_router = Blueprint("ship_router", __name__)

ship_router.add_url_rule(
    "/ships",
    view_func=ShipGeneral.as_view("ships"), 
    methods = ["GET"]
)

ship_router.add_url_rule(
    "/ship/<int:ship_id>",
    view_func=ShipSpecific.as_view("ship"), 
    methods = ["GET"]
)