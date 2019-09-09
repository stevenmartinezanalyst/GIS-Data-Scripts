import os
import psycopg2

#Credentials for database are stored in .bashrc for security
db_user = os.environ.get('db_user')
db_pass = os.environ.get('db_password')

#Connect to postgres OSM database
conn = psycopg2.connect(user=db_user,password=db_pass, host='localhost',port='5432',database='OSM')

#Cursor
cur = conn.cursor()

#SQL Statement
#Grab Cuba polygons with building values: house, apartments, and residential. Data downloaded from geofabrik and hosted on a postgres database.
cur.execute("SELECT osm_id, name, building, st_astext(ST_Transform(way,4326)) FROM public.planet_osm_polygon WHERE building IN (%s,%s,%s) ORDER BY building,name",("house","apartments","residential"))

print(cur.fetchone())