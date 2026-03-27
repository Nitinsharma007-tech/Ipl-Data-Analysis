import streamlit as st
import pandas as pd
import numpy as np
import pickle

# -------------------------------
# Load Model & Encoders
# -------------------------------
model = pickle.load(open("Model files/model.pkl", "rb"))
le_team = pickle.load(open("Model files/le_team.pkl", "rb"))
le_venue = pickle.load(open("Model files/le_venue.pkl", "rb"))
le_toss = pickle.load(open("Model files/le_toss.pkl", "rb"))

# -------------------------------
# UI Title
# -------------------------------
st.title("🏏 IPL Match Winner Predictor")

st.write("Select match details below:")

# -------------------------------
# Dropdown Options (NO SPELLING ERROR)
# -------------------------------
teams = list(le_team.classes_)
venues = list(le_venue.classes_)
toss_options = list(le_toss.classes_)

# -------------------------------
# User Inputs (Dropdowns)
# -------------------------------
team1 = st.selectbox("Select Team 1", teams)
team2 = st.selectbox("Select Team 2", teams)

# Prevent same team selection
if team1 == team2:
    st.error("Team 1 and Team 2 cannot be the same!")
    st.stop()

toss_winner = st.selectbox("Toss Winner", [team1, team2])
toss_decision = st.selectbox("Toss Decision", toss_options)
venue = st.selectbox("Match Venue", venues)

# -------------------------------
# Prediction Button
# -------------------------------
if st.button("Predict Winner"):

    # Encoding
    team1_enc = le_team.transform([team1])[0]
    team2_enc = le_team.transform([team2])[0]
    toss_winner_enc = le_team.transform([toss_winner])[0]
    venue_enc = le_venue.transform([venue])[0]
    toss_decision_enc = le_toss.transform([toss_decision])[0]

    # Create DataFrame (Fix warning issue ✅)
    input_df = pd.DataFrame({
        'team1': [team1_enc],
        'team2': [team2_enc],
        'toss_winner': [toss_winner_enc],
        'toss_decision': [toss_decision_enc],
        'venue': [venue_enc]
    })

    # Prediction
    pred = model.predict(input_df)

    if pred[0] == 1:
        winner = team1
    else:
        winner = team2

    st.success(f"🏆 Predicted Winner: {winner}")