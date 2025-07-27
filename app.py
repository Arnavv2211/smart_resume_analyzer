import streamlit as st
from analyze import extract_text_from_pdf, extract_text_from_docx, get_similarity

st.title("📄 Smart Resume Analyzer using NLP + ML")

resume_file = st.file_uploader("Upload your Resume", type=["pdf", "docx"])
jd_input = st.text_area("Paste the Job Description here...")

if st.button("Analyze"):
    if resume_file and jd_input:
        if resume_file.name.endswith(".pdf"):
            resume_text = extract_text_from_pdf(resume_file)
        else:
            resume_text = extract_text_from_docx(resume_file)

        score = get_similarity(resume_text, jd_input)
        st.sucess(f"✅ Resume Match Score: {score}%")

        if score > 75:
            st.balloons()
            st.info("Awesome! Your resume matches the job well.")
        else:
            st.warning("Your resume could use more relevant keywords.")
    else:
        st.error("⚠️ Please upload a resume and enter the job description.")


