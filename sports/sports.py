from flask import Flask, request, jsonify
app = Flask(__name__)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Team, Athlete

engine = create_engine('sqlite:///sports.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

@app.route('/api/athletes')
def getAthletes():
    athletes = session.query(Athlete).all()
    return jsonify(athletes = [a.serialize for a in athletes])

@app.route('/api/teams')
def getTeams():
    teams = session.query(Team).all()
    return jsonify(teams = [t.serialize for t in teams])

if __name__ == '__main__':
    app.debug = True
    app.run(host = '127.0.0.1', port=1337)
