from flask import Blueprint

# Create blueprint for customer module
customer_bp = Blueprint("customer", __name__, template_folder="templates")

from . import routes
