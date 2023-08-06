import contextily as cx
import geopandas
import matplotlib.pyplot as plt 
import pandas as pd

def _concat(gpd, geojson: dict):
    inval = str(geojson).replace('\'', '\"')
    return pd.concat([gpd, geopandas.read_file(inval)])

def plot(geojson):
    gpd = geopandas.GeoDataFrame()
    if type(geojson) is list:
        for item in geojson:
            gpd = _concat(gpd, item)
    elif type(geojson) is dict:
        gpd = _concat(gpd, geojson)
    
    ax = gpd.plot(color="none", edgecolor="red", linewidth=3, figsize=(6, 4))

    # print(gpd)
    cx.add_basemap(ax, crs=gpd.crs.to_string(), source=cx.providers.OpenStreetMap.Mapnik)
    
    return ax
