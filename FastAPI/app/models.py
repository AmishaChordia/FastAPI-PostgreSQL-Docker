from .database import Base
from sqlalchemy import Column, String, Boolean, Integer


class DeviceInfo(Base):
    __tablename__ = 'DeviceInfo'
    token = Column(String, primary_key = True)
    username = Column(String, default = 'user')


class Configuration(Base):
    __tablename__ = 'Configuration'
    id = Column(Integer, primary_key = True, autoincrement = True)
    modelUrl = Column(String)
    frequency = Column(Integer)
    federated = Column(Boolean)
