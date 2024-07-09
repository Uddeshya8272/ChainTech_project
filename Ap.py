# app.py
# app.py (no changes needed)
from flask import Flask, render_template, jsonify, request
from datetime import datetime
import json
import random
import csv

app = Flask(__name__)

#Load the quotes dataset
with open('static/quotes.json') as f:
    quotes = json.load(f)

@app.route("/submit", methods=["POST"])
def handle_form_submission():
    name = request.form.get("name")
    email = request.form.get("email")

    # Write the data to the CSV file
    with open("static/data.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([name, email])

    # Return the data as JSON
    return jsonify({"name": name, "email": email})

@app.route('/api/random_quote')
def random_quote():
    quote = random.choice(quotes)
    return jsonify({'quote': quote['quote'], 'author': quote['author']})

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
