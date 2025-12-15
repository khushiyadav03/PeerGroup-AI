import os
import sys

# Add project root to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from data.data_generator import generate_student_data
from src.preprocessing import preprocess_data
from src.clustering import perform_kmeans, perform_hierarchical
from src.visualization import plot_clusters

def main():
    print("Peer Group Identification System")
    print("--------------------------------")

    # 1. Generate Data
    print("\n[1] Generating synthetic student data...")
    df = generate_student_data(n_students=50)
    print(f"Generated {len(df)} students.")
    
    # 2. Preprocess Data
    print("\n[2] Preprocessing data...")
    num_cols = ['Math_Grade', 'Science_Grade', 'History_Grade', 'Personality_Score']
    cat_cols = ['Learning_Style', 'Interest']
    X, feature_names = preprocess_data(df, num_cols, cat_cols)
    print(f"Data processed. Features: {len(feature_names)}")

    # 3. Clustering (K-Means)
    n_groups = 10 # 50 students / 5 per group
    print(f"\n[3] Performing K-Means Clustering (Target: {n_groups} groups)...")
    labels = perform_kmeans(X, n_clusters=n_groups)
    
    df['Cluster_Label'] = labels
    
    # 4. Visualization
    print("\n[4] Visualizing clusters...")
    plot_clusters(X, labels, method_name="KMeans", save_path="clusters_kmeans.png")
    
    # 5. Output Results
    output_file = "student_groups.csv"
    df.sort_values(by='Cluster_Label', inplace=True)
    df.to_csv(output_file, index=False)
    print(f"\n[5] Results saved to {output_file}")
    
    print("\nSample Group (Group 0):")
    print(df[df['Cluster_Label'] == 0][['Name', 'Math_Grade', 'Learning_Style', 'Interest']])

if __name__ == "__main__":
    main()

