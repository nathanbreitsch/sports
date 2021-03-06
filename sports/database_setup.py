import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Team(Base):
    __tablename__ = 'Team'
    id = Column(Integer, primary_key = True)
    name = Column(String(80), nullable = False)
    city = Column(String(80))
    state = Column(String(2))

    @property
    def serialize(self):
        return{
            'id': self.id,
            'name': self.name,
            'city': self.city,
            'state': self.state
        }

class Athlete(Base):
    __tablename__ = 'Athlete'
    id = Column(Integer, primary_key = True)
    team_id = Column(Integer, ForeignKey('Team.id'), nullable=False)
    team = relationship(Team)
    first_name = Column(String(80), nullable = False)
    last_name = Column(String(80), nullable = False)

    @property
    def serialize(self):
        return{
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'team_name': self.team.name,
            'team_id': self.team.id
        }

class Game(Base):
    __tablename__ = 'Game'
    id = Column(Integer, primary_key = True)

    home_team_id = Column(Integer, ForeignKey('Team.id'), nullable = False)
    home_team = relationship(Team)
    away_team_id = Column(Integer, ForeignKey('Team.id'), nullable = False)
    away_team = relationship(Team)
    datetime = Column(DateTime)
    location = Column(String(80))

    @property
    def serialize(self):
        return{
            'id': self.id,
            'home_team_id': self.home_team_id,
            'away_team_id': self.away_team_id,
            'datetime': self.datetime,
            'location': self.location
        }

class Play(Base):
    __tablename__ = 'Play'

    id = Column(Integer, primary_key = True)

    play_index = Column(Integer, nullable = False)
    quarter_index = Column(Integer, nullable = False)
    down = Column(Integer, nullable = False)
    offense_id = Column(Integer, ForeignKey('Team.id'), nullable = False)
    offense = relationship(Team)
    defense_id = Column(Integer, ForeignKey('Team.id'), nullable = False)
    defense = relationship(Team)
    half = Column(Boolean)
    yards = Column(Integer)
    result = Column(String(40))

    @property
    def serialize(self):
        return{
            'id': self.id,
            'play_index': self.play_index,
            'quarter_index': self.quarter_index,
            'down': self.down,
            'offense_id': self.offense_id,
            'defense_id': self.defense_id,
            'half': self.half,
            'yards': self.yards,
            'result': self.result
        }

class Action(Base):
    __tablename__ = 'Action'

    id = Column(Integer, primary_key = True)
    player_id = Column(Integer, primary_key = True)
    player = relationship(Athlete)

    @property
    def serialize(self):
        return{
            'id': self.id,
            'player_id': self.away_team_id
        }

class Observation(Base):
    __tablename__ = 'Observation'

    id = Column(Integer, primary_key = True)
    action_id = Column(Integer, primary_key = True)
    action = relationship(Action)
    name = Column(String(40))
    value = Column(String(80))

    @property
    def serialize(self):
        return{
            'id': self.id,
            'action_id': self.action_id,
            'name': self.name,
            'value': self.value
        }


engine = create_engine('sqlite:///sports.db')
Base.metadata.create_all(engine)
