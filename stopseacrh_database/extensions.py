import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
load_dotenv()

engine: create_engine = create_engine(os.environ["STOPSEARCH_DB"])
db_session: scoped_session = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine
    )
)
LocalSession: sessionmaker = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
Base: declarative_base = declarative_base()
Base.query = db_session.query_property()

# initialise database
def init_db():
    import stopseacrh_database.models
    Base.metadata.create_all(bind=engine)
    