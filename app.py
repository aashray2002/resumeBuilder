import streamlit as st
import json
import os

from prompt_generator import prompt_generate
from gemini_sender import send_to_gemini
from render_resume import render_resume
from generate_pdf import html_to_pdf

st.set_page_config(
    page_title="Resume Optimizer",
    layout="wide"
)

st.title("AI Resume Optimizer")

uploaded_resume = st.file_uploader(
    "Upload Existing Resume JSON",
    type=["json"]
)

job_description = st.text_area(
    "Paste Job Description",
    height=300
)

if st.button("Optimize Resume"):

    if uploaded_resume and job_description:

        with open(
            "resume.json",
            "wb"
        ) as f:
            f.write(uploaded_resume.read())

        with open(
            "job_description.txt",
            "w",
            encoding="utf-8"
        ) as f:
            f.write(job_description)

        st.info("Generating Prompt")

        prompt_generate()

        st.info("Opening Gemini")

        send_to_gemini()

        render_resume()

        html_to_pdf()

        st.success("Resume Generated")

        with open(
            "resume.pdf",
            "rb"
        ) as f:

            st.download_button(
                "Download PDF",
                f,
                file_name="resume.pdf"
            )