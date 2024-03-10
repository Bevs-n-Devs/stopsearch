import os
from flask import Flask
from stopsearch_api.index import index
from stopsearch_api.manual import manual
from stopsearch_api.home import home
from stopsearch_api.new_report import new_report
from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__)

# register your routes here
app.route("/")(index)
app.route("/docs")(manual)
app.route("/home")(home)
app.route("/new/<formType>/<formDate>")(new_report)

if __name__ == "__main__":
    app.run(
        debug=True,
        port=os.environ["API_PORT"],
        host=os.environ["API_HOST"],
    )