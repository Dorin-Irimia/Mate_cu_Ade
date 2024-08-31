import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

DATABASE_URL = os.getenv('MateCuAde', 'postgresql://matecuade_user:2zEdyxbPD5oi76Ac3vVRgGxRES0XEp7R@dpg-cr9j103v2p9s73b90b4g-a/matecuade')

engine = create_engine(DATABASE_URL)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    import models
    Base.metadata.create_all(bind=engine)
