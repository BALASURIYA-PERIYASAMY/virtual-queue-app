from flask import session, redirect, url_for, flash

# Store user session
def login_user(user):
    session['uid'] = user.uid
    session['email'] = user.email
    session['role'] = user.role

# Logout user
def logout_user():
    session.pop('uid', None)
    session.pop('email', None)
    session.pop('role', None)

# Protect routes based on login
def login_required(f):
    from functools import wraps
    from flask import request

    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'uid' not in session:
            flash('Please login first.', 'warning')
            return redirect(url_for('auth.login'))
        return f(*args, **kwargs)
    return decorated_function

# Check user role
def role_required(role):
    from functools import wraps

    def wrapper(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if 'role' not in session or session['role'] != role:
                flash('Unauthorized access.', 'danger')
                return redirect(url_for('auth.login'))
            return f(*args, **kwargs)
        return decorated_function
    return wrapper
