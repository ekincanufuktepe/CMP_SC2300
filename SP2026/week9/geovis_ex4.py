import matplotlib.pyplot as plt
import geopandas as gpd
import geodatasets

world = gpd.read_file(geodatasets.get_path("naturalearth.land"))

point = gpd.GeoDataFrame(
    geometry = gpd.points_from_xy([-100], [37]),
    crs = "EPSG:4326"
)

# Convert to meters projection
points_proj = point.to_crs("EPSG:3857")

# Create a buffer (1000 km)

buffer = points_proj.buffer(1000000)
buffer_gdf = gpd.GeoDataFrame(geometry = buffer, crs="EPSG:3857")
buffer_gdf = buffer_gdf.to_crs("EPSG:4326")
ax2 = world.plot(figsize=(15,10), color="gray")
ax = buffer_gdf.plot(ax=ax2, color="lightblue")
ax1 = point.plot(ax=ax, color="red")
plt.title("100 km Buffer Around Point")
plt.show()
