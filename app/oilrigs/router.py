from flask import Blueprint
from app.oilrigs.controller import OilRigGeneral, OilRigSpecific

oilrig_router = Blueprint("oilrig_router", __name__)

oilrig_router.add_url_rule(
    "/oilrigs",
    view_func=OilRigGeneral.as_view("oilrigs"), 
    methods = ["GET", "POST"]
)

oilrig_router.add_url_rule(
    "/oilrig/<int:oilrig_id>",
    view_func=OilRigSpecific.as_view("oilrig"), 
    methods = ["GET"]
)