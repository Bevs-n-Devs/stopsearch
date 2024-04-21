from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey, Float
from sqlalchemy.orm import relationship
from StopSearchUK.stopsearch_database.extension import Base

# primary database table (top level - Lvl 1)
class Data(Base):
    __tablename__ = 'data'
    dataID = Column(Integer, primary_key=True, autoincrement=True)
    # add reportID, authenticationKey etc here for later
    # foreign keys to create relationships with other tables
    report_email = Column(String(255), nullable=False, unique=False)
    reported_by = relationship('ReportedBy', backref='reported_by')
    victim_information = relationship('VictimInformation', backref='victim_info')
    police_public_relations = relationship('PolicePublicRelations', backref='police_public')
    police_information = relationship('PoliceInformation', backref='police_info')
    
    
# secondary database tables (2nd level - Lvl 2)
class ReportedBy(Base):
    __tablename__ = 'reportedBy'
    reportedByID = Column(Integer, primary_key=True, autoincrement=True)
    confirm_email = Column(String(255), nullable=False, unique=False)
    form_type = relationship('FormType', backref='fType')
    form_date = relationship('FormDate', backref='fDate')
    data_ID = Column(Integer, ForeignKey('data.dataID'))

class VictimInformation(Base):
    __tablename__ = 'victimInformation'
    victimInformationID = Column(Integer, primary_key=True, autoincrement=True)
    number_of_victims = Column(String(8), nullable=False)
    victim_age = Column(String(8), nullable=False)
    victim_gender = Column(String(25), nullable=False)
    victim_race = Column(String(10), nullable=False)
    data_ID = Column(Integer, ForeignKey('data.dataID'))
    
class PolicePublicRelations(Base):
    __tablename__ = 'policePublicRelations'
    policePublicRelationsID = Column(Integer, primary_key=True, autoincrement=True)
    search_reason = Column(String(55), nullable=False)
    type_of_search = Column(String(10), nullable=False)
    additional_notes = Column(Text, nullable=True)
    incident_address = relationship('IncidentAddress', backref='incident_address')
    form_media = relationship('FormMedia', backref='form_media')
    data_ID = Column(Integer, ForeignKey('data.dataID'))
    
class PoliceInformation(Base):
    __tablename__ = 'policeInformation'
    policeInformationID = Column(Integer, primary_key=True, autoincrement=True)
    number_of_police = Column(String(8), nullable=False)
    obtain_police_info = Column(Integer, nullable=False) # 0 = False, 1 = True
    police_officer_information = relationship('PoliceOfficerInformation', backref='police_officer_information')
    data_ID = Column(Integer, ForeignKey('data.dataID'))


# Tertiary database tables (3rd level - Lvl 3)
class FormType(Base):
    __tablename__ = 'formType'
    formTypeID = Column(Integer, primary_key=True, autoincrement=True)
    form_type = Column(String(9), nullable=False)
    reportedBy_ID = Column(Integer, ForeignKey('reportedBy.reportedByID'))

class FormDate(Base):
    __tablename__ = 'formDate'
    formDateID = Column(Integer, primary_key=True, autoincrement=True)
    form_date = Column(String(20), nullable=False)
    formatted_date = Column(String(4), nullable=False)
    formatted_weekday = Column(String(9), nullable=False)
    formatted_month = Column(String(9), nullable=False)
    formatted_year = Column(String(4), nullable=False)
    formatted_time = Column(String(8), nullable=False)
    reportedBy_ID = Column(Integer, ForeignKey('reportedBy.reportedByID'))

class IncidentAddress(Base):
    __tablename__= 'incidentAddress'
    incidentAddressID = Column(Integer, primary_key=True, autoincrement=True)
    address_type = Column(String(16), nullable=False)  # automaticAddress or manualAddress
    street_name = Column(String(50), nullable=False)
    town_or_city = Column(String(50), nullable=False)
    country = Column(String(50), default='UK')
    map_coordinates = relationship('MapCoordinates', backref='map_coordinates')
    policePublicRelations_ID = Column(Integer, ForeignKey('policePublicRelations.policePublicRelationsID'))

class FormMedia(Base):
    __tablename__ = 'formMedia'
    formMediaID = Column(Integer, primary_key=True, autoincrement=True)
    file_path = Column(String, nullable=True, unique=True)
    policePublicRelations_ID = Column(Integer, ForeignKey('policePublicRelations.policePublicRelationsID'))
    
    
    
# Quaternary database tables (4th level - Lvl 4)
class PoliceOfficerInformation(Base):
    __tablename__ = 'policeOfficerInformation'
    policeOfficerInformationID = Column(Integer, primary_key=True, autoincrement=True)
    police_badge_number =  Column(String(10), nullable=True)
    police_officer_name =  Column(String(50), nullable=True)
    police_station =  Column(String(50), nullable=True)
    get_additional_officers = Column(String(3), nullable=False) # yes or no
    additional_officer = relationship('AdditionalOfficer', backref='additional_officer')
    policeInformation_ID = Column(Integer, ForeignKey('policeInformation.policeInformationID'))
    
class MapCoordinates(Base):
    __tablename__ = 'mapCoordinates'
    mapCoordinatesID = Column(Integer, primary_key=True, autoincrement=True)
    longitude = Column(Float, nullable=False)
    latitude = Column(Float, nullable=False)
    incidentAddressID = Column(Integer, ForeignKey('incidentAddress.incidentAddressID'))



# Level 5 database tables
class AdditionalOfficer(Base):
    __tablename__ = 'additionalOfficer'
    additionalOfficerID = Column(Integer, primary_key=True, autoincrement=True)
    police_badge_number =  Column(String(10), nullable=True)
    police_officer_name =  Column(String(50), nullable=True)
    police_station =  Column(String(50), nullable=True)
    get_additional_officers = Column(Integer, nullable=False) # 0 = False, 1 = True
    policeInformation_ID = Column(Integer, ForeignKey('policeOfficerInformation.policeOfficerInformationID'))