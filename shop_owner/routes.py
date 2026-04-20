from flask import render_template, request, redirect, url_for
from . import shop_owner_bp
from . import services as shop_services

# ---------------- ROUTES ---------------- #

@shop_owner_bp.route("/shop/dashboard/<shop_id>")
def dashboard(shop_id):
    """Shop owner dashboard"""
    data = shop_services.get_shop_dashboard(shop_id)
    return render_template("shop_dashboard.html", shop=data["shop"], queues=data["queues"])

@shop_owner_bp.route("/shop/queue/<shop_id>")
def manage_queue(shop_id):
    """View and manage current queue"""
    queue_list = shop_services.get_queue(shop_id)
    return render_template("manage_queue.html", queue=queue_list, shop_id=shop_id)

@shop_owner_bp.route("/shop/appointments/<shop_id>")
def manage_appointments(shop_id):
    """View & approve/reject appointments"""
    appointments = shop_services.get_appointments(shop_id)
    return render_template("manage_appointments.html", appointments=appointments, shop_id=shop_id)

@shop_owner_bp.route("/shop/appointments/update/<shop_id>/<appointment_id>/<action>")
def update_appointment(shop_id, appointment_id, action):
    """Approve or reject an appointment"""
    shop_services.update_appointment(appointment_id, action)
    return redirect(url_for("shop_owner.manage_appointments", shop_id=shop_id))

@shop_owner_bp.route("/shop/profile/<shop_id>", methods=["GET", "POST"])
def profile(shop_id):
    """View / Update shop profile"""
    if request.method == "POST":
        name = request.form["name"]
        category = request.form["category"]
        shop_services.update_profile(shop_id, {"name": name, "category": category})
        return redirect(url_for("shop_owner.profile", shop_id=shop_id))

    shop = shop_services.get_profile(shop_id)
    return render_template("shop_profile.html", shop=shop)
