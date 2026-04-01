import streamlit as st
import numpy as np

# Page config
st.set_page_config(page_title="Fraud Detection", page_icon="💳")

st.title("💳 Online Payment Fraud Detection")
st.markdown("### 🔍 Check whether a transaction is Fraud or Safe")

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
# Strong Fraud Logic
# -------------------------------
def detect_fraud(amount, oldOrg, newOrig, oldDest, newDest):
    
    score = 0

    # Rule 1: balance mismatch
    if oldOrg - amount != newOrig:
        score += 1

    # Rule 2: receiver balance unchanged (suspicious)
    if oldDest == newDest:
        score += 1

    # Rule 3: very large transaction
    if amount > 200000:
        score += 1

    # Rule 4: zero balance sender (fraud pattern)
    if oldOrg == 0 and amount > 0:
        score += 1

    # Rule 5: sudden huge jump in receiver balance
    if newDest - oldDest > amount * 2:
        score += 1

    return score

# -------------------------------
# Prediction
# -------------------------------
if st.button("🚀 Predict"):
    
    fraud_score = detect_fraud(amount, oldbalanceOrg, newbalanceOrig,
                               oldbalanceDest, newbalanceDest)

    st.subheader("📊 Result")

    if fraud_score >= 2:
        st.error(f"🚨 Fraud Detected! (Risk Score: {fraud_score}/5)")
    else:
        st.success(f"✅ Safe Transaction (Risk Score: {fraud_score}/5)")

# Footer
st.markdown("---")
st.markdown("💡 Rule-based Fraud Detection System")
