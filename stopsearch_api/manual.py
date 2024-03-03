from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/docs")
def manual():
    create_report = {}
    find_report_by_age = {}
    documentation = {
        "App": "Stop Search UK",
        "Description": "An app developed to record and report incidents between the public and the police.",
        "Rerdord an incident": create_report,
        "Find Report By": {
            "Age": find_report_by_age,
        }
    }
    return jsonify(documentation, {"status": 200})