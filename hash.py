'''
This file contains the essential methods to run Resume Information Extractor Application.
'''
from flask import Flask, render_template, request, redirect
from tabulate import tabulate
import google.generativeai as genai
import dotenv
import PyPDF2
import requests  
import json
import re
import os

dotenv.load_dotenv()

def pdf_to_text(pdf_path):
    '''This function extracts the text from pdf file'''
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)

        text = ''
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
        
    return text

def extract_with_gemini_api(text):
    '''This function extracts the required data from the text data using gemini model'''
    api_key = os.getenv("API_KEY")
    genai.configure(api_key = api_key)
    model = genai.GenerativeModel(
        model_name = "gemini-1.5-flash"
    )
    prompt = f'''Given the text data only extract the below 
    details from the text. This text data is extracted from resume. Extract the details carefully. The details that are
    needed to be extracted are [name , email , phone number , college name , skills]. Give the response in json file
    with the given list value as its key. Just give the json file only dont give any additional data.
    data : {text}'''

    res = model.generate_content([prompt])
    result = res.text[7:-3]
    data = json.loads(result)

    return data

def display_resume_info(data):
    '''This function returns the essential data'''
    resume_text = pdf_to_text(data)
    resume_info = extract_with_gemini_api(resume_text)
    return resume_info
