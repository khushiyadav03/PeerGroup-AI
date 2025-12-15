import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import pandas as pd
import numpy as np

print("Start Debug", flush=True)

try:
    print("Importing Faker...", flush=True)
    from faker import Faker
    print("Faker imported.", flush=True)
except Exception as e:
    print(f"Error importing Faker: {e}", flush=True)

try:
    print("Importing sklearn...", flush=True)
    from sklearn.cluster import KMeans
    print("sklearn imported.", flush=True)
except Exception as e:
    print(f"Error importing sklearn: {e}", flush=True)

print("Running data gen...", flush=True)
try:
    from data.data_generator import generate_student_data
    df = generate_student_data(10)
    print(f"Data gen done: {len(df)}", flush=True)
except Exception as e:
    print(f"Error data gen: {e}", flush=True)

print("Running KMeans...", flush=True)
try:
    km = KMeans(n_clusters=2)
    data = np.random.rand(10, 2)
    km.fit(data)
    print("KMeans fit done.", flush=True)
except Exception as e:
    print(f"Error KMeans: {e}", flush=True)
    
print("End Debug", flush=True)
