import pandas as pd
import random
from datetime import datetime, timedelta

rows = []

start_date = datetime(2025, 1, 1)

moods = ["Happy", "Normal", "Tired", "Stressed", "Anxious"]

for i in range(1000):

    date = start_date + timedelta(days=i)

    study = round(random.uniform(2, 10), 1)
    sleep = round(random.uniform(4, 9), 1)
    water = round(random.uniform(1, 4), 1)
    energy = random.randint(2, 10)
    mood = random.choice(moods)

    if sleep < 5 or study > 8 or energy < 4:
        burnout = 2
    elif sleep < 6.5 or study > 6:
        burnout = 1
    else:
        burnout = 0

    rows.append([
        date.strftime("%Y-%m-%d"),
        study,
        sleep,
        water,
        energy,
        mood,
        burnout
    ])

df = pd.DataFrame(
    rows,
    columns=[
        "Date",
        "StudyHours",
        "SleepHours",
        "WaterIntake",
        "Energy",
        "Mood",
        "Burnout"
    ]
)

df.to_csv("datasets/burnout_lstm.csv", index=False)

print("Dataset created successfully!")
print(df.head())