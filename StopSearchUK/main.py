from StopSearchUK import app
from StopSearchUK.stopsearch_api.index_route import index_route
from StopSearchUK.stopsearch_api.home_route import home_route
from StopSearchUK.stopsearch_api.manual_route import manual_route
from StopSearchUK.stopsearch_api.demo_route import demo_route
from StopSearchUK.stopsearch_api.report_demo_route import report_demo_route
# minimal viable product - MVP
from StopSearchUK.stopsearch_api.new_report_route import new_report_route
from StopSearchUK.stopsearch_api.map_route import map_data
from StopSearchUK.stopsearch_api.search_engine_route import (
    search_all_reports_route, 
    search_reports_by_data_id_route, 
    search_report_by_form_type,
    search_report_by_victim_age,
    search_report_by_victim_gender,
    search_report_by_victim_race,
    search_report_by_search_reason,
    search_report_by_search_type,
    search_report_by_search_by_90_days,
    search_report_by_search_by_6_months,
    search_report_by_search_by_12_months,
    search_report_by_search_by_30_days,
    search_report_by_year
)
from StopSearchUK.stopsearch_frontend.report_page import report_page
from StopSearchUK.stopsearch_frontend.map_page import (
    stopsearch_map_page,
    show_map_by_data_id,
    show_map_by_30_days,
    show_map_by_90_days,
    show_map_by_6_months,
    show_map_by_1_year,
    show_map_by_year, # needs fixing
    show_map_by_form_type,
    show_map_by_search_type,
)



app.route("/")(index_route)
app.route("/docs")(manual_route)
app.route("/home")(home_route)
app.route("/new/")(report_demo_route)
app.route("/demo")(demo_route)

# minimal viable product - MVP
app.route("/new/report")(new_report_route)
app.route("/report")(report_page)
app.route("/map-data")(map_data)
app.route("/map")(stopsearch_map_page)
app.route("/map/<data_id>")(show_map_by_data_id)
app.route("/map/30days")(show_map_by_30_days)
app.route("/map/90days")(show_map_by_90_days)
app.route("/map/6months")(show_map_by_6_months)
app.route("/map/1year")(show_map_by_1_year)
app.route("/map/year/<year>")(show_map_by_year)
app.route("/map/formType/<form_type>")(show_map_by_form_type)
app.route("/map/searchType/<search_type>")(show_map_by_search_type)

app.route("/search/all")(search_all_reports_route)
app.route("/search/<data_id>")(search_reports_by_data_id_route)
app.route("/search/formType/<form_type>")(search_report_by_form_type)
app.route("/search/victimAge/<victim_age>")(search_report_by_victim_age)
app.route("/search/victimGender/<victim_gender>")(search_report_by_victim_gender)
app.route("/search/victimRace/<victim_race>")(search_report_by_victim_race)
app.route("/search/searchReason/<search_reason>")(search_report_by_search_reason)
app.route("/search/searchType/<search_type>")(search_report_by_search_type)
app.route("/search/90days")(search_report_by_search_by_90_days)
app.route("/search/6months")(search_report_by_search_by_6_months)
app.route("/search/1year")(search_report_by_search_by_12_months)
app.route("/search/30days")(search_report_by_search_by_30_days)
app.route("/search/year/<year>")(search_report_by_year)