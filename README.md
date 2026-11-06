# Customer Churn Prediction & Analysis System

**An End-to-End Machine Learning Project for Customer Retention and Predictive Analytics**

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Predictive%20Analytics-orange)
![Streamlit](https://img.shields.io/badge/Framework-Streamlit-FF4B4B?logo=streamlit)
![Status](https://img.shields.io/badge/Status-Completed-success)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 1. Project Overview

Customer retention is a major challenge for businesses operating in highly competitive markets. Acquiring new customers often requires more resources than retaining existing ones. Identifying customers who are likely to discontinue a service can help businesses take preventive action and improve customer retention.

This project focuses on developing a **Customer Churn Prediction System** using Machine Learning techniques. It analyzes customer information, identifies potential churn patterns, and predicts whether a customer is likely to leave a service.

The project combines data preprocessing, machine learning model development, and an interactive application to demonstrate how predictive analytics can support business decision-making.

## 2. Business Objectives

The primary objectives of this project are:

- Identify customers who are likely to churn.
- Understand customer characteristics associated with churn.
- Analyze customer behavior and subscription patterns.
- Develop a machine learning model to predict churn.
- Provide an interactive interface for customer-level predictions.
- Support data-driven customer retention strategies.

## 3. Technology Stack

| Technology | Purpose |
|---|---|
| Python | Data processing and model development |
| Pandas | Data manipulation and preprocessing |
| NumPy | Numerical operations |
| Scikit-learn | Machine Learning and model evaluation |
| Streamlit | Interactive prediction application |
| Joblib / Pickle | Model serialization and loading |
| CSV | Dataset storage |

## 4. Project Workflow

The project follows an end-to-end machine learning workflow:

**Step 1 – Data Collection**

The Telco Customer Churn dataset is used as the primary data source. It contains customer information, service subscriptions, account details, billing information, and churn status.

**Step 2 – Data Preprocessing**

- Inspect the dataset and understand its structure.
- Handle missing and inconsistent values.
- Prepare categorical and numerical variables.
- Transform the data into a suitable format for machine learning.

**Step 3 – Model Development**

- Prepare the training dataset.
- Train a machine learning classification model.
- Save the trained model for future predictions.
- Prepare the prediction pipeline.

**Step 4 – Model Deployment**

The trained model is integrated into an interactive Streamlit application. Users can provide customer information and receive churn predictions through the interface.

**Step 5 – Prediction**

The application processes customer inputs and generates a prediction indicating whether the customer is likely to churn.

## 5. Key Features

- Customer churn prediction using Machine Learning.
- Interactive customer input interface.
- Automated prediction using a saved model.
- Customer information processing.
- Easy-to-use Streamlit application.
- Reusable trained machine learning model.

## 6. Repository Structure

```text
customer-churn-prediction-ML/
│
├── app.py                # Streamlit application
├── train_model.py        # Model training script
├── churn_model.pkl       # Saved trained model
├── telco_churn.csv       # Customer churn dataset
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
```

## 7. Installation and Setup

Follow these instructions to run the project locally.

### Prerequisites

- Python 3.9 or later
- Git
- pip package manager

### Step 1 – Clone the Repository

```bash
git clone https://github.com/Muhammed-Shafi-V-M/customer-churn-prediction-ML.git
```

### Step 2 – Navigate to the Project Directory

```bash
cd customer-churn-prediction-ML
```

### Step 3 – Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4 – Run the Application

```bash
streamlit run app.py
```

The application will open in your default browser.

## 8. Model Evaluation

The machine learning model should be evaluated using appropriate classification metrics:

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

These metrics help assess the model's ability to identify customers who are likely to churn.

*Note: Actual model evaluation scores should be added here after validating the trained model. No performance figures are assumed.*

## 9. Business Applications

This solution demonstrates how businesses can use predictive analytics to:

- Identify customers at risk of leaving.
- Prioritize customer retention activities.
- Understand factors associated with customer churn.
- Support targeted customer engagement.
- Improve customer retention planning.

## 10. Future Enhancements

Potential improvements include:

- Adding an interactive customer analytics dashboard.
- Implementing feature importance and model explainability.
- Comparing multiple classification algorithms.
- Integrating real-time customer data.
- Deploying the application to a cloud platform.
- Adding customer segmentation and retention recommendations.

## 11. Author

**Muhammed Shafi V M**

Data Analyst | Python | SQL | Excel | Power BI | Machine Learning

Computer Engineering Graduate | 2025

- **GitHub:** [Muhammed-Shafi-V-M](https://github.com/Muhammed-Shafi-V-M)
- **Project Repository:** [Customer Churn Prediction ML](https://github.com/Muhammed-Shafi-V-M/customer-churn-prediction-ML)

---

*This project was developed as part of my practical work in Data Analytics and Machine Learning, demonstrating the application of data processing and predictive modelling to solve a real-world business problem.*

**If you find this project interesting, feel free to explore the repository.**
