import geopandas as gpd
import matplotlib.pyplot as plt
import geodatasets

url = 'https://naciscdn.org/naturalearth/110m/cultural/ne_110m_admin_0_countries.zip'
world = gpd.read_file(url)

print(world.columns)
for i in world.columns:
    print(i)
print(world.info())

africa = world[world['CONTINENT'] == 'Africa']

africa.plot(column="POP_EST", cmap="OrRd", legend=True, edgecolor='black')

plt.title("Africa Population Map")
plt.axis("off")
plt.show()

usa = world[world['NAME'] == "United States of America"]
usa.plot(cmap='OrRd', edgecolor='black')
plt.title("USA Map")
plt.axis('off')
plt.show()

