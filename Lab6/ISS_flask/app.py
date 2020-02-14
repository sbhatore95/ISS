from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)


project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "studentDatabase.db"))
app.config['SQLALCHEMY_DATABASE_URI'] = database_file
db = SQLAlchemy(app)

class Student(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	rollnumber = db.Column(db.Integer, nullable = False)
	name = db.Column(db.String(80), nullable=False)
	email = db.Column(db.String(120), nullable=False)	

@app.route('/')
def root():
	return "Hello"

@app.route('/students/create', methods = ['GET', 'POST'])
def create():
	if request.form:
		form = request.form
		s = Student(name = form['name'], rollnumber = form['rollnumber'], email = form['email'])
		db.session.add(s)
		db.session.commit()
		return redirect(url_for('getStudents'))
	return render_template('home.html')

@app.route('/students', methods = ['GET'])
def getStudents():
	students = Student.query.all()
	data = []
	for s in students:
		obj = {
			"username" : s.name,
			"rollnumber" : s.rollnumber,
			"email" : s.email
		}
		data.append(obj)	
	return str(data)

if __name__ == '__main__':
	app.run(debug = True)
