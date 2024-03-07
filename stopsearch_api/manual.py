from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/docs")
def manual():
    pages = {
        "0": "/",
        "1": "/docs",
        "2": "/home",
        "3": "/create/report/",
        "4": "/find/by/victim",
        "5": "/find/by/witness"
    }
    create_report = {}
    find_report_by_age = {}
    documentation = {
        "App": "StopSearch UK",
        "Year": "2024",
        "Description": "An app developed to record and report incidents between the police and the public.",
        "Founder": "Daniella Rose + Akoto Tech",
        "AppPage": "/docs",
        "Pages": [
            {
                "Index": pages["0"],
                "Manual": pages["1"],
                "HomePage": pages["2"],
                "CreateReport": pages["3"],
                "FindReportByVictim": pages["4"],
                "FindReportByWitness": pages["5"],
            }
        ]
    }
    return jsonify(documentation, {"status": 200})