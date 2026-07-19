# import streamlit as st

# st.set_page_config(
#     page_title="NEETHER AI",
#     page_icon="🌸",
#     layout="wide"
# )

# st.title("🌸 Welcome to NEETHER AI")
# st.subheader("Intelligent Wellness & AI Study Planner for Female NEET Aspirants")

# st.write(
#     """
#     ## Features
#     - 📅 Menstrual Cycle Tracker
#     - 📚 AI Study Planner
#     - 🧠 Burnout Prediction
#     - 💧 Water Intake Tracker
#     - 😴 Sleep Tracker
#     - 😊 Mood Tracker
#     - 📈 Progress Dashboard
#     """
# )

# st.success("NEETHER AI is running successfully!")
import streamlit as st

st.set_page_config(
    page_title="NEETHER AI",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🌸 NEETHER AI")

st.markdown("""
# Intelligent Wellness & AI Study Planner

Welcome to **NEETHER AI**.

Use the sidebar to navigate through the application.

### Modules

- 🏠 Dashboard
- 📅 Cycle Tracker
- 📚 Study Planner
- 🧠 Burnout Predictor
- 💡 Wellness Tips
""")

st.info("Select a page from the left sidebar.")