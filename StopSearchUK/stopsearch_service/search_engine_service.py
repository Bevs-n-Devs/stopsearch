from StopSearchUK.utils import *
from sqlalchemy import *
from StopSearchUK import app
from StopSearchUK.stopsearch_database.extension import LocalSession, init_db
from StopSearchUK.stopsearch_database.models import (
    Data,
    ReportedBy,
    VictimInformation,
    PolicePublicRelations,
    PoliceInformation,
    FormType,
    FormDate,
    IncidentAddress,
    FormMedia,
    MapCoordinates,
    PoliceOfficerInformation,
    AdditionalOfficer,
)
init_db()


# get all report data
def search_all_reports() -> list[Data]:
    """
    SELECT data.dataID
           formType.form_type,
           formDate.formatted_date,
           formDate.formatted_month,
           formDate.formatted_year,
           formDate.formatted_time,
           victimInformation.number_of_victims,
           victimInformation.victim_age,
           victimInformation.victim_race,
           victimInformation.victim_gender,
           policePublicRelations.search_reason,
           policePublicRelations.type_of_search,
           policePublicRelations.additional_notes,
           incidentAddress.street_name,
           incidentAddress.town_or_city,
           mapCoordinates.longitude,
           mapCoordinates.latitude,
           policeInformation.number_of_police,
           policeInformation.obtain_police_info,
           policeOfficerInformation.police_badge_number,
           policeOfficerInformation.police_officer_name,
           policeOfficerInformation.police_station,
           policeOfficerInformation.get_additional_officers,
    FROM data
        JOIN reportedBy
            ON data.dataID = reportedBy.reportedByID
        JOIN formType
            ON reportedBy.reportedByID = formType.formTypeID,
        JOIN formDate
            ON reportedBy.reportedByID = formDate.formDateID
        JOIN victimInformation
            ON data.dataID = victimInformation.victimInformationID
        JOIN policePublicRelations
            ON data.dataID = policePublicRelationsID
        JOIN incidentAddress
            ON policePublicRelations.policePublicRelationsID = incidentAddress.incidentAddressID
        JOIN mapCoordinates
            ON incidentAddress.incidentAddressID = mapCoordinates.mapCoordinatesID
        JOIN policeInformation
            ON data.dataID = policeInformation
        JOIN policeOfficerInformation
            ON policeInformation.policeInformationID = policeOfficerInformation.policeOfficerInformationID,
    """
    with app.app_context():
        session = LocalSession()
        
        sql_query = select(
            Data.dataID,
            FormType.form_type,
            FormDate.formatted_date,
            FormDate.formatted_month,
            FormDate.formatted_year,
            FormDate.formatted_time,
            VictimInformation.number_of_victims,
            VictimInformation.victim_age,
            VictimInformation.victim_race,
            VictimInformation.victim_gender,
            PolicePublicRelations.search_reason,
            PolicePublicRelations.type_of_search,
            PolicePublicRelations.additional_notes,
            IncidentAddress.street_name,
            IncidentAddress.town_or_city,
            MapCoordinates.longitude,
            MapCoordinates.latitude,
            PoliceInformation.number_of_police,
            PoliceInformation.obtain_police_info,
            PoliceOfficerInformation.police_badge_number,
            PoliceOfficerInformation.police_officer_name,
            PoliceOfficerInformation.police_station,
            PoliceOfficerInformation.get_additional_officers,
        ).join(
            ReportedBy, Data.dataID==ReportedBy.data_ID 
        ).join(
            FormType, ReportedBy.reportedByID==FormType.formTypeID
        ).join(
            FormDate, ReportedBy.reportedByID==FormDate.formDateID
        ).join(
            VictimInformation, Data.dataID==VictimInformation.data_ID
        ).join(
            PolicePublicRelations, Data.dataID==PolicePublicRelations.data_ID
        ).join(
            IncidentAddress, PolicePublicRelations.policePublicRelationsID==IncidentAddress.incidentAddressID
        ).join(
            MapCoordinates, IncidentAddress.incidentAddressID==MapCoordinates.mapCoordinatesID
        ).join(
            PoliceInformation, Data.dataID==PoliceInformation.data_ID
        ).join(
            PoliceOfficerInformation, PoliceInformation.policeInformationID==PoliceOfficerInformation.policeOfficerInformationID
        )
        
        try:
            all_data = session.execute(sql_query).all()
            return all_data
        except Exception as e:
            return {"SQL Error": e}

# get report data by Data.dataID
def search_report_by_data_id(data_id: int):
    """
    SELECT data.dataID
           formType.form_type,
           formDate.formatted_date,
           formDate.formatted_month,
           formDate.formatted_year,
           formDate.formatted_time,
           victimInformation.number_of_victims,
           victimInformation.victim_age,
           victimInformation.victim_race,
           victimInformation.victim_gender,
           policePublicRelations.search_reason,
           policePublicRelations.type_of_search,
           policePublicRelations.additional_notes,
           incidentAddress.street_name,
           incidentAddress.town_or_city,
           mapCoordinates.longitude,
           mapCoordinates.latitude,
           policeInformation.number_of_police,
           policeInformation.obtain_police_info,
           policeOfficerInformation.police_badge_number,
           policeOfficerInformation.police_officer_name,
           policeOfficerInformation.police_station,
           policeOfficerInformation.get_additional_officers,
    FROM data
        JOIN reportedBy
            ON data.dataID = reportedBy.reportedByID
        JOIN formType
            ON reportedBy.reportedByID = formType.formTypeID,
        JOIN formDate
            ON reportedBy.reportedByID = formDate.formDateID
        JOIN victimInformation
            ON data.dataID = victimInformation.victimInformationID
        JOIN policePublicRelations
            ON data.dataID = policePublicRelationsID
        JOIN incidentAddress
            ON policePublicRelations.policePublicRelationsID = incidentAddress.incidentAddressID
        JOIN mapCoordinates
            ON incidentAddress.incidentAddressID = mapCoordinates.mapCoordinatesID
        JOIN policeInformation
            ON data.dataID = policeInformation
        JOIN policeOfficerInformation
            ON policeInformation.policeInformationID = policeOfficerInformation.policeOfficerInformationID
    WHERE data.dataID = :data_id
    """
    with app.app_context():
        session = LocalSession()
        
        sql_query = select(
            Data.dataID,
            FormType.form_type,
            FormDate.formatted_date,
            FormDate.formatted_month,
            FormDate.formatted_year,
            FormDate.formatted_time,
            VictimInformation.number_of_victims,
            VictimInformation.victim_age,
            VictimInformation.victim_race,
            VictimInformation.victim_gender,
            PolicePublicRelations.search_reason,
            PolicePublicRelations.type_of_search,
            PolicePublicRelations.additional_notes,
            IncidentAddress.street_name,
            IncidentAddress.town_or_city,
            MapCoordinates.longitude,
            MapCoordinates.latitude,
            PoliceInformation.number_of_police,
            PoliceInformation.obtain_police_info,
            PoliceOfficerInformation.police_badge_number,
            PoliceOfficerInformation.police_officer_name,
            PoliceOfficerInformation.police_station,
            PoliceOfficerInformation.get_additional_officers,
        ).join(
            ReportedBy, Data.dataID==ReportedBy.data_ID 
        ).join(
            FormType, ReportedBy.reportedByID==FormType.formTypeID
        ).join(
            FormDate, ReportedBy.reportedByID==FormDate.formDateID
        ).join(
            VictimInformation, Data.dataID==VictimInformation.data_ID
        ).join(
            PolicePublicRelations, Data.dataID==PolicePublicRelations.data_ID
        ).join(
            IncidentAddress, PolicePublicRelations.policePublicRelationsID==IncidentAddress.incidentAddressID
        ).join(
            MapCoordinates, IncidentAddress.incidentAddressID==MapCoordinates.mapCoordinatesID
        ).join(
            PoliceInformation, Data.dataID==PoliceInformation.data_ID
        ).join(
            PoliceOfficerInformation, PoliceInformation.policeInformationID==PoliceOfficerInformation.policeOfficerInformationID
        ).where(
            Data.dataID == data_id
        )
        
        try:
            all_data = session.execute(sql_query).first()
            return all_data
        except Exception as e:
            return {"SQL Error": e}

# get report by FormType.form_type
def search_report_by_form_type(form_type: str) -> list[Data]:
    """
    SELECT data.dataID
           formType.form_type,
           formDate.formatted_date,
           formDate.formatted_month,
           formDate.formatted_year,
           formDate.formatted_time,
           victimInformation.number_of_victims,
           victimInformation.victim_age,
           victimInformation.victim_race,
           victimInformation.victim_gender,
           policePublicRelations.search_reason,
           policePublicRelations.type_of_search,
           policePublicRelations.additional_notes,
           incidentAddress.street_name,
           incidentAddress.town_or_city,
           mapCoordinates.longitude,
           mapCoordinates.latitude,
           policeInformation.number_of_police,
           policeInformation.obtain_police_info,
           policeOfficerInformation.police_badge_number,
           policeOfficerInformation.police_officer_name,
           policeOfficerInformation.police_station,
           policeOfficerInformation.get_additional_officers,
    FROM data
        JOIN reportedBy
            ON data.dataID = reportedBy.reportedByID
        JOIN formType
            ON reportedBy.reportedByID = formType.formTypeID,
        JOIN formDate
            ON reportedBy.reportedByID = formDate.formDateID
        JOIN victimInformation
            ON data.dataID = victimInformation.victimInformationID
        JOIN policePublicRelations
            ON data.dataID = policePublicRelationsID
        JOIN incidentAddress
            ON policePublicRelations.policePublicRelationsID = incidentAddress.incidentAddressID
        JOIN mapCoordinates
            ON incidentAddress.incidentAddressID = mapCoordinates.mapCoordinatesID
        JOIN policeInformation
            ON data.dataID = policeInformation
        JOIN policeOfficerInformation
            ON policeInformation.policeInformationID = policeOfficerInformation.policeOfficerInformationID
    WHERE formType.form_type = :form_type
    """
    with app.app_context():
        session = LocalSession()
        
        sql_query = select(
            Data.dataID,
            FormType.form_type,
            FormDate.formatted_date,
            FormDate.formatted_month,
            FormDate.formatted_year,
            FormDate.formatted_time,
            VictimInformation.number_of_victims,
            VictimInformation.victim_age,
            VictimInformation.victim_race,
            VictimInformation.victim_gender,
            PolicePublicRelations.search_reason,
            PolicePublicRelations.type_of_search,
            PolicePublicRelations.additional_notes,
            IncidentAddress.street_name,
            IncidentAddress.town_or_city,
            MapCoordinates.longitude,
            MapCoordinates.latitude,
            PoliceInformation.number_of_police,
            PoliceInformation.obtain_police_info,
            PoliceOfficerInformation.police_badge_number,
            PoliceOfficerInformation.police_officer_name,
            PoliceOfficerInformation.police_station,
            PoliceOfficerInformation.get_additional_officers,
        ).join(
            ReportedBy, Data.dataID==ReportedBy.data_ID 
        ).join(
            FormType, ReportedBy.reportedByID==FormType.formTypeID
        ).join(
            FormDate, ReportedBy.reportedByID==FormDate.formDateID
        ).join(
            VictimInformation, Data.dataID==VictimInformation.data_ID
        ).join(
            PolicePublicRelations, Data.dataID==PolicePublicRelations.data_ID
        ).join(
            IncidentAddress, PolicePublicRelations.policePublicRelationsID==IncidentAddress.incidentAddressID
        ).join(
            MapCoordinates, IncidentAddress.incidentAddressID==MapCoordinates.mapCoordinatesID
        ).join(
            PoliceInformation, Data.dataID==PoliceInformation.data_ID
        ).join(
            PoliceOfficerInformation, PoliceInformation.policeInformationID==PoliceOfficerInformation.policeInformation_ID
        ).where(
            FormType.form_type == form_type
        )
        
        try:
            all_data = session.execute(sql_query).all()
            return all_data
        except Exception as e:
            return {"SQL Error": e}

# get report by year
def search_report_by_year(year: int):
    """
    SELECT data.dataID
           formType.form_type,
           formDate.formatted_date,
           formDate.formatted_month,
           formDate.formatted_year,
           formDate.formatted_time,
           victimInformation.number_of_victims,
           victimInformation.victim_age,
           victimInformation.victim_race,
           victimInformation.victim_gender,
           policePublicRelations.search_reason,
           policePublicRelations.type_of_search,
           policePublicRelations.additional_notes,
           incidentAddress.street_name,
           incidentAddress.town_or_city,
           mapCoordinates.longitude,
           mapCoordinates.latitude,
           policeInformation.number_of_police,
           policeInformation.obtain_police_info,
           policeOfficerInformation.police_badge_number,
           policeOfficerInformation.police_officer_name,
           policeOfficerInformation.police_station,
           policeOfficerInformation.get_additional_officers,
    FROM data
        JOIN reportedBy
            ON data.dataID = reportedBy.reportedByID
        JOIN formType
            ON reportedBy.reportedByID = formType.formTypeID,
        JOIN formDate
            ON reportedBy.reportedByID = formDate.formDateID
        JOIN victimInformation
            ON data.dataID = victimInformation.victimInformationID
        JOIN policePublicRelations
            ON data.dataID = policePublicRelationsID
        JOIN incidentAddress
            ON policePublicRelations.policePublicRelationsID = incidentAddress.incidentAddressID
        JOIN mapCoordinates
            ON incidentAddress.incidentAddressID = mapCoordinates.mapCoordinatesID
        JOIN policeInformation
            ON data.dataID = policeInformation
        JOIN policeOfficerInformation
            ON policeInformation.policeInformationID = policeOfficerInformation.policeOfficerInformationID
    WHERE formDate.formatted_year = :year
    """
    with app.app_context():
        session = LocalSession()
        
        sql_query = select(
            Data.dataID,
            FormType.form_type,
            FormDate.formatted_date,
            FormDate.formatted_month,
            FormDate.formatted_year,
            FormDate.formatted_time,
            VictimInformation.number_of_victims,
            VictimInformation.victim_age,
            VictimInformation.victim_race,
            VictimInformation.victim_gender,
            PolicePublicRelations.search_reason,
            PolicePublicRelations.type_of_search,
            PolicePublicRelations.additional_notes,
            IncidentAddress.street_name,
            IncidentAddress.town_or_city,
            MapCoordinates.longitude,
            MapCoordinates.latitude,
            PoliceInformation.number_of_police,
            PoliceInformation.obtain_police_info,
            PoliceOfficerInformation.police_badge_number,
            PoliceOfficerInformation.police_officer_name,
            PoliceOfficerInformation.police_station,
            PoliceOfficerInformation.get_additional_officers,
        ).join(
            ReportedBy, Data.dataID==ReportedBy.data_ID 
        ).join(
            FormType, ReportedBy.reportedByID==FormType.formTypeID
        ).join(
            FormDate, ReportedBy.reportedByID==FormDate.formDateID
        ).join(
            VictimInformation, Data.dataID==VictimInformation.data_ID
        ).join(
            PolicePublicRelations, Data.dataID==PolicePublicRelations.data_ID
        ).join(
            IncidentAddress, PolicePublicRelations.policePublicRelationsID==IncidentAddress.incidentAddressID
        ).join(
            MapCoordinates, IncidentAddress.incidentAddressID==MapCoordinates.mapCoordinatesID
        ).join(
            PoliceInformation, Data.dataID==PoliceInformation.data_ID
        ).join(
            PoliceOfficerInformation, PoliceInformation.policeInformationID==PoliceOfficerInformation.policeInformation_ID
        ).where(
            FormDate.formatted_year == year
        )
        
        try:
            all_data = session.execute(sql_query).all()
            return all_data
        except Exception as e:
            return {"SQL Error": e}

# get report by date (day, month, year)

# get report by last 30 days
def search_report_by_last_30_days():
    """
    SELECT data.dataID,
       formType.form_type,
       formDate.formatted_date,
       formDate.formatted_month,
       formDate.formatted_year,
       formDate.formatted_time,
       victimInformation.number_of_victims,
       victimInformation.victim_age,
       victimInformation.victim_race,
       victimInformation.victim_gender,
       policePublicRelations.search_reason,
       policePublicRelations.type_of_search,
       policePublicRelations.additional_notes,
       incidentAddress.street_name,
       incidentAddress.town_or_city,
       mapCoordinates.longitude,
       mapCoordinates.latitude,
       policeInformation.number_of_police,
       policeInformation.obtain_police_info,
       policeOfficerInformation.police_badge_number,
       policeOfficerInformation.police_officer_name,
       policeOfficerInformation.police_station,
       policeOfficerInformation.get_additional_officers
    FROM data
        JOIN reportedBy 
            ON data.dataID = reportedBy.reportedByID
        JOIN formType 
            ON reportedBy.reportedByID = formType.formTypeID
        JOIN formDate 
            ON reportedBy.reportedByID = formDate.formDateID
        JOIN victimInformation 
            ON data.dataID = victimInformation.victimInformationID
        JOIN policePublicRelations 
            ON data.dataID = policePublicRelationsID
        JOIN incidentAddress 
            ON policePublicRelations.policePublicRelationsID = incidentAddress.incidentAddressID
        JOIN mapCoordinates
            ON incidentAddress.incidentAddressID = mapCoordinates.mapCoordinatesID
        JOIN policeInformation 
            ON data.dataID = policeInformation
        JOIN policeOfficerInformation 
            ON policeInformation.policeInformationID = policeOfficerInformation.policeOfficerInformationID
    WHERE 
        (formDate.formatted_date >= DATE_SUB(CURDATE(), INTERVAL 1 MONTH)) AND
        (formDate.formatted_year = YEAR(DATE_SUB(CURDATE(), INTERVAL 1 MONTH)));
    """
    import datetime

    with app.app_context():
        session = LocalSession()

        # Calculate the date 1 month ago
        today = datetime.datetime.now()
        one_month_ago = today - datetime.timedelta(days=1*30)  # Assuming 30 days per month
        
        # Adjust year if necessary
        if today.month <= 1:  # If current month is Jan, Feb, or Mar etc
            year = today.year - 1
        else:
            year = today.year
        
        sql_query = select(
            Data.dataID,
            FormType.form_type,
            FormDate.formatted_date,
            FormDate.formatted_month,
            FormDate.formatted_year,
            FormDate.formatted_time,
            VictimInformation.number_of_victims,
            VictimInformation.victim_age,
            VictimInformation.victim_race,
            VictimInformation.victim_gender,
            PolicePublicRelations.search_reason,
            PolicePublicRelations.type_of_search,
            PolicePublicRelations.additional_notes,
            IncidentAddress.street_name,
            IncidentAddress.town_or_city,
            MapCoordinates.longitude,
            MapCoordinates.latitude,
            PoliceInformation.number_of_police,
            PoliceInformation.obtain_police_info,
            PoliceOfficerInformation.police_badge_number,
            PoliceOfficerInformation.police_officer_name,
            PoliceOfficerInformation.police_station,
            PoliceOfficerInformation.get_additional_officers,
        ).join(
            ReportedBy, Data.dataID==ReportedBy.data_ID 
        ).join(
            FormType, ReportedBy.reportedByID==FormType.formTypeID
        ).join(
            FormDate, ReportedBy.reportedByID==FormDate.formDateID
        ).join(
            VictimInformation, Data.dataID==VictimInformation.data_ID
        ).join(
            PolicePublicRelations, Data.dataID==PolicePublicRelations.data_ID
        ).join(
            IncidentAddress, PolicePublicRelations.policePublicRelationsID==IncidentAddress.incidentAddressID
        ).join(
            MapCoordinates, IncidentAddress.incidentAddressID==MapCoordinates.mapCoordinatesID
        ).join(
            PoliceInformation, Data.dataID==PoliceInformation.data_ID
        ).join(
            PoliceOfficerInformation, PoliceInformation.policeInformationID==PoliceOfficerInformation.policeInformation_ID
        ).where(
            (FormDate.formatted_year == year) &
            (FormDate.formatted_date >= one_month_ago)
        )
        
        try:
            all_data = session.execute(sql_query).all()
            return all_data
        except Exception as e:
            return {"SQL Error": e}

# get report by last 3 months + year (-1 year if month past Jan - 0, -1, -2 etc)
def search_report_by_last_90_days():
    """
    SELECT data.dataID,
       formType.form_type,
       formDate.formatted_date,
       formDate.formatted_month,
       formDate.formatted_year,
       formDate.formatted_time,
       victimInformation.number_of_victims,
       victimInformation.victim_age,
       victimInformation.victim_race,
       victimInformation.victim_gender,
       policePublicRelations.search_reason,
       policePublicRelations.type_of_search,
       policePublicRelations.additional_notes,
       incidentAddress.street_name,
       incidentAddress.town_or_city,
       mapCoordinates.longitude,
       mapCoordinates.latitude,
       policeInformation.number_of_police,
       policeInformation.obtain_police_info,
       policeOfficerInformation.police_badge_number,
       policeOfficerInformation.police_officer_name,
       policeOfficerInformation.police_station,
       policeOfficerInformation.get_additional_officers
    FROM data
        JOIN reportedBy 
            ON data.dataID = reportedBy.reportedByID
        JOIN formType 
            ON reportedBy.reportedByID = formType.formTypeID
        JOIN formDate 
            ON reportedBy.reportedByID = formDate.formDateID
        JOIN victimInformation 
            ON data.dataID = victimInformation.victimInformationID
        JOIN policePublicRelations 
            ON data.dataID = policePublicRelationsID
        JOIN incidentAddress 
            ON policePublicRelations.policePublicRelationsID = incidentAddress.incidentAddressID
        JOIN mapCoordinates
            ON incidentAddress.incidentAddressID = mapCoordinates.mapCoordinatesID
        JOIN policeInformation 
            ON data.dataID = policeInformation
        JOIN policeOfficerInformation 
            ON policeInformation.policeInformationID = policeOfficerInformation.policeOfficerInformationID
    WHERE 
        (formDate.formatted_date >= DATE_SUB(CURDATE(), INTERVAL 3 MONTH)) AND
        (formDate.formatted_year = YEAR(DATE_SUB(CURDATE(), INTERVAL 3 MONTH)));
    """
    import datetime

    with app.app_context():
        session = LocalSession()

        # Calculate the date 3 months ago
        today = datetime.datetime.now()
        three_months_ago = today - datetime.timedelta(days=3*30)  # Assuming 30 days per month
        
        # Adjust year if necessary
        if today.month <= 3:  # If current month is Jan, Feb, or Mar
            year = today.year - 1
        else:
            year = today.year
        
        sql_query = select(
            Data.dataID,
            FormType.form_type,
            FormDate.formatted_date,
            FormDate.formatted_month,
            FormDate.formatted_year,
            FormDate.formatted_time,
            VictimInformation.number_of_victims,
            VictimInformation.victim_age,
            VictimInformation.victim_race,
            VictimInformation.victim_gender,
            PolicePublicRelations.search_reason,
            PolicePublicRelations.type_of_search,
            PolicePublicRelations.additional_notes,
            IncidentAddress.street_name,
            IncidentAddress.town_or_city,
            MapCoordinates.longitude,
            MapCoordinates.latitude,
            PoliceInformation.number_of_police,
            PoliceInformation.obtain_police_info,
            PoliceOfficerInformation.police_badge_number,
            PoliceOfficerInformation.police_officer_name,
            PoliceOfficerInformation.police_station,
            PoliceOfficerInformation.get_additional_officers,
        ).join(
            ReportedBy, Data.dataID==ReportedBy.data_ID 
        ).join(
            FormType, ReportedBy.reportedByID==FormType.formTypeID
        ).join(
            FormDate, ReportedBy.reportedByID==FormDate.formDateID
        ).join(
            VictimInformation, Data.dataID==VictimInformation.data_ID
        ).join(
            PolicePublicRelations, Data.dataID==PolicePublicRelations.data_ID
        ).join(
            IncidentAddress, PolicePublicRelations.policePublicRelationsID==IncidentAddress.incidentAddressID
        ).join(
            MapCoordinates, IncidentAddress.incidentAddressID==MapCoordinates.mapCoordinatesID
        ).join(
            PoliceInformation, Data.dataID==PoliceInformation.data_ID
        ).join(
            PoliceOfficerInformation, PoliceInformation.policeInformationID==PoliceOfficerInformation.policeInformation_ID
        ).where(
            (FormDate.formatted_year == year) &
            (FormDate.formatted_date >= three_months_ago)
        )
        
        try:
            all_data = session.execute(sql_query).all()
            return all_data
        except Exception as e:
            return {"SQL Error": e}

# get report by last 6 months
def search_report_last_6_months():
    """
    SELECT data.dataID,
       formType.form_type,
       formDate.formatted_date,
       formDate.formatted_month,
       formDate.formatted_year,
       formDate.formatted_time,
       victimInformation.number_of_victims,
       victimInformation.victim_age,
       victimInformation.victim_race,
       victimInformation.victim_gender,
       policePublicRelations.search_reason,
       policePublicRelations.type_of_search,
       policePublicRelations.additional_notes,
       incidentAddress.street_name,
       incidentAddress.town_or_city,
       mapCoordinates.longitude,
       mapCoordinates.latitude,
       policeInformation.number_of_police,
       policeInformation.obtain_police_info,
       policeOfficerInformation.police_badge_number,
       policeOfficerInformation.police_officer_name,
       policeOfficerInformation.police_station,
       policeOfficerInformation.get_additional_officers
    FROM data
        JOIN reportedBy 
            ON data.dataID = reportedBy.reportedByID
        JOIN formType 
            ON reportedBy.reportedByID = formType.formTypeID
        JOIN formDate 
            ON reportedBy.reportedByID = formDate.formDateID
        JOIN victimInformation 
            ON data.dataID = victimInformation.victimInformationID
        JOIN policePublicRelations 
            ON data.dataID = policePublicRelationsID
        JOIN incidentAddress 
            ON policePublicRelations.policePublicRelationsID = incidentAddress.incidentAddressID
        JOIN mapCoordinates
            ON incidentAddress.incidentAddressID = mapCoordinates.mapCoordinatesID
        JOIN policeInformation 
            ON data.dataID = policeInformation
        JOIN policeOfficerInformation 
            ON policeInformation.policeInformationID = policeOfficerInformation.policeOfficerInformationID
    WHERE 
        (formDate.formatted_date >= DATE_SUB(CURDATE(), INTERVAL 6 MONTH)) AND
        (formDate.formatted_year = YEAR(DATE_SUB(CURDATE(), INTERVAL 6 MONTH)));
    """
    import datetime
    
    with app.app_context():
        session = LocalSession()

        # Calculate the date 6 months ago
        today = datetime.datetime.now()
        six_months_ago = today - datetime.timedelta(days=6*30)  # Assuming 30 days per month
        
        # Adjust year if necessary
        if today.month <= 6:  # If current month is Jan, Feb, Mar, Apr, May, or Jun
            year = today.year - 1
        else:
            year = today.year
        
        sql_query = select(
            Data.dataID,
            FormType.form_type,
            FormDate.formatted_date,
            FormDate.formatted_month,
            FormDate.formatted_year,
            FormDate.formatted_time,
            VictimInformation.number_of_victims,
            VictimInformation.victim_age,
            VictimInformation.victim_race,
            VictimInformation.victim_gender,
            PolicePublicRelations.search_reason,
            PolicePublicRelations.type_of_search,
            PolicePublicRelations.additional_notes,
            IncidentAddress.street_name,
            IncidentAddress.town_or_city,
            MapCoordinates.longitude,
            MapCoordinates.latitude,
            PoliceInformation.number_of_police,
            PoliceInformation.obtain_police_info,
            PoliceOfficerInformation.police_badge_number,
            PoliceOfficerInformation.police_officer_name,
            PoliceOfficerInformation.police_station,
            PoliceOfficerInformation.get_additional_officers,
        ).join(
            ReportedBy, Data.dataID==ReportedBy.data_ID 
        ).join(
            FormType, ReportedBy.reportedByID==FormType.formTypeID
        ).join(
            FormDate, ReportedBy.reportedByID==FormDate.formDateID
        ).join(
            VictimInformation, Data.dataID==VictimInformation.data_ID
        ).join(
            PolicePublicRelations, Data.dataID==PolicePublicRelations.data_ID
        ).join(
            IncidentAddress, PolicePublicRelations.policePublicRelationsID==IncidentAddress.incidentAddressID
        ).join(
            MapCoordinates, IncidentAddress.incidentAddressID==MapCoordinates.mapCoordinatesID
        ).join(
            PoliceInformation, Data.dataID==PoliceInformation.data_ID
        ).join(
            PoliceOfficerInformation, PoliceInformation.policeInformationID==PoliceOfficerInformation.policeInformation_ID
        ).where(
            (FormDate.formatted_year == year) &
            (FormDate.formatted_date >= six_months_ago)
        )
        
        try:
            all_data = session.execute(sql_query).all()
            return all_data
        except Exception as e:
            return {"SQL Error": e}

# get report by last 12 months
def search_report_last_12_months():
    """
    SELECT data.dataID,
       formType.form_type,
       formDate.formatted_date,
       formDate.formatted_month,
       formDate.formatted_year,
       formDate.formatted_time,
       victimInformation.number_of_victims,
       victimInformation.victim_age,
       victimInformation.victim_race,
       victimInformation.victim_gender,
       policePublicRelations.search_reason,
       policePublicRelations.type_of_search,
       policePublicRelations.additional_notes,
       incidentAddress.street_name,
       incidentAddress.town_or_city,
       mapCoordinates.longitude,
       mapCoordinates.latitude,
       policeInformation.number_of_police,
       policeInformation.obtain_police_info,
       policeOfficerInformation.police_badge_number,
       policeOfficerInformation.police_officer_name,
       policeOfficerInformation.police_station,
       policeOfficerInformation.get_additional_officers
    FROM data
        JOIN reportedBy 
            ON data.dataID = reportedBy.reportedByID
        JOIN formType 
            ON reportedBy.reportedByID = formType.formTypeID
        JOIN formDate 
            ON reportedBy.reportedByID = formDate.formDateID
        JOIN victimInformation 
            ON data.dataID = victimInformation.victimInformationID
        JOIN policePublicRelations 
            ON data.dataID = policePublicRelationsID
        JOIN incidentAddress 
            ON policePublicRelations.policePublicRelationsID = incidentAddress.incidentAddressID
        JOIN mapCoordinates
            ON incidentAddress.incidentAddressID = mapCoordinates.mapCoordinatesID
        JOIN policeInformation 
            ON data.dataID = policeInformation
        JOIN policeOfficerInformation 
            ON policeInformation.policeInformationID = policeOfficerInformation.policeOfficerInformationID
    WHERE 
        (formDate.formatted_date >= DATE_SUB(CURDATE(), INTERVAL 12 MONTH)) AND
        (formDate.formatted_year = YEAR(DATE_SUB(CURDATE(), INTERVAL 12 MONTH)));
    """
    import datetime
    
    with app.app_context():
        session = LocalSession()

        # Calculate the date 12 months ago
        today = datetime.datetime.now()
        twelve_months_ago = today - datetime.timedelta(days=12*30)  # Assuming 30 days per month
        
        # Adjust year if necessary
        if today.month <= 12:  # If current month is Jan, Feb, Mar, ..., Nov, or Dec
            year = today.year - 1
        else:
            year = today.year
        
        sql_query = select(
            Data.dataID,
            FormType.form_type,
            FormDate.formatted_date,
            FormDate.formatted_month,
            FormDate.formatted_year,
            FormDate.formatted_time,
            VictimInformation.number_of_victims,
            VictimInformation.victim_age,
            VictimInformation.victim_race,
            VictimInformation.victim_gender,
            PolicePublicRelations.search_reason,
            PolicePublicRelations.type_of_search,
            PolicePublicRelations.additional_notes,
            IncidentAddress.street_name,
            IncidentAddress.town_or_city,
            MapCoordinates.longitude,
            MapCoordinates.latitude,
            PoliceInformation.number_of_police,
            PoliceInformation.obtain_police_info,
            PoliceOfficerInformation.police_badge_number,
            PoliceOfficerInformation.police_officer_name,
            PoliceOfficerInformation.police_station,
            PoliceOfficerInformation.get_additional_officers,
        ).join(
            ReportedBy, Data.dataID==ReportedBy.data_ID 
        ).join(
            FormType, ReportedBy.reportedByID==FormType.formTypeID
        ).join(
            FormDate, ReportedBy.reportedByID==FormDate.formDateID
        ).join(
            VictimInformation, Data.dataID==VictimInformation.data_ID
        ).join(
            PolicePublicRelations, Data.dataID==PolicePublicRelations.data_ID
        ).join(
            IncidentAddress, PolicePublicRelations.policePublicRelationsID==IncidentAddress.incidentAddressID
        ).join(
            MapCoordinates, IncidentAddress.incidentAddressID==MapCoordinates.mapCoordinatesID
        ).join(
            PoliceInformation, Data.dataID==PoliceInformation.data_ID
        ).join(
            PoliceOfficerInformation, PoliceInformation.policeInformationID==PoliceOfficerInformation.policeInformation_ID
        ).where(
            (FormDate.formatted_year == year) &
            (FormDate.formatted_date >= twelve_months_ago)
        )
        
        try:
            all_data = session.execute(sql_query).all()
            return all_data
        except Exception as e:
            return {"SQL Error": e}

# get report by victim age
def search_report_by_victim_age(age: str) -> list[Data]:
    """
    SELECT data.dataID
           formType.form_type,
           formDate.formatted_date,
           formDate.formatted_month,
           formDate.formatted_year,
           formDate.formatted_time,
           victimInformation.number_of_victims,
           victimInformation.victim_age,
           victimInformation.victim_race,
           victimInformation.victim_gender,
           policePublicRelations.search_reason,
           policePublicRelations.type_of_search,
           policePublicRelations.additional_notes,
           incidentAddress.street_name,
           incidentAddress.town_or_city,
           mapCoordinates.longitude,
           mapCoordinates.latitude,
           policeInformation.number_of_police,
           policeInformation.obtain_police_info,
           policeOfficerInformation.police_badge_number,
           policeOfficerInformation.police_officer_name,
           policeOfficerInformation.police_station,
           policeOfficerInformation.get_additional_officers,
    FROM data
        JOIN reportedBy
            ON data.dataID = reportedBy.reportedByID
        JOIN formType
            ON reportedBy.reportedByID = formType.formTypeID,
        JOIN formDate
            ON reportedBy.reportedByID = formDate.formDateID
        JOIN victimInformation
            ON data.dataID = victimInformation.victimInformationID
        JOIN policePublicRelations
            ON data.dataID = policePublicRelationsID
        JOIN incidentAddress
            ON policePublicRelations.policePublicRelationsID = incidentAddress.incidentAddressID
        JOIN mapCoordinates
            ON incidentAddress.incidentAddressID = mapCoordinates.mapCoordinatesID
        JOIN policeInformation
            ON data.dataID = policeInformation
        JOIN policeOfficerInformation
            ON policeInformation.policeInformationID = policeOfficerInformation.policeOfficerInformationID
    WHERE victimInformation.victim_age = :age
    """
    with app.app_context():
        session = LocalSession()
        
        sql_query = select(
            Data.dataID,
            FormType.form_type,
            FormDate.formatted_date,
            FormDate.formatted_month,
            FormDate.formatted_year,
            FormDate.formatted_time,
            VictimInformation.number_of_victims,
            VictimInformation.victim_age,
            VictimInformation.victim_race,
            VictimInformation.victim_gender,
            PolicePublicRelations.search_reason,
            PolicePublicRelations.type_of_search,
            PolicePublicRelations.additional_notes,
            IncidentAddress.street_name,
            IncidentAddress.town_or_city,
            MapCoordinates.longitude,
            MapCoordinates.latitude,
            PoliceInformation.number_of_police,
            PoliceInformation.obtain_police_info,
            PoliceOfficerInformation.police_badge_number,
            PoliceOfficerInformation.police_officer_name,
            PoliceOfficerInformation.police_station,
            PoliceOfficerInformation.get_additional_officers,
        ).join(
            ReportedBy, Data.dataID==ReportedBy.data_ID 
        ).join(
            FormType, ReportedBy.reportedByID==FormType.formTypeID
        ).join(
            FormDate, ReportedBy.reportedByID==FormDate.formDateID
        ).join(
            VictimInformation, Data.dataID==VictimInformation.data_ID
        ).join(
            PolicePublicRelations, Data.dataID==PolicePublicRelations.data_ID
        ).join(
            IncidentAddress, PolicePublicRelations.policePublicRelationsID==IncidentAddress.incidentAddressID
        ).join(
            MapCoordinates, IncidentAddress.incidentAddressID==MapCoordinates.mapCoordinatesID
        ).join(
            PoliceInformation, Data.dataID==PoliceInformation.data_ID
        ).join(
            PoliceOfficerInformation, PoliceInformation.policeInformationID==PoliceOfficerInformation.policeInformation_ID
        ).where(
            VictimInformation.victim_age == age
        )
        
        try:
            all_data = session.execute(sql_query).all()
            return all_data
        except Exception as e:
            return {"SQL Error": e}


# get report by victim gender
def search_report_by_victim_gender(gender: str) -> list[Data]:
    """
    SELECT data.dataID
           formType.form_type,
           formDate.formatted_date,
           formDate.formatted_month,
           formDate.formatted_year,
           formDate.formatted_time,
           victimInformation.number_of_victims,
           victimInformation.victim_age,
           victimInformation.victim_race,
           victimInformation.victim_gender,
           policePublicRelations.search_reason,
           policePublicRelations.type_of_search,
           policePublicRelations.additional_notes,
           incidentAddress.street_name,
           incidentAddress.town_or_city,
           mapCoordinates.longitude,
           mapCoordinates.latitude,
           policeInformation.number_of_police,
           policeInformation.obtain_police_info,
           policeOfficerInformation.police_badge_number,
           policeOfficerInformation.police_officer_name,
           policeOfficerInformation.police_station,
           policeOfficerInformation.get_additional_officers,
    FROM data
        JOIN reportedBy
            ON data.dataID = reportedBy.reportedByID
        JOIN formType
            ON reportedBy.reportedByID = formType.formTypeID,
        JOIN formDate
            ON reportedBy.reportedByID = formDate.formDateID
        JOIN victimInformation
            ON data.dataID = victimInformation.victimInformationID
        JOIN policePublicRelations
            ON data.dataID = policePublicRelationsID
        JOIN incidentAddress
            ON policePublicRelations.policePublicRelationsID = incidentAddress.incidentAddressID
        JOIN mapCoordinates
            ON incidentAddress.incidentAddressID = mapCoordinates.mapCoordinatesID
        JOIN policeInformation
            ON data.dataID = policeInformation
        JOIN policeOfficerInformation
            ON policeInformation.policeInformationID = policeOfficerInformation.policeOfficerInformationID
    WHERE victimInformation.victim_gender = :gender
    """
    with app.app_context():
        session = LocalSession()
        
        sql_query = select(
            Data.dataID,
            FormType.form_type,
            FormDate.formatted_date,
            FormDate.formatted_month,
            FormDate.formatted_year,
            FormDate.formatted_time,
            VictimInformation.number_of_victims,
            VictimInformation.victim_age,
            VictimInformation.victim_race,
            VictimInformation.victim_gender,
            PolicePublicRelations.search_reason,
            PolicePublicRelations.type_of_search,
            PolicePublicRelations.additional_notes,
            IncidentAddress.street_name,
            IncidentAddress.town_or_city,
            MapCoordinates.longitude,
            MapCoordinates.latitude,
            PoliceInformation.number_of_police,
            PoliceInformation.obtain_police_info,
            PoliceOfficerInformation.police_badge_number,
            PoliceOfficerInformation.police_officer_name,
            PoliceOfficerInformation.police_station,
            PoliceOfficerInformation.get_additional_officers,
        ).join(
            ReportedBy, Data.dataID==ReportedBy.data_ID 
        ).join(
            FormType, ReportedBy.reportedByID==FormType.formTypeID
        ).join(
            FormDate, ReportedBy.reportedByID==FormDate.formDateID
        ).join(
            VictimInformation, Data.dataID==VictimInformation.data_ID
        ).join(
            PolicePublicRelations, Data.dataID==PolicePublicRelations.data_ID
        ).join(
            IncidentAddress, PolicePublicRelations.policePublicRelationsID==IncidentAddress.incidentAddressID
        ).join(
            MapCoordinates, IncidentAddress.incidentAddressID==MapCoordinates.mapCoordinatesID
        ).join(
            PoliceInformation, Data.dataID==PoliceInformation.data_ID
        ).join(
            PoliceOfficerInformation, PoliceInformation.policeInformationID==PoliceOfficerInformation.policeInformation_ID
        ).where(
            VictimInformation.victim_gender == gender
        )
        
        try:
            all_data = session.execute(sql_query).all()
            return all_data
        except Exception as e:
            return {"SQL Error": e}

# get report by victim race
def search_report_by_victim_race(race: str) -> list[Data]:
    """
    SELECT data.dataID
           formType.form_type,
           formDate.formatted_date,
           formDate.formatted_month,
           formDate.formatted_year,
           formDate.formatted_time,
           victimInformation.number_of_victims,
           victimInformation.victim_age,
           victimInformation.victim_race,
           victimInformation.victim_gender,
           policePublicRelations.search_reason,
           policePublicRelations.type_of_search,
           policePublicRelations.additional_notes,
           incidentAddress.street_name,
           incidentAddress.town_or_city,
           mapCoordinates.longitude,
           mapCoordinates.latitude,
           policeInformation.number_of_police,
           policeInformation.obtain_police_info,
           policeOfficerInformation.police_badge_number,
           policeOfficerInformation.police_officer_name,
           policeOfficerInformation.police_station,
           policeOfficerInformation.get_additional_officers,
    FROM data
        JOIN reportedBy
            ON data.dataID = reportedBy.reportedByID
        JOIN formType
            ON reportedBy.reportedByID = formType.formTypeID,
        JOIN formDate
            ON reportedBy.reportedByID = formDate.formDateID
        JOIN victimInformation
            ON data.dataID = victimInformation.victimInformationID
        JOIN policePublicRelations
            ON data.dataID = policePublicRelationsID
        JOIN incidentAddress
            ON policePublicRelations.policePublicRelationsID = incidentAddress.incidentAddressID
        JOIN mapCoordinates
            ON incidentAddress.incidentAddressID = mapCoordinates.mapCoordinatesID
        JOIN policeInformation
            ON data.dataID = policeInformation
        JOIN policeOfficerInformation
            ON policeInformation.policeInformationID = policeOfficerInformation.policeOfficerInformationID
    WHERE victimInformation.victim_race = :race
    """
    with app.app_context():
        session = LocalSession()
        
        sql_query = select(
            Data.dataID,
            FormType.form_type,
            FormDate.formatted_date,
            FormDate.formatted_month,
            FormDate.formatted_year,
            FormDate.formatted_time,
            VictimInformation.number_of_victims,
            VictimInformation.victim_age,
            VictimInformation.victim_race,
            VictimInformation.victim_gender,
            PolicePublicRelations.search_reason,
            PolicePublicRelations.type_of_search,
            PolicePublicRelations.additional_notes,
            IncidentAddress.street_name,
            IncidentAddress.town_or_city,
            MapCoordinates.longitude,
            MapCoordinates.latitude,
            PoliceInformation.number_of_police,
            PoliceInformation.obtain_police_info,
            PoliceOfficerInformation.police_badge_number,
            PoliceOfficerInformation.police_officer_name,
            PoliceOfficerInformation.police_station,
            PoliceOfficerInformation.get_additional_officers,
        ).join(
            ReportedBy, Data.dataID==ReportedBy.data_ID 
        ).join(
            FormType, ReportedBy.reportedByID==FormType.formTypeID
        ).join(
            FormDate, ReportedBy.reportedByID==FormDate.formDateID
        ).join(
            VictimInformation, Data.dataID==VictimInformation.data_ID
        ).join(
            PolicePublicRelations, Data.dataID==PolicePublicRelations.data_ID
        ).join(
            IncidentAddress, PolicePublicRelations.policePublicRelationsID==IncidentAddress.incidentAddressID
        ).join(
            MapCoordinates, IncidentAddress.incidentAddressID==MapCoordinates.mapCoordinatesID
        ).join(
            PoliceInformation, Data.dataID==PoliceInformation.data_ID
        ).join(
            PoliceOfficerInformation, PoliceInformation.policeInformationID==PoliceOfficerInformation.policeInformation_ID
        ).where(
            VictimInformation.victim_race == race
        )
        
        try:
            all_data = session.execute(sql_query).all()
            return all_data
        except Exception as e:
            return {"SQL Error": e}


# get report by type of search
def search_report_by_search_type(type_of_search: str) -> list[Data]:
    """
    SELECT data.dataID
           formType.form_type,
           formDate.formatted_date,
           formDate.formatted_month,
           formDate.formatted_year,
           formDate.formatted_time,
           victimInformation.number_of_victims,
           victimInformation.victim_age,
           victimInformation.victim_race,
           victimInformation.victim_gender,
           policePublicRelations.search_reason,
           policePublicRelations.type_of_search,
           policePublicRelations.additional_notes,
           incidentAddress.street_name,
           incidentAddress.town_or_city,
           mapCoordinates.longitude,
           mapCoordinates.latitude,
           policeInformation.number_of_police,
           policeInformation.obtain_police_info,
           policeOfficerInformation.police_badge_number,
           policeOfficerInformation.police_officer_name,
           policeOfficerInformation.police_station,
           policeOfficerInformation.get_additional_officers,
    FROM data
        JOIN reportedBy
            ON data.dataID = reportedBy.reportedByID
        JOIN formType
            ON reportedBy.reportedByID = formType.formTypeID,
        JOIN formDate
            ON reportedBy.reportedByID = formDate.formDateID
        JOIN victimInformation
            ON data.dataID = victimInformation.victimInformationID
        JOIN policePublicRelations
            ON data.dataID = policePublicRelationsID
        JOIN incidentAddress
            ON policePublicRelations.policePublicRelationsID = incidentAddress.incidentAddressID
        JOIN mapCoordinates
            ON incidentAddress.incidentAddressID = mapCoordinates.mapCoordinatesID
        JOIN policeInformation
            ON data.dataID = policeInformation
        JOIN policeOfficerInformation
            ON policeInformation.policeInformationID = policeOfficerInformation.policeOfficerInformationID
    WHERE policePublicRelations.type_of_search = :type_of_search
    """
    with app.app_context():
        session = LocalSession()
        
        sql_query = select(
            Data.dataID,
            FormType.form_type,
            FormDate.formatted_date,
            FormDate.formatted_month,
            FormDate.formatted_year,
            FormDate.formatted_time,
            VictimInformation.number_of_victims,
            VictimInformation.victim_age,
            VictimInformation.victim_race,
            VictimInformation.victim_gender,
            PolicePublicRelations.search_reason,
            PolicePublicRelations.type_of_search,
            PolicePublicRelations.additional_notes,
            IncidentAddress.street_name,
            IncidentAddress.town_or_city,
            MapCoordinates.longitude,
            MapCoordinates.latitude,
            PoliceInformation.number_of_police,
            PoliceInformation.obtain_police_info,
            PoliceOfficerInformation.police_badge_number,
            PoliceOfficerInformation.police_officer_name,
            PoliceOfficerInformation.police_station,
            PoliceOfficerInformation.get_additional_officers,
        ).join(
            ReportedBy, Data.dataID==ReportedBy.data_ID 
        ).join(
            FormType, ReportedBy.reportedByID==FormType.formTypeID
        ).join(
            FormDate, ReportedBy.reportedByID==FormDate.formDateID
        ).join(
            VictimInformation, Data.dataID==VictimInformation.data_ID
        ).join(
            PolicePublicRelations, Data.dataID==PolicePublicRelations.data_ID
        ).join(
            IncidentAddress, PolicePublicRelations.policePublicRelationsID==IncidentAddress.incidentAddressID
        ).join(
            MapCoordinates, IncidentAddress.incidentAddressID==MapCoordinates.mapCoordinatesID
        ).join(
            PoliceInformation, Data.dataID==PoliceInformation.data_ID
        ).join(
            PoliceOfficerInformation, PoliceInformation.policeInformationID==PoliceOfficerInformation.policeInformation_ID
        ).where(
            PolicePublicRelations.type_of_search == type_of_search
        )
        
        try:
            all_data = session.execute(sql_query).all()
            return all_data
        except Exception as e:
            return {"SQL Error": e}

# get report by reason for search
def search_report_by_search_reason(reason_for_search: str) -> list[Data]:
    """
    SELECT data.dataID
           formType.form_type,
           formDate.formatted_date,
           formDate.formatted_month,
           formDate.formatted_year,
           formDate.formatted_time,
           victimInformation.number_of_victims,
           victimInformation.victim_age,
           victimInformation.victim_race,
           victimInformation.victim_gender,
           policePublicRelations.search_reason,
           policePublicRelations.type_of_search,
           policePublicRelations.additional_notes,
           incidentAddress.street_name,
           incidentAddress.town_or_city,
           mapCoordinates.longitude,
           mapCoordinates.latitude,
           policeInformation.number_of_police,
           policeInformation.obtain_police_info,
           policeOfficerInformation.police_badge_number,
           policeOfficerInformation.police_officer_name,
           policeOfficerInformation.police_station,
           policeOfficerInformation.get_additional_officers,
    FROM data
        JOIN reportedBy
            ON data.dataID = reportedBy.reportedByID
        JOIN formType
            ON reportedBy.reportedByID = formType.formTypeID,
        JOIN formDate
            ON reportedBy.reportedByID = formDate.formDateID
        JOIN victimInformation
            ON data.dataID = victimInformation.victimInformationID
        JOIN policePublicRelations
            ON data.dataID = policePublicRelationsID
        JOIN incidentAddress
            ON policePublicRelations.policePublicRelationsID = incidentAddress.incidentAddressID
        JOIN mapCoordinates
            ON incidentAddress.incidentAddressID = mapCoordinates.mapCoordinatesID
        JOIN policeInformation
            ON data.dataID = policeInformation
        JOIN policeOfficerInformation
            ON policeInformation.policeInformationID = policeOfficerInformation.policeOfficerInformationID
    WHERE policePublicRelations.search_reason = :reason_for_search
    """
    with app.app_context():
        session = LocalSession()
        
        sql_query = select(
            Data.dataID,
            FormType.form_type,
            FormDate.formatted_date,
            FormDate.formatted_month,
            FormDate.formatted_year,
            FormDate.formatted_time,
            VictimInformation.number_of_victims,
            VictimInformation.victim_age,
            VictimInformation.victim_race,
            VictimInformation.victim_gender,
            PolicePublicRelations.search_reason,
            PolicePublicRelations.type_of_search,
            PolicePublicRelations.additional_notes,
            IncidentAddress.street_name,
            IncidentAddress.town_or_city,
            MapCoordinates.longitude,
            MapCoordinates.latitude,
            PoliceInformation.number_of_police,
            PoliceInformation.obtain_police_info,
            PoliceOfficerInformation.police_badge_number,
            PoliceOfficerInformation.police_officer_name,
            PoliceOfficerInformation.police_station,
            PoliceOfficerInformation.get_additional_officers,
        ).join(
            ReportedBy, Data.dataID==ReportedBy.data_ID 
        ).join(
            FormType, ReportedBy.reportedByID==FormType.formTypeID
        ).join(
            FormDate, ReportedBy.reportedByID==FormDate.formDateID
        ).join(
            VictimInformation, Data.dataID==VictimInformation.data_ID
        ).join(
            PolicePublicRelations, Data.dataID==PolicePublicRelations.data_ID
        ).join(
            IncidentAddress, PolicePublicRelations.policePublicRelationsID==IncidentAddress.incidentAddressID
        ).join(
            MapCoordinates, IncidentAddress.incidentAddressID==MapCoordinates.mapCoordinatesID
        ).join(
            PoliceInformation, Data.dataID==PoliceInformation.data_ID
        ).join(
            PoliceOfficerInformation, PoliceInformation.policeInformationID==PoliceOfficerInformation.policeInformation_ID
        ).where(
            PolicePublicRelations.search_reason ==  reason_for_search
        )
        
        try:
            all_data = session.execute(sql_query).all()
            return all_data
        except Exception as e:
            return {"SQL Error": e}