from flask import Flask, render_template, request, redirect, url_for, jsonify
from pymongo import MongoClient
import json

app = Flask(__name__)

client = MongoClient("mongodb+srv://panwarkuldeepofficial_db_user:<db_password>@cluster0.3iza4ro.mongodb.net/?appName=Cluster0")
db = client["student_db"]
collection = db["students"]

# Home route - Form
@app.route('/')
def form():
    return render_template('form.html')

# Submit form (MongoDB insert)
@app.route('/submit', methods=['POST'])
def submit():
    try:
        name = request.form['name']
        grade = request.form['grade']

        collection.insert_one({
            "name": name,
            "grade": grade
        })

        return redirect(url_for('success'))

    except Exception as e:
        return render_template('form.html', error=str(e))

# Success page
@app.route('/success')
def success():
    return render_template('success.html')

# API route (file-based JSON)
@app.route('/api', methods=['GET'])
def get_data():
    try:
        with open('data.json', 'r') as file:
            data = json.load(file)
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)