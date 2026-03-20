
from sklearn.cluster import KMeans

best_k = 2

kmeans = KMeans(n_clusters=best_k, random_state=42, n_init=10)
kmeans.fit(X_clust)
cluster_labels = kmeans.labels_
