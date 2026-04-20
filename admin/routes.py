from flask import render_template, redirect, url_for
from . import admin_bp
from services import firebase_service as fb

# ---------------- ROUTES ---------------- #

@admin_bp.route("/admin/dashboard")
def dashboard():
    """Super admin dashboard showing all shops and users"""
    shops = fb.get_all_shops()
    customers = fb.get_all_customers()
    queues = fb.get_all_queues()
    return render_template("admin_dashboard.html", shops=shops, customers=customers, queues=queues)

@admin_bp.route("/admin/delete_user/<user_id>")
def delete_user(user_id):
    """Delete a customer account"""
    fb.delete_customer(user_id)
    return redirect(url_for("admin.dashboard"))

@admin_bp.route("/admin/delete_shop/<shop_id>")
def delete_shop(shop_id):
    """Delete a shop account"""
    fb.delete_shop(shop_id)
    return redirect(url_for("admin.dashboard"))
