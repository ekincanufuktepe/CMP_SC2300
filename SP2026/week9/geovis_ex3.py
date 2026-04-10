import matplotlib.pyplot as plt
import geopandas as gpd
import geodatasets

url = 'https://naciscdn.org/naturalearth/110m/cultural/ne_110m_admin_0_countries.zip'
world = gpd.read_file(url)

continents = world['CONTINENT'].unique()

fig, axes = plt.subplots(3, 3, figsize=(15,10))

axes = axes.flatten()

for i, continent in enumerate(continents):
    ax = axes[i]
    subset = world[world['CONTINENT'] == continent]
    subset.plot(
        column='POP_EST',
        cmap='OrRd',
        legend=False,
        edgecolor='black',
        ax=ax
    )
    ax.set_title(continent)
    ax.axis('off')
    
for j in range(len(continents), len(axes)):
    fig.delaxes(axes[j])

plt.tight_layout()
plt.show()