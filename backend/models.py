from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

class Exercise(Base):
    __tablename__ = 'exercises'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String)

class Progress(Base):
    __tablename__ = 'progress'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    exercise_id = Column(Integer, ForeignKey('exercises.id'))
    score = Column(Integer)
    user = relationship("User", back_populates="progress")
    exercise = relationship("Exercise", back_populates="progress")
