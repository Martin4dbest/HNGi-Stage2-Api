from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from wtforms import Form, StringField, IntegerField
from wtforms.validators import DataRequired, Email, Optional
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from werkzeug.datastructures import MultiDict

app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///persons.db'
db = SQLAlchemy(app)  # Initialize SQLAlchemy

# Define a form for input validation
class PersonForm(Form):
    name = StringField('Name', validators=[DataRequired()])
    age = IntegerField('Age', validators=[Optional()])
    email = StringField('Email', validators=[DataRequired(), Email()])

# Define the Person model
class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer)
    email = db.Column(db.String(100), unique=True, nullable=False)

# Create the database tables
def create_database():
    with app.app_context():
        db.create_all()

# Create a Limiter for rate limiting
limiter = Limiter(
    app,
    default_limits=["10 per minute"]
)

# Create a new person
@app.route('/api/person', methods=['POST'])
@limiter.limit("5 per minute")  # Adjust rate limiting as needed
def create_person():
    json_data = request.json  # Get the JSON data from the request
    formdata = MultiDict(mapping=json_data)  # Create a MultiDict from the JSON data
    form = PersonForm(formdata)  # Pass the MultiDict to the form
    if form.validate():
        data = form.data
        if 'name' not in data:
            return jsonify({"error": "Name is required"}), 400
        new_person = Person(name=data['name'], age=data.get('age'), email=data.get('email'))
        db.session.add(new_person)
        db.session.commit()
        return jsonify({"message": "Person created"}), 201
    else:
        return jsonify({"error": form.errors}), 400

# Retrieve details of a person by user ID
@app.route('/api/person/<int:user_id>', methods=['GET'])
def get_person(user_id):
    person = Person.query.get(user_id)
    if person is None:
        return jsonify({"error": "Person not found"}), 404
    return jsonify({
        "id": person.id,
        "name": person.name,
        "age": person.age,
        "email": person.email
    })

# Update details of an existing person by user ID
@app.route('/api/person/<int:user_id>', methods=['PUT'])
def update_person(user_id):
    person = Person.query.get(user_id)
    if person is None:
        return jsonify({"error": "Person not found"}), 404
    data = request.json
    person.name = data.get('name', person.name)
    person.age = data.get('age', person.age)
    person.email = data.get('email', person.email)
    db.session.commit()
    return jsonify({"message": "Person updated"}), 200

# Remove a person by user ID
@app.route('/api/person/<int:user_id>', methods=['DELETE'])
def delete_person(user_id):
    person = Person.query.get(user_id)
    if person is None:
        return jsonify({"error": "Person not found"}), 404
    db.session.delete(person)
    db.session.commit()
    return jsonify({"message": "Person removed"}), 200

# Retrieve details of a person by the name
@app.route('/api/person', methods=['GET'])
def get_person_by_name():
    name = request.args.get('name')
    person = Person.query.filter_by(name=name).first()
    if person is None:
        return jsonify({"error": "Person not found"}), 404
    return jsonify({
        "id": person.id,
        "name": person.name,
        "age": person.age,
        "email": person.email
    })

if __name__ == '__main__':
    create_database()  # Call this function to create the tables when needed
    app.run(debug=True)
