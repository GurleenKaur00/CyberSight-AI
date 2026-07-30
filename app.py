import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image
from pathlib import Path
import joblib
from textwrap import dedent
st.set_page_config(
    page_title="CyberSight AI",
    layout="wide",
    initial_sidebar_state="expanded"
)
BASE_DIR = Path(__file__).parent

DATA_PATH = BASE_DIR / "powerbi" / "network_traffic_dashboard.csv"

MODEL_PATH = BASE_DIR / "models" / "cybersight_rf_multiclass.pkl"

FEATURES_PATH = BASE_DIR / "models" / "multiclass_features.pkl"
LABEL_ENCODER_PATH = BASE_DIR / "models" / "attack_label_encoder.pkl"

IMAGES = BASE_DIR / "images"
@st.cache_data
def load_data():

    df = pd.read_csv(DATA_PATH)

    return df


df = load_data()
st.markdown("""
<style>

/* ==============================
GLOBAL
============================== */

#MainMenu{
visibility:hidden;
}

footer{
visibility:hidden;
}

header{
visibility:hidden;
}

.stApp{
background:#0F172A;
}


/* ==============================
SIDEBAR
============================== */

[data-testid="stSidebar"]{

background:#111827;

border-right:1px solid #1F2937;

}
/* Sidebar Text */

[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3,
[data-testid="stSidebar"] p,
[data-testid="stSidebar"] label{

    color:white !important;

}

/* ==============================
TEXT
============================== */

h1,h2,h3,h4,h5,h6{

color:white;

}

p{

color:#CBD5E1;

}
/* Markdown Text */

[data-testid="stMarkdownContainer"]{

    color:#E2E8F0 !important;

}

[data-testid="stMarkdownContainer"] ul{

    color:#E2E8F0 !important;

}

[data-testid="stMarkdownContainer"] li{

    color:#E2E8F0 !important;

    font-size:18px;

    line-height:1.8;

}

[data-testid="stMarkdownContainer"] strong{

    color:white;

}


/* ==============================
HERO
============================== */

.hero{

background:linear-gradient(
135deg,
#1E3A8A,
#2563EB,
#0F172A
);

padding:55px;

border-radius:28px;

margin-bottom:35px;

box-shadow:0px 12px 40px rgba(0,0,0,.40);

}

.hero-title{

font-size:60px;

font-weight:800;

color:white;

margin-bottom:10px;

}

.hero-subtitle{

font-size:25px;

color:#E2E8F0;

margin-bottom:15px;

}

.hero-tag{

font-size:18px;

color:#CBD5E1;

}


/* ==============================
SECTION
============================== */

.section-title{

font-size:34px;

font-weight:700;

color:white;

margin-top:20px;

margin-bottom:15px;

}


/* ==============================
CARDS
============================== */

.metric-card{

background:#1E293B;

border-radius:20px;

padding:24px;

min-height:240px;

display:flex;

flex-direction:column;

justify-content:space-between;

border-left:5px solid #3B82F6;

box-shadow:0 8px 22px rgba(0,0,0,.35);

transition:.35s;

overflow:hidden;

}

.metric-card:hover{

transform:translateY(-8px);

box-shadow:0px 18px 35px rgba(59,130,246,.35);

}

.metric-title{

font-size:18px;

color:#CBD5E1;

font-weight:600;

}

.metric-value{

font-size:38px;

font-weight:700;

line-height:1.35;

word-wrap:break-word;

overflow-wrap:break-word;

}

.metric-desc{

font-size:16px;

line-height:1.6;

color:#94A3B8;

}
.dashboard-card{

background:#1E293B;

border-radius:20px;

padding:24px;

height:180px;

display:flex;

flex-direction:column;

justify-content:space-between;

border-left:5px solid #2563EB;

box-shadow:0 8px 22px rgba(0,0,0,.35);

transition:.3s;

}

.dashboard-card:hover{

transform:translateY(-6px);

box-shadow:0 18px 35px rgba(37,99,235,.35);

}
/* ==============================
BADGES
============================== */

.tech{

background:#1E293B;

padding:12px 20px;

border-radius:12px;

display:inline-block;

margin:8px;

font-weight:600;

}

</style>
""", unsafe_allow_html=True)
st.sidebar.markdown("""
<h1 style="color:white;margin-bottom:5px;">
CyberSight AI
</h1>

<p style="color:#CBD5E1;font-size:16px;">
Enterprise Cyber Threat Analytics Platform
</p>
""", unsafe_allow_html=True)

page = st.sidebar.radio(

"Navigation",

[
"Home",
"Dashboard",
"Machine Learning",
"About"
]

)

st.sidebar.markdown("---")

st.sidebar.success("Version 1.0")
if page == "Home":
        st.markdown("""
        <div class="hero">

        <div class="hero-title">
        CyberSight AI
        </div>

        <div class="hero-subtitle">
        Enterprise Cyber Threat Analytics Platform
        </div>

        <div class="hero-tag">
        Detect • Analyze • Predict • Secure
        </div>

        </div>
        """, unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        col1,col2,col3,col4 = st.columns(4,gap="large")
        with col1:

            st.markdown("""

            <div class="metric-card">

            <div class="metric-title">

             Dataset

            </div>

            <div class="metric-value">

            <span style="white-space:nowrap;">UNSW-NB15</span>

            </div>

            <div class="metric-desc">

            257,673 Network Flows

            </div>

            </div>

            """,unsafe_allow_html=True)
        with col2:

            st.markdown("""

            <div class="metric-card">

            <div class="metric-title">

             Machine Learning

            </div>

            <div class="metric-value">

            Random Forest

            </div>

            <div class="metric-desc">

            Accuracy 82.66%

            </div>

            </div>

            """,unsafe_allow_html=True)
        with col3:

            st.markdown("""

            <div class="metric-card">

            <div class="metric-title">

             Analytics

            </div>

            <div class="metric-value">

            SQL + Power BI

            </div>

            <div class="metric-desc">

            Interactive Threat Dashboard

            </div>

            </div>

            """,unsafe_allow_html=True)
        with col4:

            st.markdown("""

            <div class="metric-card">

            <div class="metric-title">

             Prediction

            </div>

            <div class="metric-value">

            Real-Time

            </div>

            <div class="metric-desc">

            CSV Threat Detection

            </div>

            </div>

            """,unsafe_allow_html=True)
        st.markdown("<br><br>", unsafe_allow_html=True)

        st.markdown(
        """
        <div class="section-title">

         Project Overview

        </div>
        """,
        unsafe_allow_html=True
        )
        left,right = st.columns([1.3,1], gap="large")
        with left:

            st.markdown("""

        CyberSight AI is an **Enterprise Cyber Threat Analytics Platform**
        developed using the **UNSW-NB15 cybersecurity dataset**.

        The platform demonstrates a complete end-to-end data analytics and
        machine learning workflow for enterprise network security.

        ### Key Objectives

        - Detect malicious network traffic
        - Analyze attack patterns
        - Predict cyber attacks using Machine Learning
        - Visualize enterprise security insights
        - Support real-time threat intelligence

        """)
        with right:

           st.markdown("""
            <div class="metric-card">

            <div class="metric-title">

             Project Highlights

            </div>

            <div class="metric-desc">

            • 257,673 Network Records<br><br>

            • 9 Attack Categories<br><br>

            • SQL Analytics<br><br>

            • Random Forest Detection<br><br>

            • Power BI Dashboard<br><br>

            • Streamlit Deployment<br><br>

            • 82.66% Multiclass Detection Accuracy

            </div>

            </div>
            """, unsafe_allow_html=True)

        st.markdown(
        """
        <div class="section-title">

         Business Problem

        </div>
        """,
        unsafe_allow_html=True
        )
        st.markdown("""
        <div class="metric-card">

        <div class="metric-title">

         Business Challenge

        </div>

        <div class="metric-desc">

        Modern enterprise environments generate millions of network events every day.
        Manual investigation is slow, expensive, and often unable to detect threats in real time.

        CyberSight AI addresses this challenge by combining SQL analytics,
        machine learning, and interactive dashboards to automatically identify malicious traffic,
        support security analysts, and improve enterprise cyber defense.

        </div>

        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown("""
        <div class="section-title">

         Technology Stack

        </div>
        """, unsafe_allow_html=True)

        t1,t2,t3,t4 = st.columns(4, gap="large")
        with t1:

            st.markdown("""

            <div class="metric-card">

            <div class="metric-title">

             Data Engineering

            </div>

            <div class="metric-desc">

            • Python

            • Pandas

            • NumPy

            • SQLite

            </div>

            </div>

            """, unsafe_allow_html=True)
        with t2:

            st.markdown("""

            <div class="metric-card">

            <div class="metric-title">

             Machine Learning

            </div>

            <div class="metric-desc">

            • Scikit-Learn

            • Random Forest

            • XGBoost

            • Logistic Regression

            </div>

            </div>

            """, unsafe_allow_html=True)
        with t3:

            st.markdown("""

            <div class="metric-card">

            <div class="metric-title">

             Analytics

            </div>

            <div class="metric-desc">

            • SQL

            • Power BI

            • Plotly

            • Matplotlib

            </div>

            </div>

            """, unsafe_allow_html=True)
        with t4:

            st.markdown("""

            <div class="metric-card">

            <div class="metric-title">

             Deployment

            </div>

            <div class="metric-desc">

            • Streamlit

            • Joblib

            • Git

            • VS Code

            </div>

            </div>

            """, unsafe_allow_html=True)

        st.markdown(
        """
        <div class="section-title">

         Project Workflow

        </div>
        """,
        unsafe_allow_html=True
        )

        steps = [
        "Raw Dataset",
        "Data Cleaning",
        "Feature Engineering",
        "SQL Analytics",
        "Machine Learning",
        "Threat Visualization",
        "Prediction"
        ]

        cols = st.columns(7)

        for col, step in zip(cols, steps):

            with col:

                st.markdown(
                    f"""
                    <div style="
                        background:#1E293B;
                        height:120px;
                        border-radius:18px;
                        display:flex;
                        align-items:center;
                        justify-content:center;
                        text-align:center;
                        padding:15px;
                        font-weight:600;
                        color:white;
                        box-shadow:0 8px 20px rgba(0,0,0,.35);
                    ">
                        {step}
                    </div>
                    """,
                    unsafe_allow_html=True
                )
        st.markdown("""
        <div style="
        text-align:center;
        padding:35px;
        ">

        <h2 style="color:white;">
        Thank You for Visiting CyberSight AI
        </h2>

        <p style="color:#CBD5E1;font-size:18px;">
        An end-to-end Enterprise Cyber Threat Analytics Platform combining
        Data Engineering, SQL Analytics, Machine Learning, Power BI and Streamlit.
        </p>

        </div>
        """, unsafe_allow_html=True)

        st.markdown("<br><br><br>", unsafe_allow_html=True)

        st.markdown("""
        <div style="
        background:linear-gradient(135deg,#1F2937,#111827);
        padding:45px;
        border-radius:22px;
        border-top:4px solid #2563EB;
        border-bottom:4px solid #38BDF8;
        box-shadow:0 12px 35px rgba(0,0,0,.45);
        text-align:center;
        ">

        <h2 style="
        color:white;
        margin-bottom:8px;
        font-weight:700;
        ">

         CyberSight AI

        </h2>

        <p style="
        color:#CBD5E1;
        font-size:18px;
        margin-bottom:25px;
        ">

        Enterprise Cyber Threat Analytics Platform

        </p>

        <hr style="
        border:1px solid #334155;
        margin:20px 0;
        ">

        <p style="
        color:#94A3B8;
        font-size:15px;
        ">

        © 2026 Gurleen Kaur • CyberSight AI • All Rights Reserved

        </p>

        </div>
        """, unsafe_allow_html=True)

if page == "Dashboard":

    st.markdown("""
    <div class="hero">

    <div class="hero-title">
    Threat Intelligence Dashboard
    </div>

    <div class="hero-subtitle">
    Interactive Network Traffic Analytics
    </div>

    <div class="hero-tag">
    Explore attack patterns, protocols and suspicious traffic
    </div>

    </div>
    """, unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)

    with c1:
        attack_filter = st.multiselect(
            "Attack Category",
            sorted(df.attack_cat.unique()),
            default=["Normal","Generic","Exploits"]
        )

    with c2:
        proto_filter = st.multiselect(
            "Protocol",
            sorted(df.proto.unique()),
           default=["tcp","udp"]
        )

    with c3:
        service_filter = st.multiselect(
            "Service",
            sorted(df.service.unique()),
            default=["http","dns","smtp"]
        )
    filtered_df = df[
    (df.attack_cat.isin(attack_filter)) &
    (df.proto.isin(proto_filter)) &
    (df.service.isin(service_filter))
    ]
    total_connections = len(filtered_df)

    total_attacks = (filtered_df["label"] == 1).sum()

    normal_connections = (filtered_df["label"] == 0).sum()

    attack_rate = total_attacks / total_connections * 100 if total_connections else 0
    st.markdown("<br>", unsafe_allow_html=True)

    k1, k2, k3, k4 = st.columns(4, gap="large")

    with k1:
        st.markdown(
    f"""
    <div class="dashboard-card">
    <div class="metric-title">
    Total Connections
    </div>

    <div class="metric-value">
    {total_connections:,}
    </div>

    <div class="metric-desc">
    Network Records
    </div>
    </div>
    """,
            unsafe_allow_html=True
        )

    with k2:
        st.markdown(
    f"""
    <div class="dashboard-card">
    <div class="metric-title">
    Detected Attacks
    </div>
    <div class="metric-value">
    {total_attacks:,}
    </div>

    <div class="metric-desc">
     Malicious Traffic
    </div>
    </div>
        """, 
                unsafe_allow_html=True
            )

    with k3:
        st.markdown(
    f"""
    <div class="dashboard-card">
    <div class="metric-title">
    Normal Traffic
    </div>
    <div class="metric-value">
    {normal_connections:,}
    </div>

    <div class="metric-desc">
    Safe Connections
    </div>
    </div>
        """, 
                unsafe_allow_html=True
            )

    with k4:
        st.markdown(
    f"""
    <div class="dashboard-card">
    <div class="metric-title">
    Attack Rate
    </div>
    <div class="metric-value">
    {attack_rate:.2f}%
    </div>

    <div class="metric-desc">
    Threat Percentage
    </div>
    </div>
        """, 
                unsafe_allow_html=True
            )
    attack_counts = (
    filtered_df["attack_cat"]
    .value_counts()
    .reset_index()
    )

    attack_counts.columns = ["attack_cat", "count"]
    st.markdown(
    """
    <div class="section-title">
    Network Traffic Overview
    </div>
    """,
    unsafe_allow_html=True
    )

    fig1 = px.bar(
        attack_counts,
        x="count",
        y="attack_cat",
        orientation="h",
        color="count",
        color_continuous_scale="Blues"
    )

    fig1.update_layout(

        paper_bgcolor="#1E293B",

        plot_bgcolor="#1E293B",

        font_color="white",

        title="Attack Category Distribution",

        height=450,

        coloraxis_showscale=False

    )

    protocol_counts = (
    filtered_df["proto"]
    .value_counts()
    .head(5)
    .reset_index()
    )

    protocol_counts.columns = ["proto", "count"]

    fig2 = px.pie(

        protocol_counts,

        names="proto",

        values="count",

        hole=0.6

    )

    fig2.update_layout(

        paper_bgcolor="#1E293B",

        plot_bgcolor="#1E293B",

        font_color="white",

        title="Protocol Distribution",

        height=450
    )
    left, right = st.columns(2)
    
    with left:
            st.plotly_chart(
            fig1,
            use_container_width=True,
            config={"displayModeBar":False}
        )
    
    with right:
            st.plotly_chart(
            fig2,
            use_container_width=True,
            config={"displayModeBar":False}
        )
    st.markdown("<br><br>", unsafe_allow_html=True)
    service_counts = (
    filtered_df["service"]
    .value_counts()
    .head(10)
    .reset_index()
    )

    service_counts.columns = ["service","count"]

    fig3 = px.bar(
        service_counts,
        x="service",
        y="count",
        color="count",
        color_continuous_scale="Blues"
    )

    fig3.update_layout(
        title="Top Services",
        paper_bgcolor="#1E293B",
        plot_bgcolor="#1E293B",
        font_color="white",
        coloraxis_showscale=False,
        height=430
    )
    state_counts = (
    filtered_df["state"]
    .value_counts()
    .reset_index()
    )

    state_counts.columns = ["state","count"]

    fig4 = px.bar(
        state_counts,
        x="state",
        y="count",
        color="count",
        color_continuous_scale="Teal"
    )

    fig4.update_layout(
        title="Connection States",
        paper_bgcolor="#1E293B",
        plot_bgcolor="#1E293B",
        font_color="white",
        coloraxis_showscale=False,
        height=430
    )
    left,right = st.columns(2)

    with left:
        st.plotly_chart(fig3,use_container_width=True)

    with right:
        st.plotly_chart(fig4,use_container_width=True)
    protocol_attack = (
    filtered_df.groupby("proto")["label"]
    .sum()
    .sort_values(ascending=False)
    .reset_index()
    )

    fig5 = px.bar(
        protocol_attack,
        x="proto",
        y="label",
        color="label",
        color_continuous_scale="Reds"
    )

    fig5.update_layout(
        title="Detected Attacks by Protocol",
        paper_bgcolor="#1E293B",
        plot_bgcolor="#1E293B",
        font_color="white",
        coloraxis_showscale=False,
        height=430
    )
    traffic = (
    filtered_df.groupby("attack_cat")["total_bytes"]
    .mean()
    .sort_values(ascending=False)
    .reset_index()
    )

    fig6 = px.bar(
        traffic,
        x="attack_cat",
        y="total_bytes",
        color="total_bytes",
        color_continuous_scale="Oranges"
    )

    fig6.update_layout(
        title="Average Bytes by Attack Category",
        paper_bgcolor="#1E293B",
        plot_bgcolor="#1E293B",
        font_color="white",
        coloraxis_showscale=False,
        height=430
    )
    left,right = st.columns(2)

    with left:
        st.plotly_chart(fig5,use_container_width=True)

    with right:
        st.plotly_chart(fig6,use_container_width=True)
    st.markdown(
    """
    <div class="section-title">
    Top Suspicious Network Connections
    </div>
    """,
    unsafe_allow_html=True
    )

    top_connections = (
        filtered_df
        .sort_values("total_bytes",ascending=False)
        [["attack_cat","proto","service","state","total_bytes","total_packets"]]
        .head(20)
    )

    st.dataframe(
        top_connections,
        use_container_width=True,
        hide_index=True
    )

if page == "Machine Learning":
    st.markdown(
    """
    <div class="hero">

    <div class="hero-title">
    Machine Learning Threat Detection
    </div>

    <div class="hero-subtitle">
    Random Forest Intrusion Detection Engine
    </div>

    <div class="hero-tag">
    Upload network traffic • Detect malicious activity • Predict cyber threats in real time
    </div>

    </div>
    """,
    unsafe_allow_html=True
    )
    st.markdown(
    """
    <div class="section-title">
    Model Performance
    </div>
    """,
    unsafe_allow_html=True
    )

    m1, m2, m3, m4 = st.columns(4, gap="large")

    with m1:
        st.markdown(
    """
    <div class="dashboard-card">

    <div class="metric-title">
    Model Accuracy
    </div>

    <div class="metric-value">
    82.66%
    </div>

    <div class="metric-desc">
    Overall Prediction Accuracy
    </div>

    </div>
    """,
    unsafe_allow_html=True
    )

    with m2:
        st.markdown(
    """
    <div class="dashboard-card">

    <div class="metric-title">
    Precision
    </div>

    <div class="metric-value">
    82.70%
    </div>

    <div class="metric-desc">
    Positive Prediction Accuracy
    </div>

    </div>
    """,
    unsafe_allow_html=True
    )

    with m3:
        st.markdown(
    """
    <div class="dashboard-card">

    <div class="metric-title">
    Recall
    </div>

    <div class="metric-value">
    82.66%
    </div>

    <div class="metric-desc">
    Threat Detection Rate
    </div>

    </div>
    """,
    unsafe_allow_html=True
    )

    with m4:
        st.markdown(
    """
    <div class="dashboard-card">

    <div class="metric-title">
    Weighted F1 Score
    </div>

    <div class="metric-value">
    81.72%
    </div>

    <div class="metric-desc">
    Balanced Model Performance
    </div>

    </div>
    """,
    unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(
    """
    <div class="section-title">
    Model Information
    </div>
    """,
    unsafe_allow_html=True
    )

    left, right = st.columns([1.4, 1], gap="large")

    with left:

        st.markdown(
    """
    <div class="metric-card">

    <div class="metric-title">
    Model Overview
    </div>

    <div class="metric-desc">

    <b>Algorithm</b><br>
    Tuned Random Forest Classifier<br><br>

    <b>Training Dataset</b><br>
    UNSW-NB15 Network Intrusion Dataset<br><br>

    <b>Training Samples</b><br>
    257,673 Network Records<br><br>

    <b>Prediction Classes</b><br>
    10 Intrusion Categories<br>
    Analysis, Backdoor, DoS,<br>
    Exploits, Fuzzers,<br>
    Generic, Normal,<br>
    Reconnaissance,<br>
    Shellcode, Worms<br><br>

    <b>Framework</b><br>
    Scikit-Learn

    </div>

    </div>
    """,
    unsafe_allow_html=True
    )

    with right:

        st.markdown(
    """
    <div class="metric-card">

    <div class="metric-title">
    Deployment Status
    </div>

    <div class="metric-desc">

     <b>Model Status</b><br>
    Ready for Prediction<br><br>

     <b>Prediction Engine</b><br>
    Loaded Successfully<br><br>

     <b>Input Format</b><br>
    CSV File<br><br>

     <b>Output</b><br>
    Threat Classification<br><br>

     <b>Deployment</b><br>
    Streamlit Web Application

    </div>

    </div>
    """,
    unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(
    """
    <div class="section-title">
    Feature Importance Analysis
    </div>
    """,
    unsafe_allow_html=True
    )

    # Load model and feature names
    model = joblib.load(MODEL_PATH)
    feature_names = joblib.load(FEATURES_PATH)
    FEATURE_IMPORTANCE_IMAGE = IMAGES / "feature_importance.png"

    MODEL_COMPARISON_IMAGE = IMAGES / "model_comparison.png"

    RF_CONFUSION_IMAGE = IMAGES / "RFTunedConfusionMatrix.png"

    st.image(
    FEATURE_IMPORTANCE_IMAGE,
    use_container_width=True
    )

    st.image(
        MODEL_COMPARISON_IMAGE,
        use_container_width=True
    )

    st.image(
        RF_CONFUSION_IMAGE,
        use_container_width=True
    )
    st.markdown("<br>", unsafe_allow_html=True)      
    st.markdown(
    """
    <div class="section-title">
    Real-Time Threat Detection
    </div>
    """,
    unsafe_allow_html=True
    )
    uploaded_file = st.file_uploader(
    "Upload Network Traffic CSV",
    type=["csv"]
    )
    if uploaded_file is not None:

        input_df = pd.read_csv(uploaded_file)

        st.success("CSV uploaded successfully.")

        st.markdown(
        """
        <div class="metric-title">
        Uploaded Dataset Preview
        </div>
        """,
        unsafe_allow_html=True
        )

        st.dataframe(
            input_df.head(),
            use_container_width=True,
            hide_index=True
        )
        predict = st.button(
        "Run Threat Detection",
        use_container_width=True
        )
        if predict:

            model = joblib.load(MODEL_PATH)
            label_encoder = joblib.load(LABEL_ENCODER_PATH)

            feature_names = joblib.load(FEATURES_PATH)

            prediction_data = input_df[feature_names]

            predictions = model.predict(prediction_data)

            predictions = label_encoder.inverse_transform(predictions)

            probabilities = model.predict_proba(prediction_data)

            confidence = probabilities.max(axis=1)

            result_df = input_df.copy()

            result_df["Prediction"] = predictions

            result_df["Confidence (%)"] = (
                confidence*100
            ).round(2)

           
            st.success("Threat detection completed successfully.")

            st.dataframe(
            result_df[
                [
                    "Prediction",
                    "Confidence (%)"
                ]
            ].head(20),
            use_container_width=True,
            hide_index=True
            )
            st.markdown(
            """
            <div class="section-title">
            Prediction Summary
            </div>
            """,
            unsafe_allow_html=True
            )

            col1,col2,col3 = st.columns(3)

            with col1:
                st.metric(
                    "Total Records",
                    len(result_df)
                )

            with col2:
                st.metric(
                    "Unique Attack Types",
                    result_df["Prediction"].nunique()
                )

            with col3:
                st.metric(
                    "Average Confidence",
                    f"{result_df['Confidence (%)'].mean():.2f}%"
                )
            summary = (
            result_df["Prediction"]
            .value_counts()
            .reset_index()
            )

            summary.columns = ["Attack Category","Count"]

            fig = px.bar(

                summary,

                x="Attack Category",

                y="Count",

                color="Count",

                color_continuous_scale="Reds"

            )

            fig.update_layout(

                paper_bgcolor="#1E293B",

                plot_bgcolor="#1E293B",

                font_color="white",

                coloraxis_showscale=False,

                height=450

            )

            st.plotly_chart(
                fig,
                use_container_width=True
            ) 
if page == "About":

    st.markdown("""
    <div class="hero">

    <div class="hero-title">
    About CyberSight AI
    </div>

    <div class="hero-subtitle">
    Enterprise Cyber Threat Analytics Platform
    </div>

    <div class="hero-tag">
    SQL • Machine Learning • Power BI • Streamlit
    </div>

    </div>
    """,
    unsafe_allow_html=True
    )

    left, right = st.columns([2,1], gap="large")
    with left:

        st.markdown("""
    <div class="metric-card">

    <div class="metric-title">
    Project Overview
    </div>

    <div class="metric-desc">

    CyberSight AI is an end-to-end cybersecurity analytics platform developed using the UNSW-NB15 dataset.

    <br><br>

    The project integrates:

    • Data Engineering<br>
    • SQL Analytics<br>
    • Machine Learning<br>
    • Interactive Power BI Dashboards<br>
    • Streamlit Deployment

    <br><br>

    The platform enables automated detection and analysis of malicious network traffic in enterprise environments.

    </div>

    </div>
    """, unsafe_allow_html=True)  
    with right:

        st.markdown("""
    <div class="metric-card">

    <div class="metric-title">
    Project Statistics
    </div>

    <div class="metric-desc">

    <b>Dataset</b><br>
    257,673 Network Flows

    <br><br>

    <b>Features</b><br>
    198

    <br><br>

    <b>Attack Categories</b><br>
    10

    <br><br>

    <b>Final Model</b><br>
    Tuned Random Forest

    <br><br>

    <b>Weighted F1</b><br>
    81.72%

    </div>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="section-title">
    Technology Stack
    </div>
    """,
    unsafe_allow_html=True
    )

    c1, c2, c3, c4, c5 = st.columns(5)

    with c1:
        st.info(" Python")

    with c2:
        st.info(" SQL")

    with c3:
        st.info(" Scikit-Learn")

    with c4:
        st.info(" Power BI")

    with c5:
        st.info(" Streamlit")
    st.markdown("""
    <div class="section-title">
    Project Features
    </div>
    """,
    unsafe_allow_html=True
    )

    left, right = st.columns(2)

    with left:
        st.success("Interactive Threat Dashboard")
        st.success("Multiclass Intrusion Detection")
        st.success("SQL Analytics")

    with right:
        st.success("Feature Importance Analysis")
        st.success("Model Comparison")
        st.success("Real-Time CSV Prediction")
    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div class="section-title">
    Author
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="metric-card">

    <div class="metric-title">
    Developer
    </div>

    <div class="metric-desc">

    <b>Name</b><br>
    Gurleen Kaur<br><br>

    <b>Degree</b><br>
    B.Tech Electronics & Computer Engineering<br><br>

    <b>Project</b><br>
    CyberSight AI - Enterprise Cyber Threat Analytics Platform<br><br>

    <b>Technologies</b><br>
    Python, SQL, Machine Learning, Power BI, Streamlit

    </div>

    </div>
    """, unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div class="section-title">
    Connect
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("""
        <div class="dashboard-card">
        <div class="metric-title">📧 Email</div>
        <div class="metric-desc">
        <a href="mailto:gurleenkaursandhu2210@gmail.com">
        gurleenkaursandhu2210@gmail.com
        </a>
        </div>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="dashboard-card">
        <div class="metric-title"> LinkedIn</div>
        <div class="metric-desc">
        <a href="https://www.linkedin.com/in/gurleen-kaur-sandhu/" target="_blank">
        Visit Profile
        </a>
        </div>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="dashboard-card">
        <div class="metric-title">💻 GitHub</div>
        <div class="metric-desc">
        <a href="https://github.com/GurleenKaur00" target="_blank">
        View Repository
        </a>
        </div>
        </div>
        """, unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)

    st.markdown("""
    <div style="
    background:#1E293B;
    padding:25px;
    border-radius:18px;
    text-align:center;
    ">

    <h3 style="color:white;">
    CyberSight AI
    </h3>

    <p style="color:#CBD5E1;">
    Enterprise Cyber Threat Analytics Platform
    </p>

    <p style="color:#94A3B8;">
    Developed using Python, Machine Learning, SQL, Power BI and Streamlit.
    </p>

    </div>
    """,
    unsafe_allow_html=True
    )

