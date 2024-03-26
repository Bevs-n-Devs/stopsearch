from stopsearch_webapp import app
from stopsearch_webapp.stopsearch_api.index import *
from stopsearch_webapp.stopsearch_api.home import *
from stopsearch_webapp.stopsearch_api.manual import *
from stopsearch_webapp.stopsearch_api.new_report_demo import *
from stopsearch_webapp.stopsearch_api.search_by_data_id import *
from stopsearch_webapp.stopsearch_api.search_all import *
from stopsearch_webapp.stopsearch_api.new_report_temp import *
from stopsearch_webapp.stopsearch_frontend.home import *

# backend
app.route("/")(index)
app.route("/docs")(manual)
app.route("/home")(home)
app.route("/new/")(new_report_demo)
app.route("/demo")(demo_report)
app.route("/search/all")(search_all)
app.route("/search/<data_id>")(search_by_dataID)
# frontend
app.route("/report")(report_page)

