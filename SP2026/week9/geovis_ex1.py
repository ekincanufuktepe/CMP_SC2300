import geopandas as gpd
import matplotlib.pyplot as plt
import geodatasets

world = gpd.read_file(geodatasets.get_path('naturalearth.land'))

print(world.head())

world.plot(figsize=(10,5))
plt.show()

cities = gpd.GeoDataFrame({
            'city' : ['NYC', 'London', 'Tokyo', 'Houston'],
            'geometry' : gpd.points_from_xy([-74, -0.7, 139.4, -95.2], [40.4, 50.3, 35.4, 29.4])
            })
            
ax = world.plot(color='lightgray', figsize=(10,5))
ax2 = cities.plot(ax=ax, color='red')

new_city = gpd.GeoDataFrame({
            'city' : ['Chicago'],
            'geometry' : gpd.points_from_xy([-87.3], [41.5])
            })

new_city.plot(ax=ax2, color='blue')
plt.title('Cities on World Map')
plt.show()  
  