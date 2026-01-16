import streamlit as st
import re
from urllib.parse import urlparse

# --- PAGE SETUP ---
st.set_page_config(page_title="Cyber Security Tool Suite", page_icon="🔒")
st.title("🔒 Cyber Security Student Toolkit")
st.write("Select a tool from the sidebar to begin.")

# --- SIDEBAR MENU ---
menu = ["Home", "Password Strength Checker", "Phishing Link Scanner"]
choice = st.sidebar.selectbox("Choose Tool", menu)

# --- HOME PAGE ---
if choice == "Home":
    st.info("Welcome! This application demonstrates two common cybersecurity defenses.")
    st.markdown("""
    * **Password Checker:** Validates complexity (Length, Uppercase, Numbers, Symbols).
    * **Phishing Scanner:** Checks URLs for IP usage, length, and typosquatting.
    """)

# --- TOOL 1: PASSWORD CHECKER ---
elif choice == "Password Strength Checker":
    st.header("🔑 Password Strength Checker")
    password = st.text_input("Enter Password", type="password")
    
    if st.button("Check Strength"):
        score = 0
        feedback = []
        
        # Logic
        if len(password) >= 8: score += 1
        else: feedback.append("❌ Too short (needs 8+ chars)")
        
        if re.search(r'[A-Z]', password): score += 1
        else: feedback.append("❌ Missing uppercase letter")
        
        if re.search(r'\d', password): score += 1
        else: feedback.append("❌ Missing a number")
        
        if re.search(r'[\W_]', password): score += 1
        else: feedback.append("❌ Missing special character")
        
        # Display Results
        st.write(f"**Score: {score}/4**")
        if score == 4:
            st.success("Result: STRONG Password ✅")
        elif score >= 2:
            st.warning("Result: MODERATE Password ⚠️")
        else:
            st.error("Result: WEAK Password ❌")
            
        for tip in feedback:
            st.write(tip)

# --- TOOL 2: PHISHING SCANNER ---
elif choice == "Phishing Link Scanner":
    st.header("🎣 Phishing Link Scanner")
    url = st.text_input("Enter URL (e.g., http://google.com)")
    
    if st.button("Scan URL"):
        if not url:
            st.warning("Please enter a URL first.")
        else:
            parsed = urlparse(url)
            domain = parsed.netloc
            risk_score = 0
            warnings = []

            # 1. IP Check
            if re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", domain):
                warnings.append("🚩 URL uses an IP address instead of a domain.")
                risk_score += 1
            
            # 2. Length Check
            if len(domain) > 50:
                warnings.append("🚩 Domain is suspiciously long.")
                risk_score += 1
            
            # 3. Typosquatting
            suspicious_keywords = ["goog1e", "paypa1", "amaz0n", "faceb00k"]
            for keyword in suspicious_keywords:
                if keyword in domain:
                    warnings.append(f"🚩 Possible typosquatting detected ({keyword}).")
                    risk_score += 1

            # Verdict
            if risk_score == 0:
                st.success("✅ No obvious threats detected.")
            else:
                st.error(f"⚠️ CAUTION: {risk_score} Risk Factors Found!")
                for w in warnings:
                    st.write(w)