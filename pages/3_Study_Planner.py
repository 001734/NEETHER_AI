import streamlit as st
import pandas as pd
from datetime import date
import os

st.set_page_config(page_title="AI Study Planner", layout="wide")

st.title("📚 AI Study Planner")

st.write("Generate a personalized study plan based on your wellness and study performance.")

st.divider()

col1, col2 = st.columns(2)

with col1:

    study_hours = st.slider(
        "Study Hours Today",
        0.0,
        12.0,
        6.0,
        0.5
    )

    sleep_hours = st.slider(
        "Sleep Hours",
        3.0,
        12.0,
        7.5,
        0.5
    )

    mood = st.selectbox(
        "Mood",
        ["Happy","Normal","Tired","Stressed","Anxious"]
    )

with col2:

    energy = st.slider(
        "Energy Level",
        1,
        10,
        7
    )

    subject = st.selectbox(
        "Today's Main Subject",
        ["Biology","Chemistry","Physics"]
    )

    mock = st.slider(
        "Latest Mock Test Score (%)",
        0,
        100,
        70
    )

st.divider()

recommendation = ""

if energy >= 8 and sleep_hours >= 7:

    recommendation = f"""
✅ Focus on **{subject}**

• 3-hour deep study session

• 1-hour revision

• Solve 100 MCQs

• Attempt one mock test
"""

elif mood == "Stressed":

    recommendation = """
💖 Take a lighter study day.

• Study for 2 hours

• Revise notes

• Drink enough water

• Sleep early
"""

elif sleep_hours < 6:

    recommendation = """
😴 Sleep is insufficient.

Avoid long study sessions.

Take frequent breaks.

Sleep at least 7–8 hours tonight.
"""

else:

    recommendation = f"""
📘 Study {subject}

• 2-hour focused session

• 50 MCQs

• 30-minute revision

• Review mistakes
"""

st.subheader("🤖 AI Recommendation")

st.success(recommendation)

st.divider()

c1,c2,c3 = st.columns(3)

with c1:
    st.metric("Study Hours",study_hours)

with c2:
    st.metric("Mock Score",str(mock)+"%")

with c3:
    st.metric("Energy",energy)

st.divider()

if st.button("Save Today's Study Plan"):

    row = pd.DataFrame({

        "Date":[date.today()],

        "StudyHours":[study_hours],

        "SleepHours":[sleep_hours],

        "Subject":[subject],

        "MockScore":[mock],

        "Mood":[mood],

        "Energy":[energy],

        "Recommendation":[recommendation]

    })

    file = "data/study_data.csv"

    if os.path.exists(file):

        old = pd.read_csv(file)

        new = pd.concat([old,row],ignore_index=True)

        new.to_csv(file,index=False)

    else:

        row.to_csv(file,index=False)

    st.success("Study plan saved successfully!")

st.divider()

try:

    df = pd.read_csv("data/study_data.csv")

    st.subheader("📈 Study History")

    st.dataframe(df,use_container_width=True)

except:

    pass