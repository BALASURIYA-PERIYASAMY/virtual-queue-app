from flask import render_template, request, redirect, url_for, jsonify
from . import customer_bp
from . import services as customer_services

# ---------------- ROUTES ---------------- #

@customer_bp.route("/dashboard/<user_id>")
def dashboard(user_id):
    """Customer dashboard"""
    data = customer_services.get_customer_dashboard(user_id)
    return render_template("customer_dashboard.html", user=data["user"], recent=data["recent"])

@customer_bp.route("/queue/join/<shop_id>/<user_id>")
def join_queue(shop_id, user_id):
    """Join shop queue"""
    status = customer_services.join_queue(shop_id, user_id)
    return render_template("join_queue.html", shop_id=shop_id, status=status)

@customer_bp.route("/queue/status/<user_id>")
def view_status(user_id):
    """View customer’s current queue status"""
    status = customer_services.get_status(user_id)
    return render_template("view_status.html", status=status)

@customer_bp.route("/profile/<user_id>", methods=["GET", "POST"])
def profile(user_id):
    """View / Update profile"""
    if request.method == "POST":
        name = request.form["name"]
        phone = request.form["phone"]
        customer_services.update_profile(user_id, {"name": name, "phone": phone})
        return redirect(url_for("customer.profile", user_id=user_id))

    user = customer_services.get_profile(user_id)
    return render_template("profile.html", user=user)
