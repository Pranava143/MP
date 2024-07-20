from flask import Flask, render_template
from Code_1 import start1  # Import the function directly

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/start_detection')
def start_detection():
    start1()
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
