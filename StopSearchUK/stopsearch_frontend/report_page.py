from flask import Flask, jsonify, request, render_template, url_for
from StopSearchUK import app

@app.route("/report", methods=['POST', 'GET'])
def report_page():
    if request.method == "GET":
        # If it's a GET request, render the template
        return render_template('homepage.html')
    else:
        # If it's a POST request, process the form data
        results = {
            "Results": []
        }
        result_data = {
            "ReportEmail": [],
            "VictimInformation": [],
            "PolicePublicRelations": [],
            "PoliceInformation": []
        }
        results["Results"].append(result_data)
        
        # Access form data safely
        form_email = request.form["form_email"]
        
        # Store the form email in result_data
        result_data["ReportEmail"].append(form_email)
        
        # Create a message indicating successful handling of the POST request
        message = "POST request received and processed successfully!"
        
        # Return a JSON response containing the message and the form email
        return jsonify({"message": message, "form_email": form_email})