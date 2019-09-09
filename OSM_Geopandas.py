import os
import psycopg2
import geopandas as gpd

#Credentials for database are stored in .bashrc for security
db_user = os.environ.get('db_user')
db_pass = os.environ.get('db_password')

#Connect to postgres OSM database
conn = psycopg2.connect(user=db_user,password=db_pass, host='localhost',port='5432',database='OSM')

#SQL Statement
#Grab Cuba polygons with building values: house, apartments, and residential. Data downloaded from geofabrik and hosted on a postgres database.
sql = "SELECT osm_id, name, building, way as way FROM public.planet_osm_polygon WHERE building IN ('house','apartments','residential') ORDER BY building,name"

df = gpd.GeoDataFrame.from_postgis(sql, conn, geom_col='way' )

print(df.head())