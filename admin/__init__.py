from flask import Blueprint

# Create blueprint for admin module
admin_bp = Blueprint("admin", __name__, template_folder="templates")

from . import routes
