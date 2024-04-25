import numpy as np

class KMeans:
def __init__(self, n_clusters=8, max_iter=300):
self.n_clusters = n_clusters
self.max_iter = max_iter

def fit(self, X):
self.centroids = X[np.random.choice(X.shape[0], self.n_clusters, replace=False)]

for _ in range(self.max_iter):
# Assign each data point to the nearest centroid
labels = self._assign_clusters(X)

# Update centroids based on the mean of the data points assigned to each cluster
new_centroids = np.array([X[labels == i].mean(axis=0) for i in range(self.n_clusters)])

# Check for convergence
if np.allclose(self.centroids, new_centroids):
break

self.centroids = new_centroids

self.labels_ = self._assign_clusters(X)

def _assign_clusters(self, X):
distances = np.sqrt(((X - self.centroids[:, np.newaxis])**2).sum(axis=2))
return np.argmin(distances, axis=0)
