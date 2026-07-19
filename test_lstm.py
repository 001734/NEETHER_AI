from models.predict_lstm import predict_burnout

sample = [
    [6, 8, 2.5, 8, "Happy"],
    [6, 8, 2.6, 8, "Happy"],
    [7, 7.5, 2.3, 7, "Normal"],
    [8, 7, 2.4, 7, "Normal"],
    [9, 6, 2.0, 6, "Tired"],
    [9, 5.5, 1.8, 5, "Stressed"],
    [10, 5, 1.5, 4, "Anxious"]
]

result, probability = predict_burnout(sample)

print("Prediction:", result)
print("Probability:", probability)