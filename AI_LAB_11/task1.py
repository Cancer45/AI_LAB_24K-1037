import numpy as nm
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('/kaggle/input/mall-customers/Mall_Customers.csv')

df = df.rename(columns={'Genre': 'Gender'})
df['Gender'] = df['Gender'].map({'Male': 0, 'Female': 1})

x_all = df[['Gender', 'Age', 'Annual Income (k$)', 'Spending Score (1-100)']].values

kmeans_unscaled = KMeans(n_clusters=5, init='k-means++', random_state=42)
y_unscaled = kmeans_unscaled.fit_predict(x_all)

scaler = StandardScaler()

scaled_features = scaler.fit_transform(df[['Gender', 'Annual Income (k$)', 'Spending Score (1-100)']])

x_scaled_partial = nm.column_stack((df['Age'].values, scaled_features))

kmeans_scaled = KMeans(n_clusters=5, init='k-means++', random_state=42)
y_scaled = kmeans_scaled.fit_predict(x_scaled_partial)


df['Cluster_Unscaled'] = y_unscaled
df['Cluster_Scaled'] = y_scaled

print("Comparison of first 5 rows:")
print(df.head())

print("\n--- Average Age per Cluster (Scaled Scenario) ---")
print(df.groupby('Cluster_Scaled')['Age'].mean())
