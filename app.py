from flask import Flask, render_template, request, redirect, url_for, jsonify
from services import firebase_service as fb, maps_service, queue_service, notification_service

app = Flask(__name__)

# ---------------- ROUTES ---------------- #

# Home / Index page
@app.route('/')
def index():
    shops = fb.get_shops()
    return render_template("index.html", shops=shops)

# Login page
@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        # In real case, verify password client-side or with Firebase SDK
        user = fb.login_user(email)
        if user:
            return redirect(url_for("index"))
        return render_template("login.html", error="Invalid login")
    return render_template("login.html")

# Register page
@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        name = request.form["name"]

        user_data = {"email": email, "name": name, "role": "customer"}
        uid = fb.register_user(email, password, user_data)
        return redirect(url_for("login"))
    return render_template("register.html")

# About page
@app.route('/about')
def about():
    return render_template("about.html")

# Contact page
@app.route('/contact')
def contact():
    return render_template("contact.html")

# Map API / Nearby shops
@app.route('/map')
def map_view():
    lat, lng = request.args.get("lat"), request.args.get("lng")
    if lat and lng:
        shops = maps_service.find_nearby(lat, lng)
        return jsonify(shops)
    return render_template("about.html")  # fallback page

# Join queue
@app.route('/queue/join/<shop_id>/<user_id>')
def join_queue(shop_id, user_id):
    queue_service.join_queue(shop_id, user_id)
    return jsonify({"status": "joined"})

# Get queue
@app.route('/queue/<shop_id>')
def get_queue(shop_id):
    queue = queue_service.get_queue(shop_id)
    return jsonify(queue)

# 404 Error page
@app.errorhandler(404)
def page_not_found(e):
    return render_template("error.html"), 404

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
