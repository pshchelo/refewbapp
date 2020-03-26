from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String

Base = declarative_base()


class Record(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True)
    uuid = Column(String(50))
    data = Column(String(50), nullable=True)
    host = Column(String(255))


def init(engine):
    Base.metadata.create_all(engine)
