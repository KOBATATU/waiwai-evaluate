from sqlalchemy import UniqueConstraint, Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import uuid
from datetime import datetime

Base = declarative_base()

def generate_uuid():
    return str(uuid.uuid4())


class Session(Base):
    __tablename__ = 'Session'

    id = Column(String, primary_key=True, default=generate_uuid)
    sessionToken = Column(String, unique=True, nullable=False)
    expires = Column(DateTime, nullable=False)

    userId = Column(String, ForeignKey('User.id'), nullable=False)
    user = relationship('User', back_populates='sessions')


class User(Base):
    __tablename__ = 'User'

    id = Column(String, primary_key=True, default=generate_uuid)

    sessions = relationship('Session', back_populates='user')

class Competition(Base):
    __tablename__ = 'Competition'
    id = Column(String, primary_key=True, default=generate_uuid)
    evaluation_func = Column(String, unique=True, nullable=False)