import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Dashboard", layout="wide")

st.title("🌸 NEETHER AI Dashboard")

st.write("Welcome back!")

st.divider()

col1,col2,col3,col4 = st.columns(4)

with col1:
    st.metric("📚 Study Hours","6 hrs","+1")

with col2:
    st.metric("😴 Sleep","7.5 hrs","+0.5")

with col3:
    st.metric("💧 Water","2.3 L","+0.2")

with col4:
    st.metric("😊 Mood","Happy")

st.divider()

study=np.random.randint(2,10,7)

chart=pd.DataFrame({
    "Day":["Mon","Tue","Wed","Thu","Fri","Sat","Sun"],
    "Study Hours":study
})

st.subheader("Weekly Study Progress")

st.line_chart(chart.set_index("Day"))

st.divider()

col1,col2=st.columns([2,1])

with col1:

    st.subheader("Today's AI Recommendation")

    st.success("""

    ✔ Study Biology first.

    ✔ Drink 2.5L Water.

    ✔ Sleep before 11 PM.

    ✔ Take a 20-minute revision break every 2 hours.

    """)

with col2:

    st.subheader("Burnout Risk")

    st.progress(20)

    st.success("Low Risk")