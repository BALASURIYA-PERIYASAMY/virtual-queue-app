from services.firebase_service import auth, db  # Firebase auth and Firestore wrapper

class User:
    def __init__(self, uid, email, role):
        self.uid = uid
        self.email = email
        self.role = role

    @staticmethod
    def create_user(email, password, role):
        try:
            # Create user in Firebase Auth
            user = auth.create_user(email=email, password=password)
            uid = user['uid']
            # Store role in Firestore
            db.collection('users').document(uid).set({'email': email, 'role': role})
            return User(uid, email, role)
        except Exception as e:
            print("Error creating user:", e)
            return None

    @staticmethod
    def get_user(uid):
        try:
            doc = db.collection('users').document(uid).get()
            if doc.exists:
                data = doc.to_dict()
                return User(uid, data['email'], data['role'])
            return None
        except Exception as e:
            print("Error fetching user:", e)
            return None
