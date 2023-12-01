from flask import Blueprint, render_template, request, flash

auths = Blueprint('auths', __name__)

@auths.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@auths.route('/logout')
def logout():
    return '<h1>Logout Page</h1>'

@auths.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
    
        if len(email) < 4:
            flash('Email is too short', category='error')
        elif len(firstName) < 2:
            flash('Name is too short', category='error')
        elif password1 != password2:
            flash('Password do not match', category='error')
        elif len(password1) < 7:
            flash('Password is too short', category='error')
        else:
            flash('Account created !', category='success')
        
    return render_template('sign-up.html')