import streamlit as st

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
# STRONG FRAUD LOGIC
# -------------------------------
def detect_fraud(amount, oldOrg, newOrig, oldDest, newDest):
    
    score = 0

    # Rule 1: Sender balance mismatch
    if abs((oldOrg - amount) - newOrig) > 1:
        score += 2

    # Rule 2: Receiver balance unchanged
    if oldDest == newDest and amount > 0:
        score += 2

    # Rule 3: Large transaction
    if amount > 100000:
        score += 1

    # Rule 4: Sender has no balance
    if oldOrg <= 0 and amount > 0:
        score += 2

    # Rule 5: Abnormal receiver increase
    if (newDest - oldDest) > amount * 1.5:
        score += 1

    return score

# -------------------------------
# Prediction
# -------------------------------
if st.button("🚀 Predict"):
    
    fraud_score = detect_fraud(
        amount, oldbalanceOrg, newbalanceOrig,
        oldbalanceDest, newbalanceDest
    )

    st.subheader("📊 Result")

    if fraud_score >= 3:
        st.error(f"🚨 Fraud Detected! (Risk Score: {fraud_score}/6)")
    else:
        st.success(f"✅ Safe Transaction (Risk Score: {fraud_score}/6)")

# Footer
st.markdown("---")
st.markdown("💡 Smart Rule-Based Fraud Detection System")
