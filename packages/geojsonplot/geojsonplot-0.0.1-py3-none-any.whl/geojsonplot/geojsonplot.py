import contextily as cx
import geopandas

def geojsonplot(geojson: dict):
    inval = str(geojson).replace('\'', '\"')
    db = geopandas.read_file(inval)

    ax = None
    if geojson['type'] == 'Point':
        ax = db.plot(color="red", figsize=(9, 9))
    else:
        ax = db.plot(color="none", edgecolor="red", linewidth=3, figsize=(9, 9))
    
    cx.add_basemap(ax, crs=db.crs.to_string(), source=cx.providers.OpenStreetMap.Mapnik)
    
    return ax
