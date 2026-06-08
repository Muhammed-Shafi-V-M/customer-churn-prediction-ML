import streamlit as st
import pandas as pd
import joblib
import plotly.express as px
import plotly.graph_objects as go

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Customer Churn Dashboard",
    page_icon="📊",
    layout="wide"
)

# -----------------------------
# LOAD MODEL
# -----------------------------
model = joblib.load("churn_model.pkl")

# -----------------------------
# TITLE
# -----------------------------
st.title("📊 Customer Churn Prediction Dashboard")
st.markdown(
    "Analyze customer information and predict whether the customer is likely to churn."
)

st.divider()

# -----------------------------
# INPUTS
# -----------------------------
col1, col2 = st.columns(2)

with col1:

    gender = st.selectbox(
        "Gender",
        ["Female", "Male"]
    )

    senior = st.selectbox(
        "Senior Citizen",
        ["No", "Yes"]
    )

    partner = st.selectbox(
        "Partner",
        ["No", "Yes"]
    )

    dependents = st.selectbox(
        "Dependents",
        ["No", "Yes"]
    )

    tenure = st.slider(
        "Tenure (Months)",
        0,
        72,
        12
    )

    phone = st.selectbox(
        "Phone Service",
        ["No", "Yes"]
    )

    multiple = st.selectbox(
        "Multiple Lines",
        ["No", "Yes"]
    )

    internet = st.selectbox(
        "Internet Service",
        ["No", "Yes"]
    )

    security = st.selectbox(
        "Online Security",
        ["No", "Yes"]
    )

    backup = st.selectbox(
        "Online Backup",
        ["No", "Yes"]
    )

with col2:

    device = st.selectbox(
        "Device Protection",
        ["No", "Yes"]
    )

    support = st.selectbox(
        "Tech Support",
        ["No", "Yes"]
    )

    tv = st.selectbox(
        "Streaming TV",
        ["No", "Yes"]
    )

    movies = st.selectbox(
        "Streaming Movies",
        ["No", "Yes"]
    )

    contract = st.selectbox(
        "Contract Type",
        [
            "Month-to-Month",
            "One Year",
            "Two Year"
        ]
    )

    paperless = st.selectbox(
        "Paperless Billing",
        ["No", "Yes"]
    )

    payment = st.selectbox(
        "Payment Method",
        [
            "Electronic Check",
            "Mailed Check",
            "Bank Transfer",
            "Credit Card"
        ]
    )

    monthly = st.number_input(
        "Monthly Charges",
        min_value=0.0,
        value=50.0
    )

    total = st.number_input(
        "Total Charges",
        min_value=0.0,
        value=500.0
    )

# -----------------------------
# MAPPINGS
# -----------------------------
yes_no = {
    "No": 0,
    "Yes": 1
}

contract_map = {
    "Month-to-Month": 0,
    "One Year": 1,
    "Two Year": 2
}

payment_map = {
    "Electronic Check": 0,
    "Mailed Check": 1,
    "Bank Transfer": 2,
    "Credit Card": 3
}

# -----------------------------
# PREDICTION
# -----------------------------
if st.button("🔍 Predict Customer Churn", use_container_width=True):

    customer = pd.DataFrame([{
        'gender': 1 if gender == "Male" else 0,
        'SeniorCitizen': yes_no[senior],
        'Partner': yes_no[partner],
        'Dependents': yes_no[dependents],
        'tenure': tenure,
        'PhoneService': yes_no[phone],
        'MultipleLines': yes_no[multiple],
        'InternetService': yes_no[internet],
        'OnlineSecurity': yes_no[security],
        'OnlineBackup': yes_no[backup],
        'DeviceProtection': yes_no[device],
        'TechSupport': yes_no[support],
        'StreamingTV': yes_no[tv],
        'StreamingMovies': yes_no[movies],
        'Contract': contract_map[contract],
        'PaperlessBilling': yes_no[paperless],
        'PaymentMethod': payment_map[payment],
        'MonthlyCharges': monthly,
        'TotalCharges': total
    }])

    prediction = model.predict(customer)[0]

    try:
        probability = model.predict_proba(customer)[0][1]
    except:
        probability = 0.5

    st.divider()

    # -----------------------------
    # RESULT
    # -----------------------------
    if prediction == 1:
        st.error(
            f"⚠ HIGH CHURN RISK ({probability*100:.1f}%)"
        )
    else:
        st.success(
            f"✅ LOW CHURN RISK ({(1-probability)*100:.1f}%)"
        )

    # -----------------------------
    # KPI CARDS
    # -----------------------------
    k1, k2, k3 = st.columns(3)

    k1.metric(
        "Tenure",
        f"{tenure} Months"
    )

    k2.metric(
        "Monthly Charges",
        f"${monthly:.2f}"
    )

    k3.metric(
        "Risk Score",
        f"{probability*100:.1f}%"
    )

    st.divider()

    # -----------------------------
    # CHURN RISK GAUGE
    # -----------------------------
    fig_gauge = go.Figure(go.Indicator(
        mode="gauge+number",
        value=probability * 100,
        title={"text": "Churn Risk (%)"},
        gauge={
            "axis": {"range": [0, 100]}
        }
    ))

    st.plotly_chart(
        fig_gauge,
        use_container_width=True
    )

    # -----------------------------
    # SERVICE USAGE CHART
    # -----------------------------
    service_df = pd.DataFrame({
        "Service": [
            "Online Security",
            "Online Backup",
            "Device Protection",
            "Tech Support",
            "Streaming TV",
            "Streaming Movies"
        ],
        "Status": [
            yes_no[security],
            yes_no[backup],
            yes_no[device],
            yes_no[support],
            yes_no[tv],
            yes_no[movies]
        ]
    })

    fig_service = px.bar(
        service_df,
        x="Service",
        y="Status",
        title="Customer Service Usage"
    )

    st.plotly_chart(
        fig_service,
        use_container_width=True
    )

    # -----------------------------
    # CHARGES ANALYSIS
    # -----------------------------
    charges_df = pd.DataFrame({
        "Type": [
            "Monthly Charges",
            "Total Charges"
        ],
        "Amount": [
            monthly,
            total
        ]
    })

    fig_charges = px.bar(
        charges_df,
        x="Type",
        y="Amount",
        title="Charges Analysis"
    )

    st.plotly_chart(
        fig_charges,
        use_container_width=True
    )

    # -----------------------------
    # FEATURE IMPORTANCE
    # -----------------------------
    if hasattr(model, "feature_importances_"):

        feature_df = pd.DataFrame({
            "Feature": customer.columns,
            "Importance": model.feature_importances_
        })

        feature_df = feature_df.sort_values(
            by="Importance",
            ascending=False
        )

        fig_importance = px.bar(
            feature_df.head(10),
            x="Importance",
            y="Feature",
            orientation="h",
            title="Top Factors Influencing Churn"
        )

        st.plotly_chart(
            fig_importance,
            use_container_width=True
        )