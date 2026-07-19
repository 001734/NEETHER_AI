# from pathlib import Path
# from datetime import datetime
# import pandas as pd

# # Project root
# BASE_DIR = Path(__file__).resolve().parent.parent

# # Data folder
# DATA_DIR = BASE_DIR / "data"
# DATA_DIR.mkdir(exist_ok=True)

# # CSV file path
# CSV_FILE = DATA_DIR / "wellness_history.csv"


# def initialize_file():
#     """Create CSV file if it doesn't exist."""
#     if not CSV_FILE.exists():
#         df = pd.DataFrame(columns=[
#             "Date",
#             "StudyHours",
#             "SleepHours",
#             "WaterIntake",
#             "Energy",
#             "Mood"
#         ])
#         df.to_csv(CSV_FILE, index=False)


# def save_today(study, sleep, water, energy, mood):
#     """Save today's wellness data."""

#     initialize_file()

#     df = pd.read_csv(CSV_FILE)

#     today = datetime.now().strftime("%Y-%m-%d")

#     new_row = {
#         "Date": today,
#         "StudyHours": study,
#         "SleepHours": sleep,
#         "WaterIntake": water,
#         "Energy": energy,
#         "Mood": mood
#     }

#     df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

#     df.to_csv(CSV_FILE, index=False)


# def get_all_data():
#     """Return complete wellness history."""

#     initialize_file()

#     return pd.read_csv(CSV_FILE)


# def get_last_7_days():
#     """Return last 7 days of data."""

#     initialize_file()

#     df = pd.read_csv(CSV_FILE)

#     if len(df) < 7:
#         return None

#     return df.tail(7)


# def clear_history():
#     """Delete all saved data."""

#     initialize_file()

#     df = pd.DataFrame(columns=[
#         "Date",
#         "StudyHours",
#         "SleepHours",
#         "WaterIntake",
#         "Energy",
#         "Mood"
#     ])

#     df.to_csv(CSV_FILE, index=False)



from pathlib import Path
from datetime import datetime
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)

CSV_FILE = DATA_DIR / "wellness_history.csv"


def initialize_file():
    if not CSV_FILE.exists():
        df = pd.DataFrame(columns=[
            "Date",
            "StudyHours",
            "SleepHours",
            "WaterIntake",
            "Energy",
            "Mood"
        ])
        df.to_csv(CSV_FILE, index=False)


def save_today(study, sleep, water, energy, mood):
    initialize_file()

    df = pd.read_csv(CSV_FILE)

    new_row = {
        "Date": datetime.now().strftime("%Y-%m-%d"),
        "StudyHours": study,
        "SleepHours": sleep,
        "WaterIntake": water,
        "Energy": energy,
        "Mood": mood
    }

    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    df.to_csv(CSV_FILE, index=False)


def get_all_data():
    initialize_file()
    return pd.read_csv(CSV_FILE)


def last_7_days():
    initialize_file()

    df = pd.read_csv(CSV_FILE)

    if len(df) < 7:
        return None

    return df.tail(7)


def clear_history():
    initialize_file()

    df = pd.DataFrame(columns=[
        "Date",
        "StudyHours",
        "SleepHours",
        "WaterIntake",
        "Energy",
        "Mood"
    ])

    df.to_csv(CSV_FILE, index=False)