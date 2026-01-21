.
.
🤖 Intelligent Resume-Based Job Recommendation & Skill Gap Analysis System

An AI-powered career intelligence platform that analyzes resumes, fetches live job listings, evaluates skill relevance, identifies skill gaps, and recommends personalized learning paths using NLP and cloud technologies.

📌 Overview

Traditional job portals rely on basic keyword matching and often fail to capture the true context of a candidate’s skills. This project solves that problem by implementing a multi-stage intelligent pipeline that understands resume content, aligns it with real-time job market data, and delivers actionable career insights to improve employability.

✨ Features

📄 Resume upload and automated analysis

🔐 Secure resume storage using AWS S3

🧠 Intelligent skill extraction and normalization

🌐 Live job fetching via Adzuna Job Search API

🎯 Resume-to-job relevance matching

📊 Job match score calculation

🧩 Skill gap identification

📚 Personalized course and upskilling recommendations

🖥️ Interactive and modern Streamlit dashboard

🔄 System Workflow
Resume Upload
     ↓
AWS S3 Secure Storage
     ↓
Resume Text Extraction & Cleaning
     ↓
Skill Identification & Enrichment
     ↓
Live Job Data Fetching (Adzuna API)
     ↓
Skill Matching & Relevance Scoring
     ↓
Skill Gap Analysis
     ↓
Course & Learning Recommendations
     ↓
Results Visualization (Streamlit Dashboard)

🧩 Architecture (Stage-Wise)
🔹 Stage 1 – Resume Upload

Users upload resumes via a Streamlit interface. Files are validated and securely stored in an AWS S3 bucket along with metadata such as timestamp and user ID.

🔹 Stage 2 – Resume Parsing

PDF and DOCX resumes are processed to extract raw text, which is cleaned and structured for further NLP analysis.

🔹 Stage 3 – Skill Enrichment

Relevant technical and professional skills are extracted from resume text and normalized to standardized industry skill names.

🔹 Stage 4 – Job Matching & Scoring

Live job listings are fetched from the Adzuna API. Resume skills are compared with job descriptions to compute match scores and identify matched and missing skills.

🔹 Stage 5 – Visualization & Learning Insights

A premium Streamlit dashboard presents job matches, relevance scores, skill gaps, explainable matching insights, and recommended learning resources.

📁 Project Structure
Final_project/
│
├── app.py                  # Main Streamlit application
├── stage2_runner.py        # Resume text extraction logic
├── stage3_runner.py        # Skill enrichment pipeline
├── stage4_runner.py        # Job matching & scoring logic
│
├── extract_text.py         # PDF/DOCX text extraction utilities
├── semantic_match.py       # Semantic skill matching
├── scoring.py              # Match score calculation
├── explain_match.py        # Explainable AI match reasoning
│
├── fetch_jobs.py           # Live job fetching via Adzuna API
├── course_recommender.py   # Course recommendations for skill gaps
│
├── requirements.txt        # Project dependencies
├── README.md               # Project documentation
└── .venv/                  # Virtual environment

🛠️ Tech Stack
Frontend

Streamlit

Custom CSS (Glassmorphism-inspired UI)

Backend & Cloud

Python

AWS S3

AWS IAM

AI / NLP

Resume text processing

Skill extraction & normalization

Semantic similarity matching

Explainable AI logic

External APIs

Adzuna Job Search API (live job market data)
