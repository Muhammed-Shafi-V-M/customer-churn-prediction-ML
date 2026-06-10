import streamlit as st
import pandas as pd
import joblib
import plotly.express as px
import plotly.graph_objects as go

# ==================================
# PAGE CONFIG
# ==================================
st.set_page_config(
    page_title="Customer Churn Dashboard",
    page_icon="⚠",
    layout="wide"
)

# ==================================
# CUSTOM CSS
# ==================================
st.markdown("""
<style>

.main {
    background-color: #0E1117;
}

h1 {
    color: #00E5FF;
    text-align: center;
    font-weight: 700;
}

.stButton>button {
    width: 100%;
    height: 55px;
    border-radius: 12px;
    border: none;
    font-size: 18px;
    font-weight: bold;
    color: white;
    background: linear-gradient(90deg,#00E5FF,#7B61FF);
}

.stButton>button:hover {
    background: linear-gradient(90deg,#7B61FF,#00E5FF);
}

[data-testid="stMetric"] {
    background-color: #161B22;
    padding: 15px;
    border-radius: 15px;
    border: 1px solid #2A2F3A;
}

section[data-testid="stSidebar"] {
    background-color: #161B22;
}

</style>
""", unsafe_allow_html=True)

# ==================================
# LOAD MODEL
# ==================================
model = joblib.load("churn_model.pkl")

# ==================================
# HEADER
# ==================================
st.markdown(
    "<h1>⚠ Customer Churn Analytics Dashboard</h1>",
    unsafe_allow_html=True
)

st.markdown(
    """
    Predict whether a customer is likely to leave the company based on customer behavior and subscription details.
    """
)

st.divider()

# ==================================
# SIDEBAR INPUTS
# ==================================
st.sidebar.header("📋 Customer Information")

gender = st.sidebar.selectbox(
    "Gender",
    ["Female", "Male"]
)

senior = st.sidebar.selectbox(
    "Senior Citizen",
    ["No", "Yes"]
)

partner = st.sidebar.selectbox(
    "Partner",
    ["No", "Yes"]
)

dependents = st.sidebar.selectbox(
    "Dependents",
    ["No", "Yes"]
)

tenure = st.sidebar.slider(
    "Tenure (Months)",
    0,
    72,
    12
)

phone = st.sidebar.selectbox(
    "Phone Service",
    ["No", "Yes"]
)

multiple = st.sidebar.selectbox(
    "Multiple Lines",
    ["No", "Yes"]
)

internet = st.sidebar.selectbox(
    "Internet Service",
    ["No", "Yes"]
)

security = st.sidebar.selectbox(
    "Online Security",
    ["No", "Yes"]
)

backup = st.sidebar.selectbox(
    "Online Backup",
    ["No", "Yes"]
)

device = st.sidebar.selectbox(
    "Device Protection",
    ["No", "Yes"]
)

support = st.sidebar.selectbox(
    "Tech Support",
    ["No", "Yes"]
)

tv = st.sidebar.selectbox(
    "Streaming TV",
    ["No", "Yes"]
)

movies = st.sidebar.selectbox(
    "Streaming Movies",
    ["No", "Yes"]
)

contract = st.sidebar.selectbox(
    "Contract Type",
    [
        "Month-to-Month",
        "One Year",
        "Two Year"
    ]
)

paperless = st.sidebar.selectbox(
    "Paperless Billing",
    ["No", "Yes"]
)

payment = st.sidebar.selectbox(
    "Payment Method",
    [
        "Electronic Check",
        "Mailed Check",
        "Bank Transfer",
        "Credit Card"
    ]
)

monthly = st.sidebar.number_input(
    "Monthly Charges",
    min_value=0.0,
    value=50.0
)

total = st.sidebar.number_input(
    "Total Charges",
    min_value=0.0,
    value=500.0
)

# ==================================
# MAPPINGS
# ==================================
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

# ==================================
# PREDICT BUTTON
# ==================================
predict_btn = st.button(
    "🔍 Predict Customer Churn"
)

# ==================================
# PREDICTION
# ==================================
if predict_btn:

    customer = pd.DataFrame([{
        "gender": 1 if gender == "Male" else 0,
        "SeniorCitizen": yes_no[senior],
        "Partner": yes_no[partner],
        "Dependents": yes_no[dependents],
        "tenure": tenure,
        "PhoneService": yes_no[phone],
        "MultipleLines": yes_no[multiple],
        "InternetService": yes_no[internet],
        "OnlineSecurity": yes_no[security],
        "OnlineBackup": yes_no[backup],
        "DeviceProtection": yes_no[device],
        "TechSupport": yes_no[support],
        "StreamingTV": yes_no[tv],
        "StreamingMovies": yes_no[movies],
        "Contract": contract_map[contract],
        "PaperlessBilling": yes_no[paperless],
        "PaymentMethod": payment_map[payment],
        "MonthlyCharges": monthly,
        "TotalCharges": total
    }])

    prediction = model.predict(customer)[0]

    try:
        churn_probability = model.predict_proba(customer)[0][1]
    except:
        churn_probability = 0.5

    # ==========================
    # RESULT CARD
    # ==========================
    if prediction == 1:

        st.markdown("""
        <div style="
        background:#3A0F0F;
        padding:20px;
        border-radius:15px;
        border-left:6px solid red;
        margin-bottom:20px;">
        <h2>⚠ High Churn Risk</h2>
        <p>Customer is likely to leave the company.</p>
        </div>
        """, unsafe_allow_html=True)

    else:

        st.markdown("""
        <div style="
        background:#103A1D;
        padding:20px;
        border-radius:15px;
        border-left:6px solid green;
        margin-bottom:20px;">
        <h2>✅ Low Churn Risk</h2>
        <p>Customer is likely to stay with the company.</p>
        </div>
        """, unsafe_allow_html=True)

    # ==========================
    # KPI CARDS
    # ==========================
    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "Tenure",
            f"{tenure} Months"
        )

    with c2:
        st.metric(
            "Monthly Charges",
            f"${monthly:.2f}"
        )

    with c3:
        st.metric(
            "Risk Score",
            f"{churn_probability * 100:.1f}%"
        )

    st.divider()

    # ==========================
    # GAUGE CHART
    # ==========================
    gauge_chart = go.Figure(go.Indicator(
        mode="gauge+number",
        value=churn_probability * 100,
        title={"text": "Customer Churn Risk (%)"},
        gauge={
            "axis": {"range": [0, 100]}
        }
    ))

    # ==========================
    # SERVICE CHART
    # ==========================
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

    service_chart = px.bar(
        service_df,
        x="Service",
        y="Status",
        title="Customer Service Usage"
    )

    # ==========================
    # CHARGES CHART
    # ==========================
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

    charges_chart = px.bar(
        charges_df,
        x="Type",
        y="Amount",
        title="Customer Charges Analysis"
    )

    # ==========================
    # FEATURE IMPORTANCE
    # ==========================
    feature_chart = None

    if hasattr(model, "feature_importances_"):

        feature_df = pd.DataFrame({
            "Feature": customer.columns,
            "Importance": model.feature_importances_
        })

        feature_df = feature_df.sort_values(
            by="Importance",
            ascending=False
        )

        feature_chart = px.bar(
            feature_df.head(10),
            x="Importance",
            y="Feature",
            orientation="h",
            title="Top Churn Drivers"
        )

    # ==========================
    # DASHBOARD LAYOUT
    # ==========================
    col1, col2 = st.columns(2)

    with col1:
        st.plotly_chart(
            gauge_chart,
            use_container_width=True
        )

    with col2:
        st.plotly_chart(
            service_chart,
            use_container_width=True
        )

    col3, col4 = st.columns(2)

    with col3:
        st.plotly_chart(
            charges_chart,
            use_container_width=True
        )

    with col4:
        if feature_chart:
            st.plotly_chart(
                feature_chart,
                use_container_width=True
            )