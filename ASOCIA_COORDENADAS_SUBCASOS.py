
import pandas as pd
import numpy as np


df_latlon=pd.read_csv('/Users/Pablo/Desktop/CELDAS_LAT_LON.csv')
df_subcasos=pd.read_csv('/Users/Pablo/Downloads/incidencias.csv',delimiter=';')

df_latlon.set_index("NODE_ID",drop=True,inplace=True)

df_subcasos.set_index("Nodo",drop=True,inplace=True)

df_subcasos=df_subcasos.dropna()


dict_lat_lon=df_latlon.to_dict(orient="index")
dict_subcasos=df_subcasos.to_dict(orient="index")

latitudes=[]
longitudes=[]

for index,row in df_subcasos.iterrows():
    try:
        latitudes.append(dict_lat_lon[index]['LATITUDE'])
    except: latitudes.append('NA')
    try:
        longitudes.append(dict_lat_lon[index]['LONGITUDE'])
    except: longitudes.append('NA')

df_subcasos['LAT']=latitudes
df_subcasos['LON']=longitudes

df_subcasos.to_csv('/Users/Pablo/Desktop/subcasos_lat_lon.csv')

print df_subcasos.head()