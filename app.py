import streamlit as st
import numpy as np
import pickle

# Page config
st.set_page_config(page_title="Fraud Detection", page_icon="💳", layout="centered")

# Load model
@st.cache_resource
def load_model():
    try:
        model = pickle.load(open("model.pkl", "rb"))
        return model
    except:
        return None

model = load_model()

# Title
st.title("💳 Online Payment Fraud Detection")
st.markdown("### 🔍 Check whether a transaction is Fraud or Safe")

# Check model
if model is None:
    st.error("❌ model.pkl not found! Please train and save your model.")
    st.stop()

# Sidebar info
st.sidebar.header("ℹ️ Instructions")
st.sidebar.write("Enter transaction details and click Predict.")

# Input section
st.subheader("📥 Enter Transaction Details")

col1, col2 = st.columns(2)

with col1:
    amount = st.number_input("💰 Amount", min_value=0.0, step=1.0)
    oldbalanceOrg = st.number_input("🏦 Old Balance (Sender)", min_value=0.0)
    newbalanceOrig = st.number_input("🏦 New Balance (Sender)", min_value=0.0)

with col2:
    oldbalanceDest = st.number_input("🏦 Old Balance (Receiver)", min_value=0.0)
    newbalanceDest = st.number_input("🏦 New Balance (Receiver)", min_value=0.0)

# Prediction button
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
        st.error(f"⚠️ Error: {e}")

# Footer
st.markdown("---")
st.markdown("💡 Built using Streamlit | ML Project")
