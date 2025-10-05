# StellarSynth

**AI-Powered Exoplanet Candidate Classification Using TESS Data**

---

## Project Overview
StellarSynth is an AI-based application designed to classify exoplanet candidates using NASA’s **Transiting Exoplanet Survey Satellite (TESS)** dataset. The system analyzes key astrophysical parameters, such as orbital period, transit depth, planetary radius, and stellar properties, to predict whether a candidate is likely to be a confirmed planet or a false positive.

The goal of StellarSynth is to demonstrate how artificial intelligence can accelerate exoplanet discovery by automating classification, reducing manual analysis, and highlighting high-potential candidates.

---

## Key Features
- Predicts the disposition of exoplanet candidates (confirmed planet or false positive)
- Uses an **XGBoost** machine learning model for accurate classification
- Interactive **Streamlit** web application for real-time predictions
- Simple interface allowing users to input or upload candidate data

---

## Technology Stack
- **Programming Language:** Python
- **Libraries:** XGBoost, pandas, scikit-learn, joblib, Streamlit, NumPy
- **Deployment:** Streamlit Community Cloud
- **Data Source:** [NASA TESS Objects of Interest (TOI)](https://exoplanetarchive.ipac.caltech.edu/cgi-bin/TblView/nph-tblView?app=ExoTbls&config=TOI)

---

## How AI is Used
StellarSynth uses **XGBoost**, a supervised machine learning algorithm, to learn patterns from labeled TESS data. The model predicts the likelihood of a candidate being a confirmed planet or a false positive based on astrophysical features such as orbital period, transit depth, stellar temperature, and planet radius.

---

## Installation & Usage
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/StellarSynth.git
