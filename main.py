'''
This file is the driver code for Resume Information Extractor Application.
'''

import streamlit as st
import hash
import pandas as pd
from bson import ObjectId

st.title("Resume Uploader")

uploaded_file = st.file_uploader("Choose a resume file (PDF)", type=["pdf"])

if st.button("Retrieve Resume Data"):
    if uploaded_file:
        # Extract and display resume data
        resume_data = hash.display_resume_info(uploaded_file)

        if isinstance(resume_data, dict):
            resume_data['skills'] = "".join(i + " | " for i in resume_data['skills']).strip()
            
            # Save the resume to MongoDB and get the ID
            resume_id = hash.save_resume_to_db(uploaded_file)
            resume_data['resume_id'] = str(resume_id)  # Store resume ID for later use
            
            resume_df = pd.DataFrame(list(resume_data.items()), columns=["Key", "Value"])
            st.subheader("Retrieved Resume Data:")
            st.table(resume_df)  
        else:
            st.write("Error: Retrieved data is not in the expected format.")
    else:
        st.write("Please upload a resume first.")

# Display stored resumes
st.subheader("Stored Resumes in MongoDB")
stored_resumes = hash.fs.find()  
resume_list = list(stored_resumes)

if resume_list:
    resume_ids = [str(resume._id) for resume in resume_list]
    resume_names = [resume.filename for resume in resume_list]
    resume_df = pd.DataFrame({"Resume ID": resume_ids, "Filename": resume_names})
    st.table(resume_df)


resume_id_input = st.text_input("Enter Resume ID to Download")

if st.button("Download Resume PDF"):
    if resume_id_input:
        try:
            resume_file_id = ObjectId(resume_id_input)  # Convert input string to ObjectId
            resume_file = hash.fs.get(resume_file_id)  # Fetch the file from GridFS
            
            st.download_button(
                label="Download Resume",
                data=resume_file.read(),
                file_name=resume_file.filename,
                mime='application/pdf'
            )
        except Exception as e:
            st.write(f"Error: {e}")
    else:
        st.write("Please enter a valid Resume ID.")
