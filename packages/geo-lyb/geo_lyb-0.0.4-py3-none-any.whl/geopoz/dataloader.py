import geopandas as gpd

def load_data():
    # Load ames.geojson file
    data = gpd.read_file('./data/ames.geojson')
    
    return data
