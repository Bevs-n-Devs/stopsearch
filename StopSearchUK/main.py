from StopSearchUK import app
from StopSearchUK.stopsearch_api.index_route import index_route
from StopSearchUK.stopsearch_api.home_route import home_route
from StopSearchUK.stopsearch_api.manual_route import manual_route
from StopSearchUK.stopsearch_api.demo_route import demo_route
from StopSearchUK.stopsearch_api.search_by_data_id import search_by_dataID_route
from StopSearchUK.stopsearch_api.search_all import search_all_route
from StopSearchUK.stopsearch_api.report_demo_route import report_demo_route
from StopSearchUK.stopsearch_frontend.report_page import report_page
from StopSearchUK.stopsearch_api.new_report_route import new_report_route
from StopSearchUK.stopsearch_frontend.map_page import stopsearch_map_page


# backend
app.route("/")(index_route)
app.route("/docs")(manual_route)
app.route("/home")(home_route)
app.route("/new/")(report_demo_route)
app.route("/demo")(demo_route)
app.route("/search/all")(search_all_route)
app.route("/search/<data_id>")(search_by_dataID_route)
app.route("/new/report")(new_report_route)
# frontend
app.route("/report")(report_page)
app.route("/map")(stopsearch_map_page)