import sys
import os
import base64
import docx

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import streamlit as st
from utils.parser import extract_text_from_file
from utils.openai_generator import generate_tailored_resume, generate_cover_letter

st.set_page_config(page_title="AI Resume & Cover Letter Generator", layout="centered")
st.title("📄 AI Resume & Cover Letter Generator")

# ===== File download helpers =====
def create_docx(text, filename):
    doc = docx.Document()
    for line in text.split('\n'):
        doc.add_paragraph(line)
    filepath = f"{filename}.docx"
    doc.save(filepath)
    return filepath

def download_file(path):
    with open(path, "rb") as f:
        b64 = base64.b64encode(f.read()).decode()
        href = f'<a href="data:application/octet-stream;base64,{b64}" download="{os.path.basename(path)}">📥 Download {os.path.basename(path)}</a>'
        return href

# ===== ATS Score =====
def calculate_ats_score(resume_text, jd_text):
    resume_words = set(resume_text.lower().split())
    jd_words = set(jd_text.lower().split())
    matched = resume_words & jd_words
    score = round(len(matched) / len(jd_words) * 100, 2)
    return score, matched

# ===== Input Fields =====
st.markdown("### 📄 Upload Your Current Resume or Paste Below")
resume_file = st.file_uploader("Upload Resume", type=["pdf", "docx"])
resume_textbox = st.text_area("Or paste your resume here 👇", height=200)

st.markdown("### 📝 Upload Job Description or Paste Below")
jd_file = st.file_uploader("Upload Job Description", type=["pdf", "docx", "txt"])
jd_textbox = st.text_area("Or paste the job description here 👇", height=200)

# ===== Logic: Use whichever inputs are available =====
if (resume_file or resume_textbox.strip()) and (jd_file or jd_textbox.strip()):
    resume_text = extract_text_from_file(resume_file) if resume_file else resume_textbox
    jd_text = extract_text_from_file(jd_file) if jd_file else jd_textbox

    st.subheader("🧾 Resume Text Preview")
    st.text_area("Resume", resume_text, height=200)

    st.subheader("📝 Job Description Preview")
    st.text_area("Job Description", jd_text, height=200)

    # ATS Score
    score, matched_keywords = calculate_ats_score(resume_text, jd_text)
    st.markdown(f"### 📊 ATS Score: **{score}% match**")
    with st.expander("🧠 Matched Keywords"):
        st.write(sorted(list(matched_keywords)))

    st.markdown("---")
    st.subheader("⚙️ AI Tools")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("🎯 Generate Tailored Resume"):
            with st.spinner("Generating tailored resume..."):
                tailored_resume = generate_tailored_resume(resume_text, jd_text)
                st.subheader("📄 Tailored Resume")
                st.text_area("Generated Resume", tailored_resume, height=400)

                resume_path = create_docx(tailored_resume, "Tailored_Resume")
                st.markdown(download_file(resume_path), unsafe_allow_html=True)

    with col2:
        if st.button("✉️ Generate Cover Letter"):
            with st.spinner("Generating cover letter..."):
                cover_letter = generate_cover_letter(resume_text, jd_text)
                st.subheader("✉️ Cover Letter")
                st.text_area("Generated Cover Letter", cover_letter, height=400)

                cover_path = create_docx(cover_letter, "Cover_Letter")
                st.markdown(download_file(cover_path), unsafe_allow_html=True)

else:
    st.info("📎 Please upload or paste both a resume and a job description.")
