
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from model import train_model, preprocess_input

st.set_page_config(page_title="No-Show Predictor", layout="wide")

st.title("🚨 Appointment No-Show Risk Prediction Dashboard")

# Load ML model
model, label_encoders, feature_cols = train_model()

# Sidebar – CSV Upload
st.sidebar.header("📂 Upload Appointment CSV")
uploaded_file = st.sidebar.file_uploader("Upload CSV", type=["csv"])

# Manual prediction
st.subheader("📝 Predict Single Appointment")

col1, col2, col3 = st.columns(3)

with col1:
    day = st.selectbox("Appointment Day",
                       ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"])
    gap = st.slider("Booking Gap (Days)", 0, 30, 5)

with col2:
    time = st.selectbox("Time Slot",
                        ["Morning","Afternoon","Evening"])
    prev = st.slider("Previous No-Shows", 0, 5, 0)

with col3:
    sms = st.selectbox("SMS Reminder Sent?", ["Yes","No"])
    dist = st.slider("Distance (km)", 1, 25, 5)

atype = st.selectbox("Appointment Type",
                     ["Checkup","Test","Consultation"])

if st.button("🔍 Predict Risk"):
    input_df = pd.DataFrame([{
        "Appointment_Day": day,
        "Time_Slot": time,
        "Booking_Gap": gap,
        "Previous_No_Shows": prev,
        "SMS_Reminder": sms,
        "Distance_km": dist,
        "Appointment_Type": atype
    }])

    input_df = preprocess_input(input_df, label_encoders)
    risk = model.predict_proba(input_df)[0][1] * 100

    if risk > 70:
        st.error(f"High No-Show Risk: {risk:.2f}%")
    elif risk > 40:
        st.warning(f"Medium No-Show Risk: {risk:.2f}%")
    else:
        st.success(f"Low No-Show Risk: {risk:.2f}%")

# CSV batch prediction
if uploaded_file:
    st.subheader("📊 Batch Prediction Results")

    csv_df = pd.read_csv(uploaded_file)
    st.dataframe(csv_df.head())

    processed_df = preprocess_input(csv_df.copy(), label_encoders)
    risks = model.predict_proba(processed_df[feature_cols])[:,1] * 100

    csv_df["No_Show_Risk_%"] = risks.round(2)
    st.dataframe(csv_df)

    st.subheader("📈 Risk Distribution")
    fig, ax = plt.subplots()
    ax.hist(risks, bins=20)
    ax.set_xlabel("No-Show Risk (%)")
    ax.set_ylabel("Number of Appointments")
    st.pyplot(fig)
