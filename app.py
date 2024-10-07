import os
from flask import Flask
from controllers import UserController
from models import db

app = Flask(__name__)

# Configure your database
username = os.getenv('DB_USERNAME')
password = os.getenv('DB_PASSWORD')
hostname = os.getenv('DB_HOSTNAME')
database_name = os.getenv('DB_NAME')
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://{username}:{password}@{hostname}/{database_name}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Set a secret key for session management
app.secret_key = os.urandom(24)  # Generate a random 24-byte secret key

db.init_app(app)  # Initialize the app with db

# Create all database tables
with app.app_context():
    db.create_all()  # Create all tables defined in your models

# Home route to display all students
@app.route("/", methods=["GET"])
def index():
    return UserController.index()

# Show spesifik id student
@app.get("/student/<int:id>")
def show_student(id):
    return UserController.show_student(id)

# Form to create a new student
@app.route("/create_student", methods=["GET", "POST"])
def create_student():
    return UserController.create_student()

# Update student data
@app.route("/update_student/<int:id>", methods=["GET", "POST"])
def update_student(id):
    return UserController.update_student(id)

# Delete a student
@app.route("/delete_student/<int:id>", methods=["POST"])
def delete_student(id):
    return UserController.delete_student(id)

if __name__ == '__main__':
    app.run(debug=True)
