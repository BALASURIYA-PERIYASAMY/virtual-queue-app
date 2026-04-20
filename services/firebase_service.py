import firebase_admin
from firebase_admin import credentials, auth, firestore

# Initialize Firebase (only once)
cred = credentials.Certificate("firebase_key.json")  # Your Firebase Admin SDK JSON
firebase_admin.initialize_app(cred)
db = firestore.client()

# ---------- AUTH ----------
def register_user(email, password, user_data):
    """Register new user with Firebase Auth & store details in Firestore"""
    user = auth.create_user(email=email, password=password)
    db.collection("users").document(user.uid).set(user_data)
    return user.uid

def login_user(email):
    """Fetch user details by email (Password verification handled client-side)"""
    users = db.collection("users").where("email", "==", email).stream()
    return [u.to_dict() for u in users]

# ---------- FIRESTORE ----------
def add_shop(shop_id, shop_data):
    """Add a shop to Firestore"""
    db.collection("shops").document(shop_id).set(shop_data)

def get_shops():
    """Retrieve all shops"""
    shops = db.collection("shops").stream()
    return [s.to_dict() for s in shops]

def get_user(uid):
    """Fetch user profile by UID"""
    return db.collection("users").document(uid).get().to_dict()
