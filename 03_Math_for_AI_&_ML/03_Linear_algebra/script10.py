import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs  # pyright: ignore[reportMissingModuleSource]
from sklearn.decomposition import PCA  # pyright: ignore[reportMissingModuleSource]

# Generate sample dataset with 3 features
X, y = make_blobs(n_samples=200, centers=3, n_features=3, random_state=42)

# Apply PCA
pca = PCA(n_components=2)

X_reduced = pca.fit_transform(X)

print("Original shape:", X.shape)
print("Reduced shape:", X_reduced.shape)

print("Explained variance:")
print(pca.explained_variance_ratio_)

# Visualize reduced data
plt.scatter(X_reduced[:, 0], X_reduced[:, 1], c=y)

plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.title("PCA - Dimensionality Reduction")

plt.show()
