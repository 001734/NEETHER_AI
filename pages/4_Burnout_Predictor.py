import streamlit as st
import pandas as pd

from utils.storage import save_today, last_7_days
from models.predict_lstm import predict_burnout

st.set_page_config(page_title="Burnout Predictor", page_icon="🧠")

st.title("🧠 Burnout Predictor (LSTM)")
st.write("Save your daily wellness data. After 7 days, the AI will predict your burnout risk.")

st.divider()

study = st.slider("📚 Study Hours", 0.0, 15.0, 6.0)

sleep = st.slider("😴 Sleep Hours", 0.0, 12.0, 7.0)

water = st.slider("💧 Water Intake (Litres)", 0.0, 5.0, 2.5)

energy = st.slider("⚡ Energy Level", 1, 10, 7)

mood = st.selectbox(
    "😊 Mood",
    [
        "Happy",
        "Normal",
        "Tired",
        "Stressed",
        "Anxious"
    ]
)

if st.button("💾 Save Today's Data"):

    save_today(
        study,
        sleep,
        water,
        energy,
        mood
    )

    st.success("Today's data has been saved successfully!")

st.divider()

history = last_7_days()

if history is None:

    st.warning("You need at least 7 days of wellness data before prediction.")

else:

    st.subheader("Last 7 Days")

    st.dataframe(history, use_container_width=True)

    if st.button("🔮 Predict Burnout"):

        sequence = history[
            [
                "StudyHours",
                "SleepHours",
                "WaterIntake",
                "Energy",
                "Mood"
            ]
        ].values.tolist()

        prediction, probability = predict_burnout(sequence)

        st.subheader("Prediction Result")

        if prediction == "Low":
            st.success("🟢 Low Burnout Risk")

        elif prediction == "Medium":
            st.warning("🟡 Medium Burnout Risk")

        else:
            st.error("🔴 High Burnout Risk")

        st.write("Prediction Probabilities")

        st.write(probability)

        st.divider()

        st.subheader("AI Recommendation")

        if prediction == "Low":

            st.success("""
Continue your healthy routine.

✅ Maintain sleep schedule

✅ Stay hydrated

✅ Continue balanced study sessions
""")

        elif prediction == "Medium":

            st.warning("""
Reduce study load slightly.

💧 Drink more water

😴 Sleep at least 7-8 hours

🧘 Take regular breaks
""")

        else:

            st.error("""
High Burnout Risk Detected!

🚨 Take a break

😴 Prioritize sleep

💧 Increase water intake

📚 Reduce study hours for a day

❤️ Practice relaxation
""")