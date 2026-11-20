import os, pickle
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Placement Predictor", page_icon="🎓", layout="wide")
st.markdown("""
<style>
.stApp{background:linear-gradient(135deg,#f4f7fc,#eaf1ff)}
.block-container{max-width:1180px;padding-top:2rem}
.hero{background:linear-gradient(110deg,#14213d,#28558d);padding:28px 30px;border-radius:20px;color:white;margin-bottom:22px}
.hero h1{color:white;margin:0}.hero p{color:#e6efff;margin:8px 0 0}
div[data-testid="stMetric"]{background:white;padding:16px;border-radius:14px;border:1px solid #e3eaf5}
</style>
""", unsafe_allow_html=True)

@st.cache_resource
def get_model():
    with open("placement_model.pkl","rb") as f: return pickle.load(f)

st.markdown('<div class="hero"><h1>🎓 Student Placement Predictor</h1><p>Machine Learning project powered by Logistic Regression</p></div>', unsafe_allow_html=True)
model = get_model()
st.sidebar.title("Project Overview")
st.sidebar.write("Predicts a likely placement outcome from academic and skill-related details.")
st.sidebar.info("Algorithm: Logistic Regression\n\nOutput: Placed / Not Placed")

t1,t2,t3 = st.tabs(["🔮 Predict Placement","📊 Dataset Insights","ℹ️ About"])
with t1:
    a,b = st.columns([1,1],gap="large")
    with a:
        st.subheader("Enter Student Details")
        with st.form("predict"):
            c1,c2=st.columns(2)
            with c1:
                cgpa=st.slider("CGPA",4.0,10.0,7.5,.1)
                aptitude=st.slider("Aptitude Score",0,100,70)
                technical=st.slider("Technical Skills",0,100,72)
            with c2:
                communication=st.slider("Communication Skills",0,100,68)
                internships=st.selectbox("Internships",[0,1,2,3])
                projects=st.selectbox("Projects",list(range(7)))
            go=st.form_submit_button("🚀 Predict Placement",use_container_width=True)
    with b:
        st.subheader("Prediction Result")
        if go:
            row=pd.DataFrame([{"cgpa":cgpa,"aptitude_score":aptitude,"technical_score":technical,
                "communication_score":communication,"internships":internships,"projects":projects}])
            probability=float(model.predict_proba(row)[0][1])
            label=int(model.predict(row)[0])
            st.metric("Estimated placement probability",f"{probability*100:.1f}%")
            st.progress(probability)
            if label: st.success("Prediction: LIKELY TO BE PLACED")
            else: st.warning("Prediction: LIKELY TO BE NOT PLACED")
            st.caption("Educational estimate only; not a guarantee or actual hiring decision.")
        else:
            st.info("Enter student details and click Predict Placement.")
with t2:
    data=pd.read_csv("dataset.csv")
    x,y,z=st.columns(3)
    x.metric("Total records",len(data))
    y.metric("Placed examples",int(data.placed.sum()))
    z.metric("Not placed",int((data.placed==0).sum()))
    st.bar_chart(data.placed.value_counts().rename(index={0:"Not Placed",1:"Placed"}))
    st.dataframe(data.head(10),use_container_width=True)
with t3:
    st.subheader("Project Details")
    st.markdown("""
**Objective:** Estimate a student's placement outcome using machine learning.

**Algorithm:** Logistic Regression — a supervised binary classification algorithm.

**Input features:** CGPA, aptitude score, technical skills, communication skills, internships and projects.

**Workflow:** Dataset → Train/test split → Feature scaling → Logistic Regression → Prediction.

**Output:** Placed (1) or Not Placed (0).
""")
    st.warning("The included dataset is synthetic demonstration data, not real college or company placement records. The model's test accuracy must not be presented as validated real-world performance.")
