
# 🚨 Appointment No-Show Prediction System

A machine learning–based web application that predicts the likelihood of a patient missing a scheduled appointment using historical and behavioral data. The system provides a **risk score** instead of a simple yes/no prediction, enabling smarter scheduling and reminder strategies.



## 📌 Problem Statement
Appointment no-shows cause significant operational and financial losses in healthcare clinics, diagnostic centers, and service-based businesses. Missed appointments lead to wasted time slots, increased waiting times, and inefficient resource utilization.

Traditional reminder systems treat all appointments equally and fail to identify high-risk no-show cases in advance.



## 💡 Proposed Solution
This project implements a **machine learning-driven prediction system** that analyzes appointment details and past behavior to estimate the probability of a no-show.

The solution includes:
- A trained ML model for no-show prediction
- A Streamlit-based web interface
- Risk-based output to support decision-making


## 🧠 Machine Learning Approach
- **Problem Type:** Binary Classification
- **Model Used:** Random Forest Classifier
- **Target Variable:** No-Show (Yes / No)
- **Output:** Probability score (0–100%)

The trained model and encoders are stored and reused for fast inference during deployment.



## 🛠️ Tech Stack
- **Programming Language:** Python  
- **ML Libraries:** Scikit-learn, Pandas, NumPy  
- **Visualization:** Matplotlib  
- **Web Framework:** Streamlit  



## ⚙️ Key Features
- Real-time appointment no-show risk prediction
- Risk score output instead of binary result
- Batch prediction using CSV upload
- Pre-trained model for fast response
- Clean and interactive web dashboard



## 📂 Project Structure

Appointment-No-Show-Predictor/
├── app.py                  # Streamlit web application
├── model.py                # Model training logic
├── encoders.pkl             # Saved label encoders
├── no_show_model.pkl        # Trained ML model
├── appointment_data.csv     # Sample dataset
└── README.md                # Project documentation





## ▶️ How to Run the Project

### Step 1: Install Dependencies
Install all required libraries using the requirements file to ensure environment consistency.


pip install -r requirements.txt


### Step 2: Run the Application

Launch the Streamlit web application using the following command:


streamlit run app.py



## 📦 Requirements

The `requirements.txt` file includes the following dependencies:

* streamlit
* scikit-learn
* pandas
* numpy
* matplotlib


s.



