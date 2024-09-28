from app import db, app

# Create the tables using the app context
with app.app_context():
    db.create_all()
    print("Tables created successfully!")