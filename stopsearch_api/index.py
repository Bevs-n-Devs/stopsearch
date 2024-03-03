from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    pages = {
        "Introduction": "/",
        "Guide / Manual": "/docs",
        "Home Page": "/home",
    }
    info = {
        "app": "Stop Search UK",
        "year": "2024",
        "description": "An app developed to record and report incidents between the police and the public.",
        "founder": "Akoto Tech",
        "pages": pages
    }
    
    return jsonify(info, {"status": 200})