import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Team(Base):
    __tablename__ = 'team'
    id = Column(Integer, primary_key = True)

    name = Column(String(80), nullable = False)
    city = Column(String(80), nullable = False)
    state = Column(String(2), nullable = False)

    @property
    def serialize(self):
        return{
            'name': self.name,
            'city': self.city,
            'state': self.state
        }


class Athlete(Base):
    __tablename__ = 'athlete'
    id = Column(Integer, primary_key = True)
    team_id = Column(Integer, ForeignKey('team.id'))

    first_name = Column(String(80), nullable = False)
    last_name = Column(String(80), nullable = False)

    team = relationship(Team)

    @property
    def serialize(self):
        return{
            'first_name': self.first_name,
            'last_name': self.last_name,
            'team_name': self.team.name,
            'team_id': self.team.id
        }


engine = create_engine('sqlite:///sports.db')
Base.metadata.create_all(engine)
