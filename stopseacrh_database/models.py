from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship
from stopseacrh_database.extensions import Base

# primary database table (top level - Lvl 1)
class Data(Base):
    __tablename__ = 'Data'
    id = Column(Integer, primary_key=True, autoincrement=True)
    # add reportID, authenticationKey etc here for later
    # foreign keys to create relationships with other tables
    reportedBy = relationship('ReportedBy', backref='reportedBy')
    victimInformation = relationship('VictimInformation', backref='victimInformation')
    policePublicRelations = relationship('PolicePublicRelations', backref='policePublicRelations')
    policeInformation = relationship('PoliceInformation', backref='policeInformation')
    
    
# secondary database tables (2nd level - Lvl 2)
class ReportedBy(Base):
    __tablename__ = 'ReportedBy'
    id = Column(Integer, primary_key=True, autoincrement=True)
    formType = relationship('FormType', backref='formType')
    formDate = relationship('FormDate', backref='formDate')
    reportEmail = relationship('FormDate', backref='reportEmail')
    data_ID = Column(Integer, ForeignKey('Data.id'))

class VictimInformation(Base):
    __tablename__ = 'VictimInformation'
    id = Column(Integer, primary_key=True, autoincrement=True)
    numberOfVictims = Column(String(8), nullable=False)
    victimAge = Column(String(8), nullable=False)
    victimGender = Column(String(25), nullable=False)
    victimRace = Column(String(10), nullable=False)
    data_ID = Column(Integer, ForeignKey('Data.id'))
    
class PolicePublicRelations(Base):
    __tablename__ = 'PolicePublicRelations'
    id = Column(Integer, primary_key=True, autoincrement=True)
    incidentAddress = relationship('IncidentAddress', backref='incidentAddress')
    searchReason = Column(String(55), nullable=False)
    TypeOfSearch = Column(String(10), nullable=False)
    additionalNotes = Column(Text, nullable=True)
    data_ID = Column(Integer, ForeignKey('Data.id'))
    
class PoliceInformation(Base):
    __tablename__ = 'PoliceInformation'
    id = Column(Integer, primary_key=True, autoincrement=True)
    numberOfPolice = Column(String(8), nullable=False)
    policeOfficerInformation = relationship('PoliceOfficerInformation', backref='policeOfficerInformation')
    additionalOfficers = relationship('AdditionalOfficers', backref='additionalOfficers')
    data_ID = Column(Integer, ForeignKey('Data.id'))


# Tertiary database tables (3rd level - Lvl 3)
class FormType(Base):
    __tablename__ = 'FormType'
    id = Column(Integer, primary_key=True, autoincrement=True)
    formType = Column(String(9), nullable=False)
    reportedBy_ID = Column(Integer, ForeignKey('ReportedBy.id'))

class FormDate(Base):
    __tablename__ = 'FormDate'
    id = Column(Integer, primary_key=True, autoincrement=True)
    formDate = Column(DateTime, nullable=False)
    formattedDate = Column(String(4), nullable=False)
    formattedMonth = Column(String(9), nullable=False)
    formattedYear = Column(String(4), nullable=False)
    formattedTime = Column(String(8), nullable=False)
    reportedBy_ID = Column(Integer, ForeignKey('ReportedBy.id'))

class IncidentAddress(Base):
    __tablename__= 'IncidentAddress'
    id = Column(Integer, primary_key=True, autoincrement=True)
    streetName = Column(String(50), nullable=False)
    townOrCity = Column(String(50), nullable=False)
    postcode = Column(String(8), nullable=True)
    country = Column(String(50), default='UK')
    policePublicRelations_ID = Column(Integer, ForeignKey('PolicePublicRelations.id'))
    
    
    
# Quaternary database tables (4th level - Lvl 4)
class PoliceOfficerInformation(Base):
    __tablename__ = 'PoliceOfficerInformation'
    id = Column(Integer, primary_key=True, autoincrement=True)
    policeBadgeNumber =  Column(String(1), nullable=False)
    policeOfficerName =  Column(String(1), nullable=True)
    policeStation =  Column(String(1), nullable=True)
    additionalOfficers = Column(String(1), nullable=False) # this is drop down option if they got more than 1 PC details 
    additionalOfficer = relationship('AdditionalOfficer', backref='additionalOfficer')
    policeInformation_ID = Column(Integer, ForeignKey('PoliceInformation.id'))

class AdditionalOfficer(Base):
    __tablename__ = 'AdditionalOfficer'
    id = Column(Integer, primary_key=True, autoincrement=True)
    policeBadgeNumber =  Column(String(1), nullable=False)
    policeOfficerName =  Column(String(1), nullable=True)
    policeStation =  Column(String(1), nullable=True)
    additionalOfficers = Column(String(1), nullable=False) # this is drop down option if they got more than 1 PC details
    policeInformation_ID = Column(Integer, ForeignKey('PoliceInformation.id'))
    policeOfficerInformation_ID = Column(Integer, ForeignKey('PoliceOfficerInformation.id')) # this links primaray officer to addittional officer for each case