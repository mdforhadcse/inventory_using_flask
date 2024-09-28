# app.py
from flask import Flask, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Initialize Extensions
db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        role = request.form['role']
        # hashed_password = generate_password_hash(password, method='sha256')
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')

        # Create and add new user
        new_user = User(username=username, email=email, password=hashed_password, role=role)
        db.session.add(new_user)
        db.session.commit()
        flash('User registered successfully.')
        return redirect(url_for('login'))

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            login_user(user)
            if user.is_admin():
                return redirect(url_for('admin_dashboard'))
            else:
                return redirect(url_for('staff_dashboard'))
        else:
            flash('Invalid username or password')
    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/admin_dashboard')
@login_required
def admin_dashboard():
    if not current_user.is_admin():
        flash('Access Denied!')
        return redirect(url_for('staff_dashboard'))
    return render_template('admin_dashboard.html')


@app.route('/staff_dashboard')
@login_required
def staff_dashboard():
    return render_template('staff_dashboard.html')

# Create a function to initialize the database
def create_tables():
    with app.app_context():
        db.create_all()
        print("Tables created successfully!")

# Call the function to create tables at the start of the application
create_tables()

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)