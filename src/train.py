from preprocess import preprocess
from sklearn.linear_model import LogisticRegression
import pandas as pd

df = preprocess("data/sample.csv")
# Assume last column is target
X = df.iloc[:, :-1]
y = df.iloc[:, -1]

model = LogisticRegression()
model.fit(X, y)

print("Training completed!")

