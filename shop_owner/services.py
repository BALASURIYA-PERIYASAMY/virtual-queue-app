from services import firebase_service as fb, queue_service

def get_shop_dashboard(shop_id):
    """Fetch shop details & current queue"""
    shop = fb.get_shop(shop_id)
    queues = queue_service.get_queue(shop_id)
    return {"shop": shop, "queues": queues}

def get_queue(shop_id):
    """Get all users in queue for this shop"""
    return queue_service.get_queue(shop_id)

def get_appointments(shop_id):
    """Get all appointments for this shop"""
    appointments = fb.db.collection("appointments").where("shop_id", "==", shop_id).stream()
    result = []
    for app in appointments:
        data = app.to_dict()
        data["id"] = app.id
        result.append(data)
    return result

def update_appointment(appointment_id, action):
    """Approve or reject appointment"""
    fb.db.collection("appointments").document(appointment_id).update({"status": action})
    return True

def get_profile(shop_id):
    """Get shop profile"""
    return fb.get_shop(shop_id)

def update_profile(shop_id, new_data):
    """Update shop profile"""
    fb.db.collection("shops").document(shop_id).update(new_data)
    return True
