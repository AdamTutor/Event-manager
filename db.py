
import psycopg2

def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=schedule")

def deleteEvents():
    """Remove all the events from the database."""
    DB = connect()
    cursor = DB.cursor()
    cursor.execute("DELETE FROM events;");
    DB.commit()
    DB.close()

def deleteTeams():
    """delete teams from teams table in database"""
    DB = connect()
    cursor = DB.cursor()
    cursor.execute("DELETE FROM teams;");
    DB.commit()
    DB.close()

def countEvents():
    """Returns the number of events currently registered."""
    DB = connect()
    cursor = DB.cursor()
    cursor.execute("SELECT count(*) as num FROM events;")
    result = int(cursor.fetchone()[0])
    DB.close()
    return result

def registerEvent(t1, t2, dt, type):
    """Adds a new event to the Schedule database.

    The database assigns a unique serial id number for the event.

    Args:
      Team1, team2, datetime, and event type(clan war, arcade night, etc.).
    """
    DB = connect()
    cursor = DB.cursor()
    cursor.execute("INSERT INTO events (team1, team2, datetime, type) VALUES ( %s , %s , %s , %s );",
    (t1, t2, dt, type))
    DB.commit()
    DB.close()

def registerTeam(name):
    """Adds a new team to the database."""
    DB = connect()
    cursor = DB.cursor()
    cursor.execute("INSERT INTO teams (name) VALUES (%s);",
    (name,))
    DB.commit()
    DB.close()

def allEvents():
    DB = connect()
    cursor = DB.cursor()
    cursor.execute("SELECT * FROM events;")
    events = cursor.fetchall()
    DB.commit()
    DB.close()
    print(events)
    return events

def allTeams():
    DB = connect()
    cursor = DB.cursor()
    cursor.execute("SELECT * FROM teams;")
    teams = cursor.fetchall()
    DB.commit()
    DB.close()
    print(teams)
    return teams
allEvents()
allTeams()
