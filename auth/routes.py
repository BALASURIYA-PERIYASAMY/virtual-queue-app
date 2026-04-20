from flask import render_template, request, redirect, url_for, flash
from . import auth_bp
from .models import User
from .utils import login_user, logout_user

# Register route
@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        role = request.form['role']  # 'customer' or 'shop_owner'
        user = User.create_user(email, password, role)
        if user:
            flash('Registration successful! Please login.', 'success')
            return redirect(url_for('auth.login'))
        else:
            flash('Registration failed. Try again.', 'danger')
    return render_template('register.html')

# Login route
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            # Firebase login
            from services.firebase_service import auth as fb_auth
            user_data = fb_auth.sign_in_with_email_and_password(email, password)
            uid = user_data['localId']
            user = User.get_user(uid)
            if user:
                login_user(user)
                flash('Login successful!', 'success')
                if user.role == 'customer':
                    return redirect(url_for('customer.dashboard'))
                elif user.role == 'shop_owner':
                    return redirect(url_for('shop_owner.dashboard'))
            else:
                flash('User not found.', 'danger')
        except Exception as e:
            flash('Invalid email or password', 'danger')
    return render_template('login.html')

# Logout route
@auth_bp.route('/logout')
def logout():
    logout_user()
    flash('Logged out successfully.', 'info')
    return redirect(url_for('auth.login'))
