from sqlalchemy import *
from StopSearchUK.utils import *
from StopSearchUK import app
from StopSearchUK.stopsearch_database.extension import LocalSession, init_db
from StopSearchUK.stopsearch_database.models import *
init_db()


# get all map data (report data, address, coordinates)
def get_all_map_data() -> list[Data]:
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
           incidentAddress.street_name,
           incidentAddress.town_or_city,
           mapCoordinates.longitude,
           mapCoordinates.latitude,
           policeInformation.number_of_police,
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

    Returns Data object joined with ReportedBy, FormType, FormDate, VictimInformation, PolicePublicRelations, IncidentAddress, MapCoordinates, PoliceInformation
    """
    with app.app_context():
        sesison = LocalSession()
        

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
            IncidentAddress.street_name,
            IncidentAddress.town_or_city,
            MapCoordinates.latitude,
            MapCoordinates.longitude,
            PoliceInformation.number_of_police
        ).join(
            ReportedBy, Data.dataID==ReportedBy.reportedByID 
        ).join(
            FormType, ReportedBy.reportedByID==FormType.formTypeID
        ).join(
            FormDate, ReportedBy.reportedByID==FormDate.formDateID
        ).join(
            VictimInformation, Data.dataID==VictimInformation.victimInformationID
        ).join(
            PolicePublicRelations, Data.dataID==PolicePublicRelations.policePublicRelationsID
        ).join(
            IncidentAddress, PolicePublicRelations.policePublicRelationsID==IncidentAddress.incidentAddressID
        ).join(
            MapCoordinates, IncidentAddress.incidentAddressID==MapCoordinates.mapCoordinatesID
        ).join(
            PoliceInformation, Data.dataID==PoliceInformation.policeInformationID
        )
            

        try:
            all_map_data = sesison.execute(sql_query).all()
            return all_map_data
        except Exception as e:
                return {"SQL Error": e}



# get all addresses + map coordinates
def get_all_addresses() -> list[IncidentAddress]:
    """
    SELECT incidentAddress.incidentAddressID,
           incidentAddress.address_type,
           incidentAddress.street_name,
           incidentAddress.town_or_city,
           mapCoordinates.mapCoordinatesID,
           mapCoordinates.latitude,
           mapCoordinates.longitude
    FROM incidentAddress
        JOIN mapCoordinates
            ON incidentAddress.incidentAddressID = mapCoordinates.mapCoordinatesID

    Returns IncidentAddress object joined with MapCoordinates.
    """
    with app.app_context():
        session = LocalSession()

        sql_query = select(
            IncidentAddress
        ).join(
            MapCoordinates, IncidentAddress.incidentAddressID==MapCoordinates.mapCoordinatesID
        )

        try:
            all_addresses = session.execute(sql_query).all()
            return all_addresses
        except Exception as e:
            return {"SQL Error": e}

# get address + map by addressID
def get_map_info_by_data_id(data_id: int) -> list[Data]:
    """
    formType (FormType by ReportedBy)
    addressID, steetName, townCity, mapID, long + lat, (IncidentAddress + MapCoordinates)
    formdate (FormDate by ReportedBy)
    typeOfSearch, searchNotes, additionalNotes (PolicePublicRelations)
    numberOfPolice (PoliceInformation)

    SELECT 
    Return Data object joined with ...
    """

# get address + map by dataID

# get all map coordinates
def get_all_map_coordinates() -> list[MapCoordinates]:
    """
    SELECT mapCoordinates.mapCoordinatesID,
           mapCoordinates.latitude,
           mapCoordinates.longitude
    FROM mapCoordinates
    
    Returns MapCoordinates object.
    """
    with app.app_context():
        session = LocalSession()

        sql_query = select(
            MapCoordinates
        )
        
        try:
            all_map_coordinates = session.execute(sql_query).all()
            return all_map_coordinates
        except Exception as e:
            return {"SQL Error": e}

# get map coordinates by mapID
