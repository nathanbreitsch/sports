from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Team, Athlete

engine = create_engine('sqlite:///sports.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

osu = Team(name = "Buckeyes",
            city = "Columbus",
            state = "Ohio")

bama = Team(name = "Alabama",
            city = "Who",
            state = "Cares")

file = open("data/osu_roster.csv","r")
for line in file.readlines():
    words = line.split("\t")
    (last_name, first_name) = words[2].split(",")
    first_name = first_name.strip()
    position = words[3]
    

file.close()

session.add(evan)
session.add(nathan)
session.add(brian)
session.add(breitsch_bros)
session.commit()
print(session.query(Team).all())
print(session.query(Athlete).all())
