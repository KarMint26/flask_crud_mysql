from flask import render_template, request, redirect, url_for, flash
from models import db, Students

def index():
    students = Students.query.all()
    return render_template("index.html", students=students)

def show_student(id):
    student = Students.query.get_or_404(id)
    return render_template("show_student.html", name=student.name, age=student.age, email=student.email)

def create_student():
    if request.method == "POST":
        name = request.form['name']
        age = request.form['age']
        email = request.form['email']

        # Validasi input
        if not name or not age or not email:
            flash('All fields are required!', 'danger')
            return redirect(url_for('create_student'))

        new_student = Students(name=name, age=age, email=email)
        db.session.add(new_student)
        db.session.commit()
        flash('Student created successfully!', 'success')
        return redirect(url_for('index'))
    
    return render_template("create_student.html")

def update_student(id):
    student = Students.query.get_or_404(id)
    if request.method == "POST":
        student.name = request.form['name']
        student.age = request.form['age']
        student.email = request.form['email']
        
        db.session.commit()
        flash('Student updated successfully!', 'success')
        return redirect(url_for('index'))
    
    return render_template("update_student.html", student=student)

def delete_student(id):
    student = Students.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    flash('Student deleted successfully!', 'success')
    return redirect(url_for('index'))
