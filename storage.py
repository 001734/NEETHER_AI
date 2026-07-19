from pathlib import Path
import pandas as pd
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)

FILE_PATH = DATA_DIR / "wellness_history.csv"


def create_file():
    if not FILE_PATH.exists():

        df = pd.DataFrame(columns=[
            "Date",
            "StudyHours",
            "SleepHours",
            "WaterIntake",
            "Energy",
            "Mood"
        ])

        df.to_csv(FILE_PATH, index=False)


def save_today(study, sleep, water, energy, mood):

    create_file()

    df = pd.read_csv(FILE_PATH)

    today = datetime.now().strftime("%Y-%m-%d")

    new_row = pd.DataFrame([{
        "Date": today,
        "StudyHours": study,
        "SleepHours": sleep,
        "WaterIntake": water,
        "Energy": energy,
        "Mood": mood
    }])

    df = pd.concat([df, new_row], ignore_index=True)

    df.to_csv(FILE_PATH, index=False)


def get_history():

    create_file()

    return pd.read_csv(FILE_PATH)


def last_7_days():

    create_file()

    df = pd.read_csv(FILE_PATH)

    if len(df) < 7:
        return None

    return df.tail(7)