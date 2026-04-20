from flask import Blueprint

# Create blueprint for shop owner module
shop_owner_bp = Blueprint("shop_owner", __name__, template_folder="templates")

from . import routes
