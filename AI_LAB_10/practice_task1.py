import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

data = {
    "area": [300, 250, 1100, 490, 780, 610, 830],
    "age": [30, 10, 21, 5, 11, 3, 9],
    "location": ['NY', 'WA', 'WA', 'CA', 'SC', 'WA', 'CA'],
    "price": [500, 450, 1200, 700, 850, 800, 950]
}

df = pd.DataFrame(data)

df = pd.get_dummies(df, columns=['location'], drop_first=True)

X = df.drop('price', axis=1)
y = df['price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

LR = LinearRegression()
ModelLR = LR.fit(X_train, y_train)

predictions = ModelLR.predict(X_test)

print("Predictions:", predictions)
print("Actual values:", y_test.values)
