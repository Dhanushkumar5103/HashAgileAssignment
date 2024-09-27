# Resume Information Extractor

## Overview
The Resume Information Extractor is a Python-based application that allows users to upload a resume in PDF format and extract key information such as name, email, phone number, college name, and skills. The application leverages the Gemini API to convert the uploaded resume into text and retrieve the necessary data. The application also saves the uploaded resume into MongoDB using GridFS for efficient storage and retrieval.

## Working
- Text data is extracted from the resume using the `pdf_to_text` function.
- The extracted data is then passed to the `extract_with_gemini_api` function to extract only the needed data from the resume using the `gemini-flash` model.
- Extracted data is returned in JSON format and converted into a `DataFrame` to display it as a table.
- The resume PDF is stored in MongoDB using GridFS, and users can download it later by entering the associated `Resume ID`.

## Features
- **Resume Upload:** Users can upload resumes in PDF format.
- **Resume Data Extraction:** The application extracts key information such as name, email, phone number, college name, and skills using the Gemini API.
- **Resume Storage:** Uploaded resumes are saved to MongoDB using GridFS, ensuring large files are handled efficiently.
- **Resume Retrieval:** Users can view a table of all stored resumes with their unique `Resume ID` and download them by entering the `Resume ID`.

## Tech Stack
- Python
- Streamlit (for the UI)
- PyPDF2 (for PDF text extraction)
- Gemini API (for information extraction)
- MongoDB (for storing and retrieving resume files via GridFS)
- Pandas (for data representation)

## Requirements
- Python 3.x
- Streamlit
- PyPDF2
- Pandas
- MongoDB
- Pymongo
- GridFS (for handling file storage in MongoDB)

## MongoDB Setup
Make sure you have MongoDB installed and running. The MongoDB instance is connected via:
```
mongo_uri = "mongodb://localhost:27017"
```
You will need to create a database named `resume_db` where resumes will be stored in the `GridFS` format.

## How to Run the Application
1. Clone the repository and navigate to the project directory.
2. Ensure all dependencies are installed using the command:
   ```bash
   pip install -r requirements.txt
   ```
3. Start your MongoDB service if not running.
4. Run the application using Streamlit:
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

Additionally, you will see a list of stored resumes with their `Resume ID` and can download resumes by entering the corresponding `Resume ID`.

