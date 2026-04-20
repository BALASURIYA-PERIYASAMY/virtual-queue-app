# 🏪 Virtual Queue Management System (QuickQ)

A smart **Virtual Queue & Shop Appointment System** built using **Flask + Firebase + Google Maps + Twilio**.

## 🚀 Features
- User & Shop Owner Registration/Login (Firebase Auth)
- Queue Management (Join, Track, Update status)
- Google Maps Integration (Nearby shops)
- SMS Notifications & Appointment Reminders (Twilio)
- Search, Filter & Manage Shops
- Responsive UI with Tailwind + Bootstrap

## 📂 Project Structure
virtual_queue_management_system
|-admin/
|-auth/
|-customer/
|-database/
|-instance/
|-services/
|-shop_owner/
|-static/
   |-css/
      |-style.css
      |-tailwind.css
   |-js/
      |-app.js
      |-customer.js
      |-shop.js
|-templates/
   |-about.html
   |-base.html
   |-contact.html
   |-error.html
   |-index.html
   |-login.html
   |-register.html
|-app.py
|-config.py
|-firebase_key.json
|-google-services.json
|-requirements.txt

bash
Copy code

## ⚡ Setup Instructions
1. Clone repo  
   ```bash
   git clone https://github.com/BALASURIYA-PERIYASAMY/virtual-queue-app.git
   cd quickq
Install dependencies

bash
Copy code
pip install -r requirements.txt
Add Firebase Key (firebase_key.json) to root folder.

Run app

bash
Copy code
python app.py
🌐 APIs Used
Firebase Firestore/Auth

Google Maps API

Twilio SMS API

👨‍💻 Contributors
Your Name

yaml
Copy code

---

### 📂 `.gitignore`
```gitignore
# Python
__pycache__/
*.pyc
*.pyo

# Environment
.env
*.json
firebase_key.json

# IDE
.vscode/
.idea/

# OS
.DS_Store
