from sklearn.cluster import KMeans, AgglomerativeClustering

def perform_kmeans(data, n_clusters, seed=42):
    """
    Performs K-Means clustering.
    Returns the cluster labels.
    """
    kmeans = KMeans(n_clusters=n_clusters, random_state=seed, n_init=10)
    labels = kmeans.fit_predict(data)
    return labels

def perform_hierarchical(data, n_clusters):
    """
    Performs Agglomerative Hierarchical clustering.
    Returns the cluster labels.
    """
    hc = AgglomerativeClustering(n_clusters=n_clusters)
    labels = hc.fit_predict(data)
    return labels

