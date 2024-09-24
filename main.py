'''
This file is the driver code for Resume Information Extractor Application.
'''
import streamlit as st
import hash
import pandas as pd

st.title("Resume Uploader")

uploaded_file = st.file_uploader("Choose a resume file (PDF)", type=["pdf"])

if st.button("Retrieve Resume Data"):
    if uploaded_file:
        
        resume_data = hash.display_resume_info(uploaded_file)

        
        if isinstance(resume_data, dict):
            resume_data['skills'] = "".join(i+" | " for i in resume_data['skills']).strip()
            resume_df = pd.DataFrame(list(resume_data.items()), columns=["Key", "Value"])
            st.subheader("Retrieved Resume Data:")
            st.table(resume_df)  
        else:
            st.write("Error: Retrieved data is not in the expected format.")
    else:
        st.write("Please upload a resume first.")
