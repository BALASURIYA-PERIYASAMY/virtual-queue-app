from datetime import datetime
from services import firebase_service as fb

def join_queue(shop_id, user_id):
    """User joins the shop queue"""
    queue_ref = fb.db.collection("shops").document(shop_id).collection("queue")
    queue_ref.add({
        "user_id": user_id,
        "joined_at": datetime.utcnow(),
        "status": "waiting"
    })
    return True

def get_queue(shop_id):
    """Get current queue for a shop"""
    queue_ref = fb.db.collection("shops").document(shop_id).collection("queue")
    queue = queue_ref.order_by("joined_at").stream()
    return [q.to_dict() for q in queue]

def update_status(shop_id, queue_id, status):
    """Update queue status (waiting, in-progress, completed)"""
    fb.db.collection("shops").document(shop_id).collection("queue").document(queue_id).update({"status": status})
