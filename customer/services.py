from services import firebase_service as fb, queue_service

def get_customer_dashboard(user_id):
    """Fetch customer details & recent shops"""
    user = fb.get_user(user_id)
    shops = fb.get_shops()
    return {"user": user, "recent": shops[:3]}  # show top 3 shops as recent

def join_queue(shop_id, user_id):
    """Customer joins a queue"""
    return queue_service.join_queue(shop_id, user_id)

def get_status(user_id):
    """Check status of queues user joined"""
    shops = fb.get_shops()
    status_list = []
    for shop in shops:
        queue = queue_service.get_queue(shop["id"])
        for entry in queue:
            if entry["user_id"] == user_id:
                status_list.append({"shop": shop["name"], "status": entry["status"]})
    return status_list

def get_profile(user_id):
    """Get user profile"""
    return fb.get_user(user_id)

def update_profile(user_id, new_data):
    """Update profile data"""
    fb.db.collection("users").document(user_id).update(new_data)
    return True
