import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String,Boolean,Table
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

favorites=Table(
    "favorites",
    Base.metadata,
    Column("user.id",ForeignKey("user.id")),
    Column("planet.id",ForeignKey("planet.id")),
    Column("character.id",ForeignKey("character.id"))
)

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(40), nullable=False, unique=True)
    password = Column(String(10), nullable=False)

    planets = relationship('Planet',secondary=favorites, back_populates='user')
    characters = relationship('Character',secondary=favorites, back_populates='user')


class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    description = Column(String(250),nullable=False)
    climate = Column(String(50))

    user = relationship('User',secondary=favorites, back_populates='planet')
    characters = relationship('Character',secondary=favorites, back_populates='planet')
    


class Character(Base):
    __tablename__='character'
    id = Column(Integer, primary_key=True)
    name = Column(String(50),nullable=False)
    alive = Column(Boolean,nullable=False)

    user = relationship('User',secondary=favorites, back_populates='character')
    planets = relationship('Planet',secondary=favorites, back_populates='character')





## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
