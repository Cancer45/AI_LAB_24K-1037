import numpy as nm
import matplotlib.pyplot as mtp
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

data = {
    'student_id': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112],
    'GPA': [3.8, 2.1, 3.5, 2.8, 3.9, 1.5, 3.2, 2.5, 3.7, 1.9, 3.0, 2.4],
    'study_hours': [40, 10, 35, 20, 45, 5, 30, 15, 38, 12, 25, 18],
    'attendance_rate': [95, 60, 90, 75, 98, 40, 85, 70, 92, 55, 80, 65]
}
df = pd.DataFrame(data)

x = df[['GPA', 'study_hours', 'attendance_rate']].values

scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)

wcss_list = []
for i in range(2, 7):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
    kmeans.fit(x_scaled)
    wcss_list.append(kmeans.inertia_)

mtp.figure(figsize=(8, 4))
mtp.plot(range(2, 7), wcss_list, marker='o', color='maroon')
mtp.title('Elbow Method for Optimal K')
mtp.xlabel('Number of Clusters (K)')
mtp.ylabel('WCSS')
mtp.show()

optimal_k = 3 
kmeans = KMeans(n_clusters=optimal_k, init='k-means++', random_state=42)
df['Cluster'] = kmeans.fit_predict(x_scaled)

print("--- Final Student Segments ---")
print(df[['student_id', 'GPA', 'study_hours', 'attendance_rate', 'Cluster']])

mtp.figure(figsize=(10, 6))
colors = ['blue', 'green', 'red', 'purple', 'orange']

for i in range(optimal_k):
    mtp.scatter(df[df['Cluster'] == i]['study_hours'], 
                df[df['Cluster'] == i]['GPA'], 
                s=100, c=colors[i], label=f'Cluster {i}')

mtp.title('Student Segmentation: Study Hours vs GPA')
mtp.xlabel('Weekly Study Hours')
mtp.ylabel('GPA')
mtp.legend()
mtp.grid(True, linestyle='--', alpha=0.6)
mtp.show()
