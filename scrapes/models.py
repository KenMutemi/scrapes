from sqlalchemy.sql import func

from sqlalchemy.orm import validates
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

DeclarativeBase = declarative_base()

def db_connect():
    """
    Performs database connection using db settings
    in settings.py
    Returns sqlalchemy engine instance
    """

    return create_engine('sqlite:///foo.db')

def create_businesses_table(engine):
    
    DeclarativeBase.metadata.create_all(engine)

class Businesses(DeclarativeBase):
    """Sqlalchemy businesses model"""
    __tablename__ = "businesses"

    id = Column(Integer, primary_key=True)
    title = Column('title', String)
    phone_number = Column('phone_number', String)
    email = Column(String)

    @validates('email')
    def validate_email(self, key, address):
        assert '@' in address
        return address
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
