import streamlit as st
import pandas as pd
from datetime import date
import os

st.set_page_config(page_title="Wellness Tracker", layout="wide")

st.title("💖 Daily Wellness Tracker")

st.write("Track your daily health habits to receive personalized AI recommendations.")

st.divider()

col1,col2=st.columns(2)

with col1:

    sleep=st.slider(
        "Sleep Hours",
        0.0,
        12.0,
        7.5,
        0.5
    )

    water=st.slider(
        "Water Intake (L)",
        0.0,
        5.0,
        2.5,
        0.1
    )

    mood=st.selectbox(
        "Mood",
        [
            "Happy",
            "Normal",
            "Tired",
            "Stressed",
            "Anxious"
        ]
    )

with col2:

    energy=st.slider(
        "Energy Level",
        1,
        10,
        7
    )

    exercise=st.selectbox(
        "Exercise Today",
        [
            "No",
            "Walk",
            "Yoga",
            "Workout"
        ]
    )

    meals=st.slider(
        "Meals Taken",
        1,
        5,
        3
    )

notes=st.text_area("Notes")

st.divider()

score=0

score+=sleep*2
score+=water*5
score+=energy*3

if mood=="Happy":
    score+=20

elif mood=="Normal":
    score+=15

elif mood=="Tired":
    score+=8

elif mood=="Stressed":
    score+=5

else:
    score+=3

score=min(100,int(score))

st.subheader("Today's Wellness Score")

st.progress(score)

st.metric("Score",str(score)+"/100")

if score>=80:

    st.success("Excellent wellness today 🌸")

elif score>=60:

    st.info("Good. Maintain your routine.")

else:

    st.warning("Take more rest and stay hydrated.")

st.divider()

if st.button("Save Wellness Data"):

    row=pd.DataFrame({

        "Date":[date.today()],
        "SleepHours":[sleep],
        "WaterIntake":[water],
        "Mood":[mood],
        "Energy":[energy],
        "Exercise":[exercise],
        "Meals":[meals],
        "Notes":[notes]

    })

    file="data/wellness_data.csv"

    if os.path.exists(file):

        old=pd.read_csv(file)

        new=pd.concat([old,row],ignore_index=True)

        new.to_csv(file,index=False)

    else:

        row.to_csv(file,index=False)

    st.success("Data Saved Successfully!")

try:

    df=pd.read_csv("data/wellness_data.csv")

    st.subheader("Previous Records")

    st.dataframe(df,use_container_width=True)

except:
    pass