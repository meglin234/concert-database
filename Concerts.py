import sqlite3

conn = sqlite3.connect('concert_database') 
c = conn.cursor()


c.execute('''
          CREATE TABLE IF NOT EXISTS tHeadliner
          ([concert_id] INTEGER PRIMARY KEY, 
          [artist] TEXT)
          ''')

c.execute('''
          CREATE TABLE IF NOT EXISTS tOpeners
          ([concert_id] INTEGER PRIMARY KEY, 
          [artist] TEXT)
          ''')

c.execute('''
          CREATE TABLE IF NOT EXISTS tConcert
          ([concert_id] INTEGER PRIMARY KEY, 
          [date] TEXT, 
          [venue] TEXT, 
          [day] INTEGER)
          ''')

c.execute('''
          CREATE TABLE IF NOT EXISTS tLocation
          ([venue] TEXT PRIMARY KEY, 
          [city] TEXT, 
          [state] TEXT, 
          [country] TEXT )
          ''')

conn.commit()


