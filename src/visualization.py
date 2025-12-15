import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
import pandas as pd
import os

def plot_clusters(data_matrix, labels, method_name="Clustering", save_path="clusters.png"):
    """
    Reduces data to 2D using PCA and plots the clusters.
    """
    pca = PCA(n_components=2)
    components = pca.fit_transform(data_matrix)
    
    df_plot = pd.DataFrame(data=components, columns=['PC1', 'PC2'])
    df_plot['Cluster'] = labels
    
    plt.figure(figsize=(10, 8))
    sns.scatterplot(x='PC1', y='PC2', hue='Cluster', data=df_plot, palette='viridis', s=100)
    plt.title(f'Student Groups - {method_name} (PCA Reduced)')
    
    # Ensure directory exists
    os.makedirs(os.path.dirname(os.path.abspath(save_path)), exist_ok=True)
    
    plt.savefig(save_path)
    plt.close()
    print(f"Cluster plot saved to {save_path}")
    return save_path

