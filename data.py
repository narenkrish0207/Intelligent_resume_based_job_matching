import streamlit as st
import boto3
from datetime import datetime

# -------- AWS CONFIG --------
BUCKET = "resume-upload-project0207"
REGION = "ap-south-1"

s3 = boto3.client("s3", region_name=REGION)

# -------- STREAMLIT UI --------
st.title("📄 Resume Upload System")

user_id = st.text_input("Enter User ID")
file = st.file_uploader("Upload Resume", type=["pdf", "docx"])

# -------- UPLOAD BUTTON --------
if st.button("Upload Resume"):
    if not user_id:
        st.error("❌ Please enter User ID")
    elif not file:
        st.error("❌ Please upload a resume file")
    else:
        try:
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            file_name = f"resumes/{user_id}/{timestamp}_{file.name}"

            s3.upload_fileobj(
                file,
                BUCKET,
                file_name,
                ExtraArgs={
                    "ContentType": file.type,
                    "Metadata": {
                        "user_id": user_id,
                        "upload_time": timestamp
                    }
                }
            )

            st.success("✅ Resume uploaded successfully!")
            st.write("📂 Stored in S3 path:")
            st.code(file_name)

        except Exception as e:
            st.error("❌ Resume upload failed")
            st.exception(e)