import os
from dotenv import load_dotenv
import json

# Load secret config
with open(os.path.join("instance", "secret_config.json")) as f:
    secrets = json.load(f)

# Firebase
FIREBASE_KEY = secrets["firebase"]

# Google Maps
GOOGLE_MAPS_API_KEY = secrets["google_maps"]["api_key"]

# Twilio
TWILIO_SID = secrets["twilio"]["account_sid"]
TWILIO_AUTH = secrets["twilio"]["auth_token"]
TWILIO_PHONE = secrets["twilio"]["phone_number"]

# Flask
SECRET_KEY = secrets["flask"]["secret_key"]

# Load .env file (optional)
load_dotenv()

# Firebase
FIREBASE_KEY = os.getenv("FIREBASE_KEY", "firebase_key.json")

# Google Maps
GOOGLE_MAPS_API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")

# Twilio
TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH = os.getenv("TWILIO_AUTH")
TWILIO_PHONE = os.getenv("TWILIO_PHONE")

# Flask
SECRET_KEY = os.getenv("SECRET_KEY", "supersecret")
