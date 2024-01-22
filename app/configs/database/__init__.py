from .database_credentials import DatabaseCredentials
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

credentials = DatabaseCredentials()

__engine__ = create_engine(credentials.connection_str)

Session = sessionmaker(
    bind=__engine__,
    autocommit=False,
    autoflush=False
)

Base = declarative_base()

def get_session():
    session = scoped_session(Session)
    try:
        yield session
    except Exception as e:
        print(e)
        session.rollback()
    finally:
        session.close()