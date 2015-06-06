from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Team, Athlete

engine = create_engine('sqlite:///sports.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

breitsch_bros = Team(name = "Breitsch Bros",
                    city = "Chagrin Falls",
                    state = "Ohio")

evan = Athlete(first_name = "Evan", last_name = "Breitsch", team = breitsch_bros)
nathan = Athlete(first_name = "Nathan", last_name = "Breitsch", team = breitsch_bros)
brian = Athlete(first_name = "Brian", last_name = "Breitsch", team = breitsch_bros)
session.add(evan)
session.add(nathan)
session.add(brian)
session.add(breitsch_bros)
session.commit()
print(session.query(Team).all())
print(session.query(Athlete).all())
