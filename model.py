
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

def train_model():
    np.random.seed(42)

    data = {
        "Appointment_Day": np.random.choice(
            ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"], 500),
        "Time_Slot": np.random.choice(
            ["Morning","Afternoon","Evening"], 500),
        "Booking_Gap": np.random.randint(0, 30, 500),
        "Previous_No_Shows": np.random.randint(0, 5, 500),
        "SMS_Reminder": np.random.choice(["Yes","No"], 500),
        "Distance_km": np.random.randint(1, 25, 500),
        "Appointment_Type": np.random.choice(
            ["Checkup","Test","Consultation"], 500),
        "No_Show": np.random.choice([0,1], 500, p=[0.7,0.3])
    }

    df = pd.DataFrame(data)

    label_encoders = {}
    for col in df.select_dtypes(include='object').columns:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        label_encoders[col] = le

    X = df.drop("No_Show", axis=1)
    y = df["No_Show"]

    model = RandomForestClassifier(n_estimators=200, random_state=42)
    model.fit(X, y)

    return model, label_encoders, X.columns


def preprocess_input(df, label_encoders):
    for col in label_encoders:
        if col in df.columns:
            df[col] = label_encoders[col].transform(df[col])
    return df
