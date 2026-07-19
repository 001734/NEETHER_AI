from pathlib import Path
import numpy as np
import joblib
from tensorflow.keras.models import load_model

BASE_DIR = Path(__file__).resolve().parent.parent

# Load model
model = load_model(BASE_DIR / "models" / "lstm_model.keras")

# Load scaler
scaler = joblib.load(BASE_DIR / "models" / "scaler.pkl")

# Load encoder
encoder = joblib.load(BASE_DIR / "models" / "label_encoder.pkl")


def predict_burnout(last_7_days):

    data = np.array(last_7_days)

    moods = encoder.transform(data[:,4])

    data = np.column_stack([
        data[:,0].astype(float),
        data[:,1].astype(float),
        data[:,2].astype(float),
        data[:,3].astype(float),
        moods
    ])

    data = scaler.transform(data)

    data = data.reshape(1,7,5)

    prediction = model.predict(data)

    index = np.argmax(prediction)

    labels = [
        "Low",
        "Medium",
        "High"
    ]

    return labels[index], prediction