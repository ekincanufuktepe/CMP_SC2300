from sklearn.datasets import load_wine
import pandas as pd

data = load_wine()

#df = data.frame
df = pd.DataFrame(data.data, columns=data.feature_names)

from sklearn.cluster import KMeans

X = df.copy()

kmeans = KMeans(n_clusters=3)
labels = kmeans.fit_predict(X)


from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

X_scaled = StandardScaler().fit_transform(X)
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

plt.scatter(X_pca[:,0], X_pca[:,1], c=labels)
plt.title("Clusters Visualized in PCA Space")
plt.show()


import networkx as nx
import matplotlib.pyplot as plt

# Example: student collaboration network
G = nx.Graph()

edges = [
    ("Alice", "Bob"),
    ("Alice", "Carlos"),
    ("Bob", "Dina"),
    ("Carlos", "Dina"),
    ("Dina", "Eli"),
    ("Eli", "Fatima"),
    ("Carlos", "Fatima")
]

G.add_edges_from(edges)

plt.figure(figsize=(7, 5))
pos = nx.spring_layout(G, seed=42)

nx.draw(
    G,
    pos,
    with_labels=True,
    node_size=1200,
    font_size=10
)

plt.title("Student Collaboration Network")
plt.show()


# Parallel

import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import parallel_coordinates

# Example: student performance profiles
df = pd.DataFrame({
    "math": [90, 75, 60, 85, 70],
    "coding": [95, 80, 55, 88, 72],
    "writing": [70, 85, 90, 65, 75],
    "presentation": [75, 88, 92, 70, 80],
    "group": ["Technical", "Balanced", "Writing", "Technical", "Balanced"]
})

plt.figure(figsize=(9, 5))
parallel_coordinates(df, "group")

plt.title("Student Skill Profiles")
plt.ylabel("Score")
plt.show()


# Sankey

import plotly.graph_objects as go

# Example: website user journey
labels = ["Homepage", "Product Page", "Cart", "Checkout", "Exit"]

source = [0, 0, 1, 1, 2, 2, 3]
target = [1, 4, 2, 4, 3, 4, 4]
value  = [100, 40, 60, 40, 35, 25, 20]

fig = go.Figure(data=[go.Sankey(
    node=dict(label=labels),
    link=dict(source=source, target=target, value=value)
)])

fig.update_layout(title_text="Website User Flow", font_size=12)
fig.show()


# Treemap

import plotly.express as px
import pandas as pd

# Example: company revenue by department and product
df = pd.DataFrame({
    "department": ["Tech", "Tech", "Tech", "Home", "Home", "Sports", "Sports"],
    "product": ["Laptop", "Phone", "Tablet", "Furniture", "Kitchen", "Shoes", "Equipment"],
    "revenue": [400, 300, 150, 250, 180, 220, 120]
})

fig = px.treemap(
    df,
    path=["department", "product"],
    values="revenue",
    title="Company Revenue by Department and Product"
)

fig.show()


# Radar Chart

import matplotlib.pyplot as plt
import numpy as np

# Example: athlete skill profile
categories = ["Speed", "Strength", "Endurance", "Agility", "Technique"]
athlete_a = [8, 7, 9, 8, 6]
athlete_b = [6, 9, 6, 7, 9]

angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False)

# close the loop
athlete_a += athlete_a[:1]
athlete_b += athlete_b[:1]
angles = np.concatenate([angles, [angles[0]]])

plt.figure(figsize=(6, 6))
ax = plt.subplot(111, polar=True)

ax.plot(angles, athlete_a, label="Athlete A")
ax.fill(angles, athlete_a, alpha=0.2)

ax.plot(angles, athlete_b, label="Athlete B")
ax.fill(angles, athlete_b, alpha=0.2)

ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories)
ax.set_title("Athlete Skill Comparison")
ax.legend(loc="upper right")

plt.show()

# Hexbin 

import numpy as np
import matplotlib.pyplot as plt

# Example: dense location-like data
np.random.seed(42)

x = np.random.normal(0, 1, 5000)
y = 0.6 * x + np.random.normal(0, 0.8, 5000)

plt.figure(figsize=(7, 5))
plt.hexbin(x, y, gridsize=35)
plt.colorbar(label="Count")

plt.title("Hexbin Plot: Density of Points")
plt.xlabel("x")
plt.ylabel("y")

plt.show()

# Stremgraph

import numpy as np
import matplotlib.pyplot as plt

# Example: popularity of music genres over time
years = np.arange(2015, 2025)

pop = np.array([30, 32, 35, 38, 42, 45, 47, 49, 50, 52])
rock = np.array([40, 38, 36, 34, 31, 29, 27, 25, 23, 21])
hiphop = np.array([20, 22, 25, 28, 32, 36, 40, 44, 48, 52])
country = np.array([15, 16, 16, 17, 17, 18, 18, 19, 19, 20])

plt.figure(figsize=(9, 5))
plt.stackplot(
    years,
    pop,
    rock,
    hiphop,
    country,
    labels=["Pop", "Rock", "Hip-Hop", "Country"],
    baseline="wiggle"
)

plt.legend(loc="upper left")
plt.title("Music Genre Popularity Over Time")
plt.xlabel("Year")
plt.ylabel("Relative Popularity")

plt.show()

# t-sne visualization

import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.manifold import TSNE
from sklearn.preprocessing import StandardScaler

# Example: handwritten digits dataset
digits = load_digits()

X = digits.data
y = digits.target

# Scale data before t-SNE
X_scaled = StandardScaler().fit_transform(X)

tsne = TSNE(
    n_components=2,
    random_state=42,
    perplexity=30,
    learning_rate="auto",
    init="pca"
)

X_tsne = tsne.fit_transform(X_scaled)

plt.figure(figsize=(8, 6))
scatter = plt.scatter(
    X_tsne[:, 0],
    X_tsne[:, 1],
    c=y,
    cmap="tab10",
    s=20
)

plt.colorbar(scatter, label="Digit")
plt.title("t-SNE Visualization of Handwritten Digits")
plt.xlabel("t-SNE 1")
plt.ylabel("t-SNE 2")

plt.show()

# hierarichal clustering

import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from scipy.cluster.hierarchy import linkage, dendrogram
from sklearn.preprocessing import StandardScaler

# Example: iris flower measurements
iris = load_iris()

X = iris.data
X_scaled = StandardScaler().fit_transform(X)

# Ward linkage builds the hierarchy
Z = linkage(X_scaled, method="ward")

plt.figure(figsize=(10, 5))
dendrogram(Z, truncate_mode="lastp", p=20)

plt.title("Hierarchical Clustering Dendrogram")
plt.xlabel("Cluster")
plt.ylabel("Distance")

plt.show()