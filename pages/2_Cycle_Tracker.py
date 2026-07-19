import streamlit as st
import pandas as pd
from datetime import date, timedelta
import os

st.set_page_config(page_title="Cycle Tracker", layout="wide")

st.title("🌸 Menstrual Cycle Tracker")

st.write("Track your menstrual cycle and receive AI-based predictions.")

st.divider()

col1, col2 = st.columns(2)

with col1:
    last_period = st.date_input(
        "Last Period Start Date",
        value=date.today()
    )

with col2:
    cycle_length = st.slider(
        "Average Cycle Length",
        21,
        35,
        28
    )

today = date.today()

current_day = (today - last_period).days + 1

next_period = last_period + timedelta(days=cycle_length)

ovulation = next_period - timedelta(days=14)

fertile_start = ovulation - timedelta(days=5)

fertile_end = ovulation + timedelta(days=1)

st.divider()

c1, c2, c3 = st.columns(3)

with c1:
    st.metric("Current Cycle Day", current_day)

with c2:
    st.metric("Next Period", next_period.strftime("%d %b %Y"))

with c3:
    st.metric("Ovulation", ovulation.strftime("%d %b %Y"))

st.divider()

st.subheader("🌼 Fertile Window")

st.info(
    f"{fertile_start.strftime('%d %b')}  ➜  {fertile_end.strftime('%d %b')}"
)

st.divider()

if st.button("Save Cycle Data"):

    data = pd.DataFrame({

        "LastPeriod":[last_period],

        "CycleLength":[cycle_length],

        "CurrentDay":[current_day],

        "NextPeriod":[next_period],

        "OvulationDay":[ovulation],

        "FertileStart":[fertile_start],

        "FertileEnd":[fertile_end]

    })

    file = "data/cycle_data.csv"

    if os.path.exists(file):

        old = pd.read_csv(file)

        new = pd.concat([old,data],ignore_index=True)

        new.to_csv(file,index=False)

    else:

        data.to_csv(file,index=False)

    st.success("Cycle data saved successfully!")

st.divider()

st.subheader("AI Wellness Suggestion")

if current_day <= 5:

    st.warning("🩸 Your period phase. Prioritize rest, hydration, and light study sessions.")

elif current_day <= 13:

    st.success("⚡ Energy is generally increasing. A good time for focused study.")

elif current_day <= 16:

    st.info("🌼 Ovulation phase. You may feel energetic and productive.")

else:

    st.warning("🌙 Luteal phase. Plan regular breaks and maintain healthy sleep.")