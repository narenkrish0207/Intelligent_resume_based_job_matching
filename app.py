import streamlit as st
import boto3
import requests
from datetime import datetime

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Career Intelligence Platform",
    page_icon="🧠",
    layout="wide"
)

# ---------------- PREMIUM CSS ----------------
st.markdown("""
<style>

/* Base */
html, body, [class*="css"] {
    background-color: #0b1020;
    color: #e5e7eb;
    font-family: 'Inter', sans-serif;
}

/* Hide Streamlit chrome */
header, footer {visibility: hidden;}

/* Hero */
.hero {
    padding: 40px 10px 25px 10px;
}
.hero h1 {
    font-size: 44px;
    font-weight: 800;
    background: linear-gradient(90deg,#60a5fa,#a78bfa,#22d3ee);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.hero p {
    font-size: 18px;
    color: #9ca3af;
}

/* Glass cards */
.glass {
    background: rgba(255,255,255,0.06);
    backdrop-filter: blur(14px);
    border-radius: 18px;
    padding: 26px;
    border: 1px solid rgba(255,255,255,0.12);
    margin-bottom: 25px;
}

/* Buttons */
.stButton>button {
    background: linear-gradient(90deg,#6366f1,#8b5cf6);
    color: white;
    border-radius: 14px;
    padding: 12px 26px;
    border: none;
    font-size: 16px;
    font-weight: 600;
}

/* Job card */
.job-card {
    background: rgba(255,255,255,0.05);
    border-radius: 16px;
    padding: 22px;
    border: 1px solid rgba(255,255,255,0.1);
    margin-bottom: 18px;
}
.company {
    font-size: 21px;
    font-weight: 700;
}
.role {
    font-size: 17px;
    color: #c7d2fe;
}

/* Skill pills */
.skill {
    display: inline-block;
    padding: 6px 14px;
    border-radius: 20px;
    font-size: 13px;
    margin: 4px;
    background: rgba(96,165,250,0.18);
    color: #93c5fd;
}
.skill-miss {
    background: rgba(248,113,113,0.18);
    color: #fca5a5;
}

/* Course card */
.course {
    background: rgba(255,255,255,0.05);
    border-radius: 14px;
    padding: 18px;
    border: 1px solid rgba(255,255,255,0.1);
}

</style>
""", unsafe_allow_html=True)

# ---------------- AWS CONFIG ----------------
BUCKET = "resume-upload-project0207"
REGION = "ap-south-1"
s3 = boto3.client("s3", region_name=REGION)

# ---------------- ADZUNA CONFIG ----------------
ADZUNA_APP_ID = "28b58f49"
ADZUNA_APP_KEY = "eb9df74952394c8563fd51b71246d4a7"
COUNTRY = "in"

# ---------------- HERO ----------------
st.markdown("""
<div class="hero">
  <h1>AI Career Intelligence Platform</h1>
  <p>Live job matching • Skill gap analysis • Learning recommendations</p>
</div>
""", unsafe_allow_html=True)

# ---------------- UPLOAD SECTION ----------------
st.markdown('<div class="glass">', unsafe_allow_html=True)
st.subheader("📄 Upload Resume")

user_id = st.text_input("Candidate ID")
resume = st.file_uploader("Upload Resume (PDF / DOCX)", type=["pdf","docx"])

uploaded = False
if st.button("Analyze Resume"):
    if not user_id or not resume:
        st.warning("Please enter Candidate ID and upload resume")
    else:
        ts = datetime.utcnow().strftime("%Y%m%d%H%M%S")
        key = f"resumes/{user_id}/{ts}_{resume.name}"
        s3.upload_fileobj(resume, BUCKET, key)
        st.success("Resume uploaded & analyzed successfully")
        uploaded = True

st.markdown('</div>', unsafe_allow_html=True)

# ---------------- RESUME SKILLS (SIMULATED) ----------------
resume_skills = {"python","sql","aws","machine learning","data analysis"}

# ---------------- JOB API FUNCTIONS ----------------
def fetch_jobs(skill):
    url = f"https://api.adzuna.com/v1/api/jobs/{COUNTRY}/search/1"
    params = {
        "app_id": ADZUNA_APP_ID,
        "app_key": ADZUNA_APP_KEY,
        "what": skill,
        "results_per_page": 8
    }
    return requests.get(url, params=params).json().get("results", [])

def match_job(text):
    text = text.lower()
    matched = [s for s in resume_skills if s in text]
    score = int((len(matched)/len(resume_skills))*100)
    missing = list(resume_skills - set(matched))
    return score, matched, missing

# ---------------- DASHBOARD ----------------
if uploaded:

    col1, col2 = st.columns([2,1])

    # -------- JOB MATCHES --------
    with col1:
        st.subheader("🎯 Live Job Matches")

        jobs = []
        for s in resume_skills:
            jobs.extend(fetch_jobs(s))

        seen = set()
        for job in jobs:
            if job["id"] in seen:
                continue
            seen.add(job["id"])

            score, matched, missing = match_job(job.get("description",""))
            if score == 0:
                continue

            st.markdown('<div class="job-card">', unsafe_allow_html=True)
            st.markdown(f"<div class='company'>{job['company']['display_name']}</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='role'>{job['title']}</div>", unsafe_allow_html=True)
            st.write(f"📍 {job['location']['display_name']}")
            st.progress(score/100)
            st.write(f"Match Score: **{score}%**")
            st.markdown(f"[Apply Now]({job['redirect_url']})")
            st.markdown('</div>', unsafe_allow_html=True)

    # -------- SKILL GAP + COURSES --------
    with col2:
        st.subheader("🧠 Skill Gap Analysis")

        for skill in resume_skills:
            level = 90 if skill in ["python","sql"] else 50
            st.write(skill.title())
            st.progress(level/100)

        st.subheader("📚 Recommended Courses")

        courses = {
            "AWS": "AWS Cloud Practitioner – Coursera",
            "Machine Learning": "ML with Python – Coursera",
            "Data Analysis": "Data Analytics Professional – Coursera",
        }

        for skill, course in courses.items():
            st.markdown('<div class="course">', unsafe_allow_html=True)
            st.write(f"🎓 **{course}**")
            st.caption(f"Recommended to improve {skill}")
            st.markdown('</div>', unsafe_allow_html=True)

# ---------------- FOOTER ----------------
st.caption("Enterprise-grade UI • Live jobs via Adzuna • AI-ready architecture")