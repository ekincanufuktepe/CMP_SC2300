import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import load_digits
from sklearn.preprocessing import StandardScaler
from sklearn.manifold import TSNE
from sklearn.neighbors import NearestNeighbors

# Load digits dataset
digits = load_digits()
X = digits.data
y = digits.target
images = digits.images

# Scale data
X_scaled = StandardScaler().fit_transform(X)

# Run t-SNE
tsne = TSNE(
    n_components=2,
    random_state=42,
    perplexity=30,
    learning_rate="auto",
    init="pca"
)

X_tsne = tsne.fit_transform(X_scaled)

# Find nearest neighbors in t-SNE space
nn = NearestNeighbors(n_neighbors=10)
nn.fit(X_tsne)

distances, indices = nn.kneighbors(X_tsne)

# Find a close pair with different true labels
pair = None

for i in range(len(X_tsne)):
    for neighbor_index, dist in zip(indices[i][1:], distances[i][1:]):
        if y[i] != y[neighbor_index]:
            pair = (i, neighbor_index, dist)
            break
    if pair is not None:
        break

i, j, dist = pair

print("Point 1 index:", i, "label:", y[i])
print("Point 2 index:", j, "label:", y[j])
print("Distance in t-SNE space:", dist)

plt.figure(figsize=(8, 6))

scatter = plt.scatter(
    X_tsne[:, 0],
    X_tsne[:, 1],
    c=y,
    cmap="tab10",
    s=20,
    alpha=0.7
)

plt.scatter(
    X_tsne[[i, j], 0],
    X_tsne[[i, j], 1],
    s=180,
    facecolors="none",
    edgecolors="black",
    linewidths=2
)

plt.colorbar(scatter, label="True Digit")
plt.title("t-SNE of Digits Dataset: Close Points with Different Labels")
plt.xlabel("t-SNE 1")
plt.ylabel("t-SNE 2")

plt.show()

x_min = min(X_tsne[i, 0], X_tsne[j, 0]) - 5
x_max = max(X_tsne[i, 0], X_tsne[j, 0]) + 5
y_min = min(X_tsne[i, 1], X_tsne[j, 1]) - 5
y_max = max(X_tsne[i, 1], X_tsne[j, 1]) + 5

plt.figure(figsize=(7, 6))

scatter = plt.scatter(
    X_tsne[:, 0],
    X_tsne[:, 1],
    c=y,
    cmap="tab10",
    s=30,
    alpha=0.7
)

plt.scatter(
    X_tsne[[i, j], 0],
    X_tsne[[i, j], 1],
    s=220,
    facecolors="none",
    edgecolors="black",
    linewidths=2
)

plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)

plt.colorbar(scatter, label="True Digit")
plt.title("Zoomed View: Two Nearby Points with Different Labels")
plt.xlabel("t-SNE 1")
plt.ylabel("t-SNE 2")

plt.show()

fig, axes = plt.subplots(1, 2, figsize=(6, 3))

axes[0].imshow(images[i], cmap="gray")
axes[0].set_title(f"Point {i}\nTrue label: {y[i]}")
axes[0].axis("off")

axes[1].imshow(images[j], cmap="gray")
axes[1].set_title(f"Point {j}\nTrue label: {y[j]}")
axes[1].axis("off")

plt.suptitle("What Do These Nearby Points Actually Look Like?")
plt.tight_layout()
plt.show()