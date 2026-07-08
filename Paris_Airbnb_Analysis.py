import geopandas as gpd
import pandas as pd


df = pd.read_csv("Listing_AirBnB_Paris.csv")


df = df.dropna(subset=['latitude', 'longitude', 'price'])
gdf = gpd.GeoDataFrame(
    df,
    geometry=gpd.points_from_xy(df['longitude'], df['latitude']),
    crs="EPSG:4326"
)

gdf.to_file("paris_airbnb_real.geojson", driver="GeoJSON")
