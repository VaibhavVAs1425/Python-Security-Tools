# Python-Security-Tools

# 🛡️ Cybersecurity & Network Security Toolkit

A collection of Python-based tools developed to understand core security concepts, including input validation, threat detection, and endpoint monitoring.

## 📂 Projects Included

### 1. Password Strength & Phishing Scanner (Web App)
A unified interface built with **Streamlit** that demonstrates defensive coding.
* **Password Validator:** Audits password complexity using Regex to prevent weak credentials.
* **Phishing Scanner:** heuristic analysis of URLs to detect IP-based domains and typosquatting (e.g., `goog1e.com`).

### 2. Educational Keylogger (Endpoint Security)
A Python-based GUI application designed to demonstrate how malware persists and captures data.
* **Tech Stack:** Python, Tkinter (GUI), Pynput (Keyboard Hooks), Threading.
* **Objective:** Built to understand the importance of Endpoint Detection and Response (EDR) systems in detecting behavioral anomalies.

## 🚀 How to Run

### Web Application
1. Install dependencies: `pip install -r requirements.txt`
2. Run the app: `streamlit run web_app.py`

### Keylogger (GUI)
1. Run the script: `python keylogger_gui.py`
2. Or use the compiled `.exe` version (Windows only).

---
*⚠️ **Disclaimer:** These tools are developed for educational and ethical testing purposes only. Usage of the keylogger on systems without permission is illegal.*
