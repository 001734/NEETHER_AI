from pathlib import Path
import joblib
import numpy as np
import pandas as pd

from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from tensorflow.keras.utils import to_categorical

BASE_DIR = Path(__file__).resolve().parent.parent

df = pd.read_csv(BASE_DIR / "datasets" / "burnout_lstm.csv")

# Encode mood
encoder = LabelEncoder()
df["Mood"] = encoder.fit_transform(df["Mood"])

# Features
features = [
    "StudyHours",
    "SleepHours",
    "WaterIntake",
    "Energy",
    "Mood"
]

X = df[features].values
y = df["Burnout"].values

# Scale features
scaler = MinMaxScaler()
X = scaler.fit_transform(X)

SEQUENCE_LENGTH = 7

X_seq = []
y_seq = []

for i in range(len(X) - SEQUENCE_LENGTH):
    X_seq.append(X[i:i + SEQUENCE_LENGTH])
    y_seq.append(y[i + SEQUENCE_LENGTH])

X_seq = np.array(X_seq)
y_seq = np.array(y_seq)

y_seq = to_categorical(y_seq, num_classes=3)

print("Sequence Shape:", X_seq.shape)
print("Labels Shape:", y_seq.shape)

model = Sequential()

model.add(
    LSTM(
        64,
        input_shape=(SEQUENCE_LENGTH, 5)
    )
)

model.add(Dropout(0.3))

model.add(Dense(32, activation="relu"))

model.add(Dense(3, activation="softmax"))

model.compile(
    optimizer="adam",
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)

model.summary()

history = model.fit(
    X_seq,
    y_seq,
    epochs=20,
    batch_size=32,
    validation_split=0.2
)

model.save(BASE_DIR / "models" / "lstm_model.keras")

joblib.dump(
    scaler,
    BASE_DIR / "models" / "scaler.pkl"
)

joblib.dump(
    encoder,
    BASE_DIR / "models" / "label_encoder.pkl"
)

print("\nModel Saved Successfully!")