from sqlalchemy import *
from StopSearchUK.utils import *
from StopSearchUK import app
from StopSearchUK.stopsearch_database.extension import LocalSession, init_db
from StopSearchUK.stopsearch_database.models import *
init_db()



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
        FROM mapCoordinates
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
