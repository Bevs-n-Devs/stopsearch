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
def search_all_reports() -> list[Data ]:
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
           additionalOfficer.police_badge_number,
           additionalOfficer.police_officer_name,
           additionalOfficer.police_station,
           additionalOfficer.get_additional_officers
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
        JOIN  additionalOfficers
            ON policeOfficerInformation.policeOfficerInformationID = additionalOfficers.additionalOfficersID
    
    Returns Data object joined with ReportedBy, VictimInformation, PolicePublicRelations, PoliceInformation, PoliceOfficerInformation, AdditionalOfficer.
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
            AdditionalOfficer.police_badge_number,
            AdditionalOfficer.police_officer_name,
            AdditionalOfficer.police_station,
            AdditionalOfficer.get_additional_officers
            # add data object here 
        ).join(
            ReportedBy, Data.dataID==ReportedBy.reportedByID,
        ).join(
            FormType, ReportedBy.reportedByID==FormType.formTypeID 
        ).join(
            FormDate, ReportedBy.reportedByID==FormDate.formDateID
        ).join(
            VictimInformation, Data.dataID==VictimInformation.victimInformationID
        ).join(
            PolicePublicRelations, Data.dataID==PolicePublicRelations.policePublicRelationsID
        ).join(
            IncidentAddress, PoliceInformation.policeInformationID==IncidentAddress.incidentAddressID
        ).join(
            MapCoordinates, IncidentAddress.incidentAddressID==MapCoordinates.mapCoordinatesID
        ).join(
            PoliceInformation, Data.dataID==PoliceInformation.policeInformationID
        ).join(
            PoliceOfficerInformation, Data.dataID==PoliceOfficerInformation.policeOfficerInformationID
        ).join(
            AdditionalOfficer, PoliceOfficerInformation.policeOfficerInformationID==AdditionalOfficer.additionalOfficerID
        )
        
        try:
            all_data = session.execute(sql_query).all()
            return all_data
        except Exception as e:
            return {"SQL Error": e}

# get report data by Data.dataID

# get report by FormType.form_type

# get report by year

# get report by date (day, month, year)

# get report by last 3 months

# get report by last 6 months

# get report by last 12 months

# get report by victim age

# get report by victim gender

# get report by victim race

# get report by type of search

# get report by reason for search