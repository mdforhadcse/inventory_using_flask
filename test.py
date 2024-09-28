# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from config import Config
#
# app = Flask(__name__)
# app.config.from_object(Config)
#
# # Initialize SQLAlchemy
# db = SQLAlchemy(app)
#
# # User model definition
# class User(db.Model):
#     __tablename__ = 'users'
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(150), unique=True, nullable=False)
#     email = db.Column(db.String(150), unique=True, nullable=False)
#     password = db.Column(db.String(150), nullable=False)
#     role = db.Column(db.String(10), nullable=False)
#
# # Create the database tables
# if __name__ == '__main__':
#     with app.app_context():
#         db.create_all()  # Create all tables defined in models
#         print("Tables created successfully!")  # Print to confirm creation
#     app.run(debug=True)