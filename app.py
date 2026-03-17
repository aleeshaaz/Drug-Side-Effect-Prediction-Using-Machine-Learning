import streamlit as st
import pandas as pd
import os
import base64
import re

st.set_page_config(
    page_title="Drug Side Effect Prediction System",
    layout="centered"
)

# -------------------------------------------------
# Hide Streamlit UI
# -------------------------------------------------
st.markdown("""
<style>
header {visibility: hidden;}
[data-testid="stToolbar"] {display:none;}
[data-testid="stDecoration"] {display:none;}
#MainMenu {visibility:hidden;}
.block-container {padding-top:0rem;}
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# Background
# -------------------------------------------------
def set_background(image_path):

    if os.path.exists(image_path):

        with open(image_path,"rb") as img:
            encoded=base64.b64encode(img.read()).decode()

        st.markdown(
        f"""
        <style>
        .stApp {{
        background-image:url("data:image/jpg;base64,{encoded}");
        background-size:cover;
        background-position:center;
        background-repeat:no-repeat;
        background-attachment:fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
        )

set_background("assets/drg_bj.jpg")

# -------------------------------------------------
# Paths
# -------------------------------------------------
BASE_DIR=os.path.dirname(os.path.abspath(__file__))

DATA_PATH=os.path.join(BASE_DIR,"data","drug_side_effect_dataset_5000_enhanced.csv")
USER_PATH=os.path.join(BASE_DIR,"data","users.csv")

# -------------------------------------------------
# Create users file
# -------------------------------------------------
if not os.path.exists(USER_PATH):

    users_df=pd.DataFrame(columns=[
        "first_name","last_name","username","email","mobile","password"
    ])

    users_df.to_csv(USER_PATH,index=False)

# -------------------------------------------------
# Load Dataset
# -------------------------------------------------
df=pd.read_csv(DATA_PATH)
df.columns=df.columns.str.strip()

df["Drug"]=df["Drug"].astype(str).str.strip()

drug_list=sorted(df["Drug"].unique())

# Extract symptoms
symptom_set=set()

for s in df["Symptoms"]:
    for item in str(s).split(","):
        symptom_set.add(item.strip())

symptom_list=sorted(symptom_set)

# -------------------------------------------------
# Session State
# -------------------------------------------------
if "page" not in st.session_state:
    st.session_state.page="home"

if "user" not in st.session_state:
    st.session_state.user=""

if "logged_in" not in st.session_state:
    st.session_state.logged_in=False


# =================================================
# NAVIGATION CONTROL
# =================================================

# HOME PAGE NAVIGATION
if st.session_state.page == "home":

    col1,col2,col3 = st.columns(3)

    with col1:
        if st.button("🏠 Home"):
            st.session_state.page="home"

    with col2:
        if st.button("🔑 Login"):
            st.session_state.page="login"

    with col3:
        if st.button("ℹ️ About"):
            st.session_state.page="about"


# LOGIN / REGISTER / ABOUT NAVIGATION
elif st.session_state.page in ["login","register","about"]:

    col1,col2,col3 = st.columns(3)

    with col1:
        if st.button("🏠 Home"):
            st.session_state.page="home"

    with col2:
        if st.button("🔑 Login"):
            st.session_state.page="login"

    with col3:
        if st.button("ℹ️ About"):
            st.session_state.page="about"


# WELCOME PAGE NAVIGATION
elif st.session_state.page == "welcome":

    col1,col2,col3 = st.columns([4,1,4])

    with col2:
        if st.button("🏠 Home"):
            st.session_state.page="home"


# Prediction / Results / Dashboard → NO navigation


# =================================================
# HOME PAGE
# =================================================
if st.session_state.page=="home":

    st.markdown('<div class="center-box">', unsafe_allow_html=True)

    st.title("🧬 Drug Side Effect Prediction System")

    st.markdown("""
    Welcome to the **Drug Side Effect Prediction System**, an AI-powered healthcare application that helps analyze the possible side effects of medicines using **patient symptoms and blood test results**.

    Medicines are essential for treating diseases, but sometimes they may cause **unexpected adverse reactions**.  
    This system helps in predicting possible **drug side effects, severity levels, and safety indications** using healthcare data analysis.
    """)

    st.markdown("---")

    st.subheader("🔍 Key Features of the System")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        🧬 **Drug Side Effect Prediction**

        Predicts potential side effects based on selected drug and patient symptoms.
        """)

        st.markdown("""
        🧪 **Blood Test Analysis**

        Evaluates blood test parameters like WBC, ALT, AST, Creatinine and more.
        """)

        st.markdown("""
        ⚠ **Severity Detection**

        Determines the severity level of possible adverse drug reactions.
        """)

    with col2:
        st.markdown("""
        💊 **Drug Safety Indication**

        Provides indication whether the selected drug is safe or risky for the patient.
        """)

        st.markdown("""
        📊 **Analytics Dashboard**

        Displays visual charts for blood test values and drug safety statistics.
        """)

        st.markdown("""
        🏥 **Healthcare Support Tool**

        Helps researchers and healthcare professionals analyze drug safety patterns.
        """)


    st.success("➡️ Login or Register to start predicting drug side effects.")

    st.markdown('</div>', unsafe_allow_html=True)
# =================================================
# ABOUT PAGE
# =================================================
elif st.session_state.page=="about":

    st.title("ℹ About the Project")

    st.markdown("""
    The **Drug Side Effect Prediction System** is a healthcare data analysis application
    designed to identify potential drug reactions using patient symptoms and blood test values.

    The system aims to support better understanding of drug safety by analyzing medical data
    and predicting possible side effects associated with medications.
    """)

    st.markdown("---")

    st.subheader("🎯 Project Objectives")

    st.markdown("""
    - Analyze possible **side effects of drugs**
    - Evaluate **patient symptoms and blood test results**
    - Determine the **severity level of reactions**
    - Provide **drug safety indication**
    - Visualize medical data using **analytics dashboards**
    """)

    st.markdown("---")

    st.subheader("🔄 System Workflow")

    st.markdown("""
    ```text
    User Login
        │
        ▼
    Drug Selection
        │
        ▼
    Symptoms Input
        │
        ▼
    Blood Test Parameters
        │
        ▼
    Dataset Analysis
        │
        ▼
    Side Effect Prediction
        │
        ▼
    Severity Detection
        │
        ▼
    Drug Safety Indication
        │
        ▼
    Analytics Dashboard
    ```
    """)

    st.markdown("---")

    st.subheader("🧪 Technologies Used")

    st.markdown("""
    - **Python**
    - **Streamlit** – Web application interface
    - **Pandas** – Data processing and dataset handling
    - **Machine Learning concepts**
    - **Data Visualization**
    """)

    st.markdown("---")

    st.subheader("🏥 Application Scope")

    st.markdown("""
    This system can be used as a **healthcare decision support tool** to analyze potential
    drug reactions. It demonstrates how medical data can be utilized to predict possible
    side effects and assist in drug safety monitoring.
    """)
# =================================================
# REGISTER PAGE
# =================================================
elif st.session_state.page=="register":

    st.title("Register User")

    first_name = st.text_input("First Name")
    last_name = st.text_input("Last Name")
    username = st.text_input("Username")

    email = st.text_input("Email ID")
    email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if email and not re.match(email_pattern,email):
        st.warning("Enter valid email format")

    mobile = st.text_input("Mobile Number")
    if mobile:
        if not mobile.isdigit():
            st.warning("Mobile must contain digits only")
        elif len(mobile)!=10:
            st.warning("Mobile must be 10 digits")

    password = st.text_input("Password",type="password")
    password_pattern=r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&]).{8,}$'
    if password and not re.match(password_pattern,password):
        st.warning("Password must contain uppercase, lowercase, number and special character")

    confirm_password = st.text_input("Retype Password",type="password")
    if confirm_password and password!=confirm_password:
        st.warning("Passwords do not match")

    if st.button("Create Account"):

        users=pd.read_csv(USER_PATH)

        if username in users["username"].values:
            st.error("Username already exists")

        elif password!=confirm_password:
            st.error("Passwords do not match")

        else:

            new_user=pd.DataFrame(
            [[first_name,last_name,username,email,mobile,password]],
            columns=["first_name","last_name","username","email","mobile","password"]
            )

            users=pd.concat([users,new_user],ignore_index=True)
            users.to_csv(USER_PATH,index=False)

            st.success("Registration Successful")

# =================================================
# LOGIN PAGE
# =================================================
elif st.session_state.page=="login":

    st.title("User Login")

    username=st.text_input("Username")
    password=st.text_input("Password",type="password")

    col1,col2=st.columns(2)

    with col1:

        if st.button("Login"):

            users=pd.read_csv(USER_PATH)

            valid=users[(users["username"]==username) & (users["password"]==password)]

            if len(valid)>0:

                st.session_state.logged_in=True
                st.session_state.user=username
                st.session_state.page="welcome"
                st.rerun()

            else:
                st.error("Invalid username or password")

    with col2:

        if st.button("Register"):
            st.session_state.page="register"
            st.rerun()

# =================================================
# WELCOME PAGE
# =================================================
elif st.session_state.page=="welcome":

    st.markdown('<div class="center-box">', unsafe_allow_html=True)

    st.title(f"Welcome {st.session_state.user} 👋")

    st.write("""
    You have successfully logged into the **Drug Side Effect Prediction System**.

    This platform helps analyze potential drug reactions by evaluating
    patient symptoms and blood test parameters.
    """)

    st.markdown("---")

    st.subheader("🔍 What You Can Do Here")

    st.markdown("""
    Using this system, you can:

    - Select a **drug name**
    - Enter **patient symptoms**
    - Provide **blood test values**
    - Predict possible **drug side effects**
    - View **severity level and safety indication**
    - Analyze results using the **analytics dashboard**
    """)


    st.markdown("---")

    st.info("Click the button below to start predicting drug side effects.")

    if st.button("🚀 Go to Prediction"):
        st.session_state.page="input"
        st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)
# =================================================
# PREDICTION PAGE
# =================================================
elif st.session_state.page=="input" and st.session_state.logged_in:

    col1,col2=st.columns([8,2])

    with col1:
        st.title("Drug Side Effect Prediction")

    with col2:
        if st.button("Logout"):
            st.session_state.logged_in=False
            st.session_state.page="home"
            st.rerun()

    if st.button("⬅ Back"):
        st.session_state.page="welcome"
        st.rerun()

    drug=st.selectbox("Drug Name",drug_list)

    symptoms_dropdown=st.multiselect("Select Symptoms",symptom_list)

    symptoms_custom=st.text_input("Or type Symptoms (comma separated)")

    symptoms=symptoms_dropdown.copy()

    if symptoms_custom.strip():
        symptoms.extend([s.strip() for s in symptoms_custom.split(",")])

    age=st.number_input("Age",0,120,30)

    st.subheader("Blood Test Results")

    wbc=st.number_input("WBC (Normal: 4000–11000 cells/µL)",0.0,50000.0,7000.0)
    eos=st.number_input("Eosinophils (Normal: 0–6%)",0.0,30.0,2.0)
    creat=st.number_input("Creatinine (Normal: 0.6–1.3 mg/dL)",0.0,15.0,1.0)
    alt=st.number_input("ALT (Normal: 7–56 U/L)",0,1000,30)
    ast=st.number_input("AST (Normal: 10–40 U/L)",0,1000,30)
    hb=st.number_input("Hemoglobin (Normal: 12–17 g/dL)",0.0,20.0,13.0)
    platelets=st.number_input("Platelets (Normal: 150000–450000 /µL)",0,1000000,250000)
    if st.button("Predict"):

        filtered=df[df["Drug"].str.lower()==drug.lower()]

        best_match=filtered.iloc[0]

        side_effects=best_match["SideEffects"]
        severity=best_match["Severity"]
        safety=best_match["Drug_Safety_Indication"]

        st.session_state.results={
        "drug":drug,
        "side_effects":side_effects,
        "severity":severity,
        "safety":safety,
        "blood_values":[wbc,eos,creat,alt,ast,hb,platelets]
        }

        st.session_state.page="results"
        st.rerun()

# =================================================
# RESULTS PAGE
# =================================================
elif st.session_state.page=="results":

    st.title("Prediction Results")

    r=st.session_state.results

    st.write("Drug Selected:",r["drug"])

    st.subheader("Side Effects")
    st.write(r["side_effects"])

    st.subheader("Severity Level")
    st.write(r["severity"])

    st.subheader("Drug Safety Indication")
    st.write(r["safety"])

    if st.button("View Analytics Dashboard"):
        st.session_state.page="dashboard"
        st.rerun()

    if st.button("Back to Prediction"):
        st.session_state.page="input"
        st.rerun()

# =================================================
# DASHBOARD PAGE
# =================================================
elif st.session_state.page=="dashboard":

    st.title("Analytics Dashboard")

    r=st.session_state.results

    blood_df=pd.DataFrame({
    "Test":["WBC","Eosinophil","Creatinine","ALT","AST","Hemoglobin","Platelets"],
    "Value":r["blood_values"]
    })

    st.subheader("Patient Blood Test Values")
    st.bar_chart(blood_df.set_index("Test"))

    st.subheader("Severity Distribution")
    st.bar_chart(df["Severity"].value_counts())

    st.subheader("Drug Safety Distribution")
    st.bar_chart(df["Drug_Safety_Indication"].value_counts())

    if st.button("Back"):
        st.session_state.page="results"
        st.rerun()


        
