import pandas as pd
import numpy as nm
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

data = {
    'vehicle_serial_no': [5, 3, 8, 2, 4, 7, 6, 10, 1, 9],
    'mileage': [150000, 120000, 250000, 80000, 100000, 220000, 180000, 300000, 75000, 280000],
    'fuel_efficiency': [15, 18, 10, 22, 20, 12, 16, 8, 24, 9],
    'maintenance_cost': [5000, 4000, 7000, 2000, 3000, 6500, 5500, 8000, 1500, 7500],
    'vehicle_type': ['SUV', 'Sedan', 'Truck', 'Hatchback', 'Sedan', 'Truck', 'SUV', 'Truck', 'Hatchback', 'SUV']
}
df = pd.DataFrame(data)

df['vehicle_type_encoded'] = df['vehicle_type'].astype('category').cat.codes

x_all = df[['mileage', 'fuel_efficiency', 'maintenance_cost', 'vehicle_type_encoded']].values

kmeans_unscaled = KMeans(n_clusters=3, init='k-means++', random_state=42)
df['Cluster_Unscaled'] = kmeans_unscaled.fit_predict(x_all)

scaler = StandardScaler()

features_to_scale = df[['mileage', 'fuel_efficiency', 'maintenance_cost']]
scaled_features = scaler.fit_transform(features_to_scale)

x_scaled = nm.column_stack((scaled_features, df['vehicle_type_encoded'].values))

kmeans_scaled = KMeans(n_clusters=3, init='k-means++', random_state=42)
df['Cluster_Scaled'] = kmeans_scaled.fit_predict(x_scaled)

print("Fleet Segmentation Results:")
print(df[['vehicle_type', 'mileage', 'Cluster_Unscaled', 'Cluster_Scaled']])
