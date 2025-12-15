import sys
import os
import pandas as pd
from src.preprocessing import preprocess_data
from src.clustering import perform_kmeans
from src.visualization import plot_clusters

# Mock Web Request Data
print("Simulating Web Request...", flush=True)

# 1. Create a mock CSV
data = {
    'Math': [90, 80, 70, 60, 50],
    'English': [88, 78, 68, 58, 48],
    'Style': ['Visual', 'Visual', 'Audio', 'Audio', 'Kinesthetic']
}
df = pd.DataFrame(data)
csv_path = "mock_upload.csv"
df.to_csv(csv_path, index=False)
print(f"Mock CSV created at {csv_path}", flush=True)

# 2. Simulate User Selection
num_features = ['Math', 'English']
cat_features = ['Style']
n_clusters = 2

# 3. Process
print("Preprocessing...", flush=True)
X, feats = preprocess_data(df, num_features, cat_features)
print(f"Features: {feats}", flush=True)

# 4. Cluster
print("Clustering...", flush=True)
labels = perform_kmeans(X, n_clusters)
df['Cluster'] = labels
print("Clustered Data:", flush=True)
print(df)

# 5. Visualise
print("Visualizing...", flush=True)
plot_clusters(X, labels, save_path="mock_plot.png")

print("Web App Logic Verification Passed!", flush=True)
