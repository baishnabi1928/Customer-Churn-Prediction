📊 ChurnScope — Customer Churn Prediction System A Machine Learning + Web Application that predicts whether a telecom customer is likely to churn (leave the service) based on their profile, services, and billing information. The system uses a Random Forest machine learning model trained on the Telco Customer Churn dataset and provides an interactive web interface for prediction and analysis.

🚀 Project Overview Customer churn prediction helps telecom companies identify customers who are likely to leave and take preventive actions.

This project:

Builds a machine learning model to predict churn Provides a Flask web application for user input Displays churn probability and risk analysis Shows model comparison and performance metrics

🧠 Machine Learning Models Tested Three classification models were evaluated:

Model Accuracy 🌲 Random Forest 84% (Best Model) ⚡ XGBoost 83% 🌿 Decision Tree 78%

Random Forest was selected because it provided better generalization and performance.

📁 Project Structure ChurnScope/ │ ├── app.py # Flask backend ├── churn_model.pkl # Trained ML model ├── customer churn.csv # Dataset ├── templates/ │ └── index.html # Frontend UI │ ├── README.md # Project documentation └── requirements.txt # Dependencies

⚙️ Technologies Used Programming

Python Machine Learning Scikit-learn NumPy Pandas Backend Flask Frontend HTML CSS JavaScript Visualization

Custom UI components Risk score gauge Model comparison dashboard

📊 Dataset The project uses the Telco Customer Churn Dataset which includes: Customer demographics Account information Billing details Services used Churn label

Key Features:

Gender Tenure Monthly Charges Contract Type Internet Service Payment Method Online Security Tech Support

Streaming Services

🔍 Features of the Application 1️⃣ Churn Prediction Users enter customer information and the system predicts:

Churn Risk Percentage Risk Category (Low / Moderate / High)

2️⃣ Customer Risk Analysis The system highlights: Key churn factors Customer profile summary Risk indicators

3️⃣ Retention Suggestions For high-risk customers the system recommends actions like:

Contract upgrade Service bundling Pricing adjustments Auto-pay incentives

4️⃣ Model Comparison Dashboard The application also includes a model comparison page showing:

Accuracy comparison Feature importance Confusion matrix Performance metrics

📈 Model Performance Random Forest Results: Metric Score Accuracy 84% Churn Recall 70.7% Churn Precision 78.6% Stay Recall 91.5% Stay Precision 87.6%

Confusion Matrix: Predicted Stay Predicted Chur Actual Stay 1148 107 Actual Churn 163 393

💻 Installation & Setup

1️⃣ Clone the repository git clone https://github.com/yourusername/churnscope.git cd churnscope 2️⃣ Install dependencies pip install flask numpy scikit-learn pandas 3️⃣ Run the application python app.py 4️⃣ Open in browser http://127.0.0.1:5000 🖥️ Application Interface

Main Components: Customer Input Form Risk Prediction Dashboard Model Comparison Page Feature Importance Visualization

🎯 Use Cases This system can help companies: Identify customers likely to leave Improve customer retention strategies Reduce revenue loss Personalize offers for customers

📌 Future Improvements Possible enhancements: Deploy on AWS / Render / Heroku Add real-time database

Implement Deep Learning models

Add SHAP explainability

Create API for external integrations