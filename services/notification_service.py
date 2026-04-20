# services/notification_service.py
import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

# Twilio credentials (from .env or environment)
TWILIO_SID   = os.getenv("TWILIO_SID")
TWILIO_AUTH  = os.getenv("TWILIO_AUTH")
TWILIO_PHONE = os.getenv("TWILIO_PHONE")          # e.g. +1415xxxxxxx (SMS-capable Twilio number)
TWILIO_WA    = os.getenv("TWILIO_WHATSAPP_FROM") # e.g. whatsapp:+14155238886 (sandbox or production WA number)

if not TWILIO_SID or not TWILIO_AUTH:
    raise EnvironmentError("Twilio credentials not set. Add TWILIO_SID and TWILIO_AUTH to .env")

client = Client(TWILIO_SID, TWILIO_AUTH)


# ---------------- SMS ----------------
def send_sms(to, message):
    """Send plain SMS (E.164 phone, e.g. +919876543210)."""
    msg = client.messages.create(
        body=message,
        from_=TWILIO_PHONE,
        to=to
    )
    return msg.sid


# ---------------- WhatsApp (Template) ----------------
def send_whatsapp_template(to_whatsapp_e164, content_sid, variables):
    """
    Send a pre-approved WhatsApp template message.
    - to_whatsapp_e164: 'whatsapp:+91xxxxxxxxxx'
    - content_sid: the HX... content SID from Twilio console
    - variables: dict mapping "1","2",... to values, e.g. {"1":"12/1","2":"3pm"}
    """
    # Twilio expects content_variables as a JSON string
    import json
    content_variables_str = json.dumps(variables)

    msg = client.messages.create(
        from_=TWILIO_WA,
        content_sid=content_sid,
        content_variables=content_variables_str,
        to=to_whatsapp_e164
    )
    return msg.sid


# ---------------- WhatsApp (Free-form after user replies) ----------------
def send_whatsapp_message(to_whatsapp_e164, text):
    """
    Send a free-form WhatsApp message. Works only if user has replied to the business within 24 hours (or after conversation is open).
    """
    msg = client.messages.create(
        from_=TWILIO_WA,
        body=text,
        to=to_whatsapp_e164
    )
    return msg.sid


# Convenience wrapper for appointment reminders (use template)
def send_appointment_whatsapp(to_number_e164, date_str, time_str, content_sid):
    """
    Sends appointment reminder using template placeholders. Example:
      variables = {"1": date_str, "2": time_str}
    """
    variables = {"1": date_str, "2": time_str}
    return send_whatsapp_template(f"whatsapp:{to_number_e164}", content_sid, variables)
