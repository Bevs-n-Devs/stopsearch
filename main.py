import os
from flask import Flask
from stopsearch_api.index import index
from stopsearch_api.manual import manual
from stopsearch_api.home import home
from stopsearch_api.new_report_demo import new_report_demo
from stopsearch_api.new_report_temp import demo_report
from stopsearch_api.search_all import search_all
from stopsearch_api.search_by_data_id import search_by_dataID
from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__)

# register your routes here
app.route("/")(index)
app.route("/docs")(manual)
app.route("/home")(home)
app.route("/new/")(new_report_demo)
app.route("/demo")(demo_report)
app.route("/search/all")(search_all)
app.route("/search/<data_id>")(search_by_dataID)

if __name__ == "__main__":
    app.run(
        debug=True,
        port=os.environ["API_PORT"],
        host=os.environ["API_HOST"],
    )