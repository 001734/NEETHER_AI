from pathlib import Path
import pandas as pd
import joblib

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# Project root
BASE_DIR = Path(__file__).resolve().parent.parent

# Dataset location
dataset_path = BASE_DIR / "datasets" / "burnout_dataset.csv"

print(f"Loading dataset from:\n{dataset_path}")

# Read dataset
df = pd.read_csv(dataset_path)

# Encode Mood column
encoder = LabelEncoder()
df["Mood"] = encoder.fit_transform(df["Mood"])

# Features and target
X = df[["StudyHours", "SleepHours", "WaterIntake", "Energy", "Mood"]]
y = df["Burnout"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
)

# Train model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
)

model.fit(X_train, y_train)

# Accuracy
accuracy = model.score(X_test, y_test)
print(f"\nAccuracy: {accuracy * 100:.2f}%")

# Save model
joblib.dump(model, BASE_DIR / "models" / "burnout_model.pkl")
joblib.dump(encoder, BASE_DIR / "models" / "mood_encoder.pkl")

print("\n✅ Model saved successfully!")