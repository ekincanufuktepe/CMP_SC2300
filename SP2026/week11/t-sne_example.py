from sklearn.datasets import load_digits
import matplotlib.pyplot as plt

digits = load_digits()
print(digits)
X = digits.data
print(X.shape)

# Apply t-SNE
from sklearn.manifold import TSNE
tsne = TSNE(n_components=2, random_state=42)
X_tsne = tsne.fit_transform(X)

plt.scatter(X_tsne[:,0], X_tsne[:,1], c=digits.target)
plt.title("t-SNE Visualization of Digits Dataset")
plt.show()

# Interpretation pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

X = digits.data
X_scaled = StandardScaler().fit_transform(X)
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)
tsne = TSNE(n_components=2)
X_tsne = tsne.fit_transform(X_scaled)
#kmeans = KMeans(n_components=3)
#labels = kmeans.fit_predict(X_scaled)

# Visualize comparison
plt.figure(figsize=(12,6))
plt.subplot(1,2,1)
plt.scatter(X_pca[:,0], X_pca[:,1], c=digits.target)
plt.title("PCA")
plt.subplot(1,2,2)
plt.scatter(X_tsne[:,0], X_tsne[:,1], c=digits.target)
plt.title("t-SNE")
plt.show()
















