import matplotlib.pyplot as plt
import geopandas as gpd
import geodatasets

world = gpd.read_file(geodatasets.get_path("naturalearth.land"))

# default projection
world.plot(figsize=(15,10))
plt.title("Default Projection")
plt.show()

# Apply projection distortion
world_equal = world.to_crs("EPSG:6933") # eqaul area projections
world_equal.plot(figsize=(15,10))
plt.title("Equal Area Projection")
plt.show()