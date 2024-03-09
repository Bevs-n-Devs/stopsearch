from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/create/new/<formType>/<formDate>", methods=["GET"])
def create_new_report(formType: str, formDate: str) -> list[dict]:
    formType_ = formType
    # .form.get("formType")
    formDate_= formDate
    app_data = {
        "AppData": []
    }
    app_pages = {
        "AppPages": []
    }
    status = {
        "Status": 200
    }
    
    # add data to AppData
    appData = {
        "App": "StopSearch UK",
        "AppPage": "/",
        "Description": "An app developed to record and report incidents between the police and the public.",
        "Founder": "Daniella Rose + Akoto Tech",
        "Year": "2024",
    }
    app_data["AppData"].append(appData)
    
    # add data to AppPages
    appPages = {
        "Index": "/",
        "Manual": "/docs",
        "HomePage": "/home",
        "CreateReport": "/create/report",
        "FindReportByVictim": "/find/by/victim",
        "FindReportByWitness": "/find/by/witness",
    }
    app_pages["AppPages"].append(appPages)
    
    user_report_data = {
        "userReportData": []
    }
    user_report_data["userReportData"].append(formType_)
    user_report_data["userReportData"].append(formDate_)
    
    return jsonify(app_data, app_pages, user_report_data )