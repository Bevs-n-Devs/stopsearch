import logging
import datetime
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

# double check the foreign keys - some are not correct (from 2nd onwards)
# check relationships (backref) in models for the correct F.keys

def create_new_report_email(email: str) -> Data: 
    """
    Takes the user email to start the report.
    
    Returns an instance of Data object.
    """
    with app.app_context():
        try:
            session = LocalSession()
            new_report_email = Data(
                report_email = email.lower()
            )
            
            session.add(new_report_email)
            session.commit()
            return new_report_email
        
        except Exception as e:
            return {'SQL Error': e}


def create_new_report_by(confirm_email: str, new_report_email_id: Data) -> ReportedBy:
    """
    Takes the user's confirmation email.
    Table linked to Data via foreign key.
    
    Retruns an instance of ReportBy object.
    """
    # check if email is valid if not return error
    with app.app_context():
        try:
            session = LocalSession()
            new_report_by = ReportedBy(
                confirm_email = confirm_email.lower(),
                reported_by = new_report_email_id,
            )
            
            session.add(new_report_by)
            session.commit()
            return new_report_by
        
        except Exception as e:
            return {'SQL Error': e}


def create_new_form_type(form_type: str, report_by_id: ReportedBy) -> list[FormType]:
    """
    Takes the user's form type (witness or victim).
    Table linked to ReportedBy via foreign key.
    
    Returns an instance of FormType object.
    """
    with app.app_context():
        try:
            session = LocalSession()
            new_form_type = FormType(
                form_type = form_type.lower(),
                fType=report_by_id
            )
            
            session.add(new_form_type)
            session.commit()
            return new_form_type
        
        except Exception as e:
            return {'SQL Error': e}


def create_new_form_date(get_date: str, report_by_id: ReportedBy) -> list[FormDate]:
    """
    Takes the datetime object from the form and converts it into
    a string format.
    Table linked to ReportedBy via foreign key.
    
    Returns an instance of FormDate object.
    """
    import StopSearchUK.utils as utils
    with app.app_context():
        try:
            session = LocalSession()
            datetime_object = get_date
            date_list_obj = utils.convert_datetime_to_string_and_parse_object(form_date=get_date)
            
            
            new_form_date = FormDate(
                form_date = datetime_object[1][0],
                formatted_date = date_list_obj[0][2],
                formatted_weekday = date_list_obj[0][0],
                formatted_month = date_list_obj[0][1],
                formatted_year = date_list_obj[0][4],
                formatted_time = date_list_obj[0][3],
                fDate = report_by_id,
            )
            
            session.add(new_form_date)
            session.commit()
            return new_form_date
        
        except Exception as e:
            return {'SQL Error': e}


def create_new_victim_information(num_victims: str, victim_age: str, victim_gender: str, victim_race: str, new_report_email_id: Data) -> list[VictimInformation]:
    """
    Takes the victim information to store in VictimInformation table.
    Table linked to Data via foreign key.
    
    Returns an instance of VictimInformation object.
    """
    with app.app_context():
        try:
            session = LocalSession()
            new_victim_info = VictimInformation(
                number_of_victims = num_victims,
                victim_age = victim_age,
                victim_gender = victim_gender,
                victim_race = victim_race,
                victim_info = new_report_email_id,
            )
            
            session.add(new_victim_info)
            session.commit()
            return new_victim_info
        
        except Exception as e:
            return {'SQL Error': e}


def create_new_police_public_relations(search_reason: str, search_type: str, notes: str, new_report_email_id: Data) -> list[PolicePublicRelations]:
    """
    This collects interactions between the police and the public and stores it in the PolicePublicRelations table.
    Table linked to Data via foreign key.
    
    Returns an instance of PolicePublicRelations object.
    """
    with app.app_context():
        try:
            session = LocalSession()
            new_police_public_relations = PolicePublicRelations(
                search_reason = search_reason,
                type_of_search = search_type,
                additional_notes = notes,
                police_public = new_report_email_id,
            )
            
            session.add(new_police_public_relations)
            session.commit()
            return new_police_public_relations
    
        except Exception as e:
            return {'SQL Error': e}


def create_new_incident_address(address_type: str, street: str, town_city: str, police_public_id: PolicePublicRelations) -> list[IncidentAddress]:
    """
    This records where the incident took place into the IncidentAddress table.
    Table linked to PolicePublicRelations via foreign key.
    
    Returns an instance of IncidentAddress object.
    """
    with app.app_context():
        try:
            session = LocalSession()
            new_incident_location = IncidentAddress(
                address_type = address_type,
                street_name = street,
                town_or_city = town_city,
                incident_address = police_public_id,
            )
            
            session.add(new_incident_location)
            session.commit()
            return new_incident_location
        
        except Exception as e:
            return {'SQL Error': e}


def create_new_map_coordinates(lat: float, lng: float, incident_address_id: IncidentAddress) -> list[MapCoordinates]:
    """
    This records the lattitude and longitude of the incident address.
    
    Table linked to IncidentAddress viua foreign key.
    
    Returns an instance of MapCoordinates object.
    """
    with app.app_context():
        try:
            session = LocalSession()
            new_map_coordinates = MapCoordinates(
                latitude = lat,
                longitude = lng,
                map_coordinates = incident_address_id,
            )
            
            session.add(new_map_coordinates)
            session.commit()
            return new_map_coordinates
        
        except Exception as e:
            return {'SQL Error': e}


def create_new_report_media(media_path: str, police_public_id: PolicePublicRelations) -> list[FormMedia]:
    """
    This records any report media associated with the report.
    Table linked to PolicePublicRelations via the foreign key.
    
    Returns an instance of FormMedia object.
    """
    with app.app_context():
        try:
            session = LocalSession()
            new_form_media = FormMedia(
                file_path = media_path,
                form_media = police_public_id
            )
            
            session.add(new_form_media)
            session.commit()
            return new_form_media
        
        except Exception as e:
            return {'SQL Error': e}
    

def create_new_police_information(num_police: str, get_police_info: int, new_report_email_id: Data) -> list[PoliceInformation]:
    """
    This records the number of police officers who attended the scene.
    It also records if the user managed to get the police officer's information.
    
    Table linked to Data via foreign key.
    
    Returns an instance of IncidentAddress object.
    """
    with app.app_context():
        session = LocalSession()
        new_police_info = PoliceInformation(
            number_of_police = num_police,
            obtain_police_info = get_police_info,
            police_info = new_report_email_id,
        )
        
        session.add(new_police_info)
        session.commit()
        
    return new_police_info


def create_new_police_officer_information(badge_num: str, police_name: str, police_station: str, more_officers: int, new_police_information_id: PoliceInformation) -> list[PoliceOfficerInformation]:
    """
    This records the individual police officer's information and check if there are any more to store.
    Table linked to PoliceInformation.
    
    Returns an instance of PoliceOfficerInformation object.
    """
    with app.app_context():
        session = LocalSession()
        new_police_officer_information = PoliceOfficerInformation(
            police_badge_number = badge_num,
            police_officer_name = police_name,
            police_station = police_station,
            get_additional_officers = more_officers,
            police_officer_information = new_police_information_id,
        )
        
        session.add(new_police_officer_information)
        session.commit()
        
    return new_police_officer_information



def create_new_additional_officer(badge_num: str, police_name: str, police_station: str, more_officers: bool, new_police_officer_information_id: PoliceOfficerInformation) -> list[AdditionalOfficer]:
    """
    This records any additional officers at the incident and checks if there are any more officers associated with the incident.
    Table inked to the PoliceOfficerInformation.
    
    Returns an instance of AdditionalOfficer instance
    """
    with app.app_context():
        session = LocalSession()
        new_additional_officer = AdditionalOfficer(
            police_badge_number = badge_num,
            police_officer_name = police_name,
            police_station = police_station,
            get_additional_officers = more_officers,
            additional_officer = new_police_officer_information_id,
        )
        
        session.add(new_additional_officer)
        session.commit()
        
    return new_additional_officer



def get_all_reported_by_data() -> list[ReportedBy]:
        """
        SELECT reportedBy.reportedByID,
               reportedBy.confirm_email,
               formType.formTypeID,
               formType.form_type,
               formDate.formDateID,
               formDate.form_date,
               formDate.formatted_date,
               formDate.formatted_weekday,
               formDate.formatted_month,
               formDate.formatted_year,
               formDate.formatted_time,
        FROM reportedBy 
            JOIN formType 
                ON reportedBy.reportedByID = formType.formTypeID
            JOIN formDate
                ON reportedBy.reportedByID = formType.formTypeID
        
        Returns ReportedBy object joined with FormType and FormDate.
        """
        with app.app_context():
            session = LocalSession()
            
            sql_query = select(
                ReportedBy
            ).join(
                FormType, ReportedBy.reportedByID==FormType.formTypeID
            ).join(
                FormDate, ReportedBy.reportedByID==FormDate.formDateID
            )
            
            try:
                all_reported_by_data = session.execute(sql_query).all()
                return all_reported_by_data
            except Exception as e:
                return {"SQL Error": e}


def get_all_victim_information_data() -> list[VictimInformation]:
    """
    SELECT victimInformation.victimInformationID,
           victimInformation.number_of_victims,
           victimInformation.victim_age,
           victimInformation.victim_gender,
           victimInformation.victim_race,
           data.dataID,
           data.report_email,
    FROM victimInformation
        JOIN Data
            ON victimInformation.victimInformationID = data.dataID
    
    Returns VictimInformation obect joined with Data.
    """
    with app.app_context():
        session = LocalSession()
        
        sql_query = select(
            VictimInformation
        ).join(
            Data, VictimInformation.victimInformationID==Data.dataID,
        )
        
        try:
            all_victim_information_data = session.execute(sql_query).all()
            return all_victim_information_data
        except Exception as e:
            return {"SQL Error": e}
    

def get_all_police_public_relations_data() -> list[PolicePublicRelations]:
    """
    SELECT policePublicRelations.policePublicRelationsID,
           policePublicRelations.search_reason, 
           policePublicRelations.type_of_search, 
           policePublicRelations.additional_notes, 
           incidentAddress.incidentAddressID,
           incidentAddress.street_name,
           incidentAddress.town_or_city,
           incidentAddress.country,
           data.dataID,
           data.report_email,
    FROM policePublicRelations
        JOIN incidentAddress
            ON policePublicRelations.policePublicRelationsID = incidentAddress.incidentAddressID
        JOIN data
            ON policePublicRelations.policePublicRelationsID = data.dataID
    
    Returns PolicePublicRelations object joined with IncidentAddress and Data.
    """
    with app.app_context():
        print("Testing")
        session = LocalSession()
        
        sql_query = select(
            PolicePublicRelations
        ).join(
            IncidentAddress, PolicePublicRelations.policePublicRelationsID==IncidentAddress.incidentAddressID,
        ).join(
            Data, PolicePublicRelations.policePublicRelationsID==Data.dataID
        )
        
        try:
            all_police_public_relations_data = session.execute(sql_query).all()
            return all_police_public_relations_data
        except Exception as e:
            return {"SQL Error": e}
    

def get_all_police_information_data() -> list[PoliceInformation]:
    """
    SELECT policeInformation.policeInformationID,
           policeInformation.number_of_police,
           policeInformation.obtain_police_info,
           policeOfficerInformation.policeOfficerInformationID,
           policeOfficerInformation.police_badge_number,
           policeOfficerInformation.police_officer_name,
           policeOfficerInformation.police_station,
           policeOfficerInformation.get_additional_officers,
           additionalOfficer.additionalOfficerID,
           additionalOfficer.police_badge_number,
           additionalOfficer.police_officer_name,
           additionalOfficer.police_station,
           additionalOfficer.get_additional_officers,
           data.dataID,
           data.report_email
    FROM policeInformation
        JOIN policeOfficerInformation
            ON policeInformation.policeInformationID = policeOfficerInformation.policeOfficerInformationID
            JOIN additionalOfficer
                ON policeOfficerInformation.policeOfficerInformationID = additionalOfficer.additionalOfficerID
        JOIN data
            ON policeInformation.policeInformationID = data.dataID
            
    Returns PoliceInformation object joined with PoliceOfficerInformation, AdditionalOfficer and Data.
    """
    with app.app_context():
        session = LocalSession()
        
        sql_query = select(
            PoliceInformation
        ).join(
            PoliceOfficerInformation, PoliceInformation.policeInformationID==PoliceOfficerInformation.policeOfficerInformationID,
        ).join(
            AdditionalOfficer, PoliceOfficerInformation.policeOfficerInformationID==AdditionalOfficer.additionalOfficerID,
        ).join(
            Data, PoliceInformation.policeInformationID==Data.dataID,
        )
        
        try:
            all_police_information_data = session.execute(sql_query).all()
            return all_police_information_data
        except Exception as e:
            return {"SQL Error": e}
    
    
def get_all_data() -> list[Data]:
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
            Data
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

def get_data_by_data_id(dataId: int) -> Data:
    """
    SELECT 
    FROM data
        Where data.dataID = :dataId
        
    Returns Data object
    """
    with app.app_context():
        dataId = int(dataId)
        session = LocalSession()
        
        sql_query = select(
            Data
        ).where(
            Data.dataID==dataId
        )
        
        try:
            get_data = session.execute(sql_query).first()
            return get_data
        except Exception as e:
            return {"SQL Error": e}
        
    