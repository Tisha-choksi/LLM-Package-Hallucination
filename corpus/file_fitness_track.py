import streamlit as st
import pandas as pd
import numpy as np

# Initialize session state for workout history
if 'workouts' not in st.session_state:
    st.session_state.workouts = []

# Title of the app
st.title("Fitness Tracker")

# Input fields for workout logging
date = st.date_input("Date")
workout_type = st.text_input("Workout Type")
duration = st.number_input("Duration (minutes)", min_value=1)

# Button to log the workout
if st.button("Log Workout"):
    # Append new workout to session state
    st.session_state.workouts.append({
        'Date': date,
        'Workout Type': workout_type,
        'Duration': duration
    })
    st.success("Workout logged!")

# Display workout history
if st.session_state.workouts:
    st.subheader("Workout History")
    workout_df = pd.DataFrame(st.session_state.workouts)
    st.dataframe(workout_df)
else:
    st.write("No workouts logged yet.")
