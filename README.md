## Insurance-Premium-predictor
 This project is an intelligent full-stack web application that predicts a customer's likelihood of paying an insurance premium, categorized into High, Medium, or Low chance levels. It features a clean Streamlit frontend, a fast and scalable FastAPI backend, and a machine learning model trained for multi-class classification.
 ## ✨ Features
 🎯 Multi-class classification for premium prediction: High / Medium / Low

⚡ FastAPI-based backend for efficient ML inference

🖥️ Streamlit frontend for intuitive user interaction

📈 Clean separation of concerns for easy maintenance and scaling

🔄 Real-time predictions based on user inputs
## 🧰 Tech Stack
Backend: FastAPI

Machine Learning: scikit-learn, pandas, joblib

Deployment Ready: Easy to containerize and scale
## 📦 Project Structure
insurance-premium-predictor/
├── app.py
│   
│
├── frontend.py
│   
│
├── insurance_premium_prediction.pkl
│__ insurance.csv
│__ insurance.ipynb
├── requirements.txt
└── README.md

## 🚀 Getting Started
### 1. Clone the repository
git clone https://github.com/your-username/insurance-premium-predictor.git

cd insurance-premium-predictor
### 2. Install dependencies
pip install -r requirements.txt
### 3. Run the FastAPI backend(if you are in vs code run first app.py then run frontend.py)
uvicorn app:app --reload
### 4. Start the Streamlit app
streamlit run frontend.py
## 🧠 Model Info
Type: Multi-class Classification

Labels: High, Medium, Low

Algorithm: Trained with scikit-learn classifiers (e.g., RandomForestClassifier)
## 🛠️ Possible Enhancements
Model retraining pipeline and versioning

Integration with a database for historical records

SHAP-based model explainability

Docker container for easy deployment
## 📬 Contact
Author: Amir 📧 [choudharyaamir828@gmail.com]


 
