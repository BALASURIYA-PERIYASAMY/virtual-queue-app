"""
Migration 001: Initialize Firestore Collections
"""

import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("instance/secret_config.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

def run():
    # Create collections with sample structure
    db.collection("users").document("sample_user").set({
        "name": "Test User",
        "email": "test@example.com",
        "role": "customer"
    })

    db.collection("shops").document("sample_shop").set({
        "name": "Demo Shop",
        "category": "General",
        "rating": 5.0
    })

    print("✅ Migration 001 applied successfully.")

if __name__ == "__main__":
    run()
