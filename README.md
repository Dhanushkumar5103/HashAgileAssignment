# Resume Information Extractor

## Overview
The Resume Information Extractor is a Python-based application that allows users to upload a resume in PDF format and extract key information such as name, email, phone number, college name, and skills. The application leverages the Gemini API to convert the uploaded resume into text and retrieve the necessary data.

## Working
- Text data is extracted from the resume using ```bash pdf_to_text``` function.
- The extracted data is then passed to ```bash extract_eith_gemini_api``` to extract only needed data from the resume. This uses ```gemini-flash``` model.
- Then the data is returned in json format to convert the data into a ```Dataframe``` and display the dataframe into a table.


## Tech Stack
- Python
- Gemini
- Streamlit


## Requirements
- Python 3.x
- Streamlit
- Pandas (for data representation)


## Run the Application
   To start the application, run the following command:

   ```bash
   streamlit run main.py
   ```

## Example Output
The application will extract and display information such as:
- Name
- Email
- Phone Number
- College Name
- Skills
