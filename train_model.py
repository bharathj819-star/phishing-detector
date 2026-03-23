import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Load dataset
data = pd.read_csv("dataset/phishing.csv")

print("Columns:", data.columns)

# Drop unnecessary column
data = data.drop("index", axis=1)

# Features and label
X = data.drop("Result", axis=1)
y = data["Result"]

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train
model = RandomForestClassifier()
model.fit(X_train, y_train)

print("Accuracy:", model.score(X_test, y_test))

# Save model
pickle.dump(model, open("model/phishing_model.pkl", "wb"))

print("Model saved successfully!")