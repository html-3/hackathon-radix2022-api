from flask import Blueprint
from app.bundles.controller import BundleGeneral, BundleSpecific

bundle_router = Blueprint("bundle_router", __name__)

bundle_router.add_url_rule(
    "/bundles",
    view_func=BundleGeneral.as_view("bundles"), 
    methods = ["GET", "POST"]
)

bundle_router.add_url_rule(
    "/bundle/<int:bundle_id>",
    view_func=BundleSpecific.as_view("bundle"), 
    methods = ["GET"]
)