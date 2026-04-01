import streamlit as st
import numpy as np
import pickle
import os

# Page config
st.set_page_config(page_title="Fraud Detection", page_icon="💳")

st.title("💳 Online Payment Fraud Detection")
st.markdown("### 🔍 Check whether a transaction is Fraud or Safe")

# -------------------------------
# DEBUG: Show current directory files
# -------------------------------
st.subheader("📁 Debug Info")
files = os.listdir()
st.write("Current Folder Files:", files)

# -------------------------------
# Load Model (SAFE)
# -------------------------------
model = None

if "model.pkl" in files:
    try:
        with open("model.pkl", "rb") as f:
            model = pickle.load(f)
        st.success("✅ Model loaded successfully!")
    except Exception as e:
        st.error(f"❌ Error loading model: {e}")
        st.stop()
else:
    st.error("❌ model.pkl not found! Please put it in same folder as app.py")
    st.stop()

# -------------------------------
# Input Section
# -------------------------------
st.subheader("📥 Enter Transaction Details")

col1, col2 = st.columns(2)

with col1:
    amount = st.number_input("💰 Amount", min_value=0.0)
    oldbalanceOrg = st.number_input("🏦 Old Balance (Sender)", min_value=0.0)
    newbalanceOrig = st.number_input("🏦 New Balance (Sender)", min_value=0.0)

with col2:
    oldbalanceDest = st.number_input("🏦 Old Balance (Receiver)", min_value=0.0)
    newbalanceDest = st.number_input("🏦 New Balance (Receiver)", min_value=0.0)

# -------------------------------
# Prediction
# -------------------------------
if st.button("🚀 Predict"):
    try:
        features = np.array([[amount, oldbalanceOrg, newbalanceOrig,
                              oldbalanceDest, newbalanceDest]])

        prediction = model.predict(features)

        st.subheader("📊 Result")

        if prediction[0] == 1:
            st.error("🚨 Fraud Transaction Detected!")
        else:
            st.success("✅ Safe Transaction")

    except Exception as e:
        st.error(f"⚠️ Prediction Error: {e}")

# Footer
st.markdown("---")
st.markdown("💡 Streamlit Fraud Detection App")
