import pandas as pd
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

data = {
    'spending': [100, 500, 150, 800, 200, 950, 110],
    'age': [22, 35, 45, 30, 25, 40, 50],
    'visits': [1, 5, 2, 8, 3, 10, 1],
    'high_value': [0, 1, 0, 1, 0, 1, 0]
}
df = pd.DataFrame(data)

X = df.drop('high_value', axis=1)
y = df['high_value']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = SVC(kernel='linear')
model.fit(X_train_scaled, y_train)

predictions = model.predict(X_test_scaled)
print("Predictions: ", predictions)

print('==================== SVM Training Accuracy ====================')
train_acc = model.score(X_train_scaled, y_train) * 100
print(f"Training Accuracy: {train_acc:.2f}%")

print('==================== SVM Testing Accuracy =====================')
test_acc = accuracy_score(y_test, predictions) * 100
print(f"Testing Accuracy: {test_acc:.2f}%")
