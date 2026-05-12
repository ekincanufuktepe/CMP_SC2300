from sklearn.datasets import load_wine
import pandas as pd

# Load Wine Dataset
wine = load_wine(as_frame=True)
df = wine.frame

print(df.head())
print(df.shape)
print(df.info())

# Separate Features and "target"

x = df.drop(columns=['target'])
y = df['target']

# DataFrame without target
print("DataFrame x: without 'target' ")
print(x.head())

# DataFrame for only 'target'
print("DataFrame y: the 'target' ")
print(y.head())

# Standardization Before PCA
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
'''
    centers each feature and scales it to
    unit variance.
'''
X_scaled = scaler.fit_transform(x)

print("Centered/Scaled X features")
print(X_scaled)  

# Run PCA with 2 components
from sklearn.decomposition import PCA

pca = PCA(n_components=2)
x_pca = pca.fit_transform(X_scaled)

print("First 5 elements of PCA output")
print(x_pca[:5])

# Visualize PCA Projection
import matplotlib.pyplot as plt

plt.figure(figsize=(7,5))
scatter = plt.scatter(x_pca[:, 0], x_pca[:, 1], c=y)
plt.xlabel=("Principal Component 1")
plt.ylabel=("Principal Component 2")
plt.title("Wine Dataset Projection into 2D PCA Space")
plt.show()

# Explain Variance Ratio

# dataset variance captured by each PC (component)
print(pca.explained_variance_ratio_)
# total variance preserved in 2D projection
# how much info we kept
print("% of Dataset Preserved: " + str(pca.explained_variance_ratio_.sum()))

# Fit PCA without Limiting Components
pca_full = PCA()
pca_full.fit(X_scaled)
explained = pca_full.explained_variance_ratio_
print("PCA Without Limiting Component")
print(explained)

# Scree Plot
plt.figure(figsize=(7,5))
plt.plot(range(1, len(explained) + 1), explained, marker="o")
plt.xlabel=("Principal Component")
plt.ylabel=("Explained Variance Ratio")
plt.title("Scree Plot")
plt.show()

# Cumulative Explained Variance
import numpy as np

cumulative = np.cumulative_sum(explained)
plt.figure(figsize=(7,5))
plt.plot(range(1, len(cumulative)+1), cumulative, marker='o')
plt.xlabel=("Number of Components")
plt.ylabel=("Cumulative Explained Variance")
plt.title("Cumulative Explained Variance")
plt.axhline(0.8, linestyle="--")
plt.show()

# PCA Loadings
loadings = pd.DataFrame(
            pca.components_.T,
            columns = ['PC1', 'PC2'],
            index = x.columns)
            
print(loadings)

# Interpret Loadings
print(loadings["PC1"].sort_values(ascending=False))
print(loadings["PC2"].sort_values(ascending=False))

# Visualize Loadings
loadings["PC1"].sort_values().plot(kind='barh', figsize=(7,5))
plt.title("Feature Loadings on PC1")
plt.xlabel=("Loading")
plt.show()

loadings["PC2"].sort_values().plot(kind='barh', figsize=(7,5))
plt.title("Feature Loadings on PC2")
plt.xlabel=("Loading")
plt.show()


















