import streamlit as st

st.set_page_config(page_title="Fraud Detection", page_icon="💳")

st.title("💳 Smart Fraud Detection System")
st.markdown("### 🔍 Check your own transaction (Real-life use)")

# -------------------------------
# Extra Inputs
# -------------------------------
transaction_type = st.selectbox("💼 Transaction Type", ["UPI", "Card", "Bank Transfer"])

col1, col2 = st.columns(2)

with col1:
    amount = st.number_input("💰 Amount", min_value=0.0)
    oldbalanceOrg = st.number_input("🏦 Old Balance (Sender)", min_value=0.0)
    newbalanceOrig = st.number_input("🏦 New Balance (Sender)", min_value=0.0)

with col2:
    oldbalanceDest = st.number_input("🏦 Old Balance (Receiver)", min_value=0.0)
    newbalanceDest = st.number_input("🏦 New Balance (Receiver)", min_value=0.0)

# -------------------------------
# Smart Detection
# -------------------------------
def detect_fraud(amount, oldOrg, newOrig, oldDest, newDest):
    
    score = 0
    reasons = []

    if abs((oldOrg - amount) - newOrig) > 1:
        score += 2
        reasons.append("❌ Sender balance mismatch")

    if oldDest == newDest and amount > 0:
        score += 2
        reasons.append("❌ Receiver balance not updated")

    if amount > 100000:
        score += 1
        reasons.append("⚠️ Large transaction")

    if oldOrg <= 0 and amount > 0:
        score += 2
        reasons.append("❌ No balance but transaction done")

    if (newDest - oldDest) > amount * 1.5:
        score += 1
        reasons.append("⚠️ Abnormal receiver balance jump")

    return score, reasons

# -------------------------------
# Prediction
# -------------------------------
if st.button("🚀 Check Transaction"):

    score, reasons = detect_fraud(
        amount, oldbalanceOrg, newbalanceOrig,
        oldbalanceDest, newbalanceDest
    )

    st.subheader("📊 Result")

    if score >= 3:
        st.error(f"🚨 Fraud Detected (Risk Score: {score}/6)")
        risk = "HIGH 🔴"
    elif score == 2:
        st.warning(f"⚠️ Suspicious Transaction (Risk Score: {score}/6)")
        risk = "MEDIUM 🟡"
    else:
        st.success(f"✅ Safe Transaction (Risk Score: {score}/6)")
        risk = "LOW 🟢"

    st.markdown(f"### 🎯 Risk Level: {risk}")

    # Show reasons
    if reasons:
        st.markdown("### 🔍 Reasons:")
        for r in reasons:
            st.write(r)
    else:
        st.write("No suspicious activity detected")

# Footer
st.markdown("---")
st.markdown("💡 Use this tool to analyze your own transactions safely")
