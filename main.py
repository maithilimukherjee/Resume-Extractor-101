import pdfplumber
import re

def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text

resume_text = extract_text_from_pdf("sampleResume.pdf")
print(resume_text)

# Example of extracting specific information using regex
def extract_email(text):
    match = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text)
    return match[0] if match else None

def extract_phone(text):
    match = re.findall(r"\+?\d[\d -]{8,13}\d", text)
    return match[0] if match else None

email = extract_email(resume_text)
phone = extract_phone(resume_text)

print(f"Email: {email}")
print(f"Phone: {phone}")

def extract_skills(text):
    skills_list = ["python", "java", "sql", "excel", "machine learning", "html", "css"]
    found_skills = []
    for skill in skills_list:
        if skill.lower() in text.lower():
            found_skills.append(skill)
    return found_skills

skills = extract_skills(resume_text)
print("Skills:", skills)

import pandas as pd

data = {
    "email": [email],
    "phone": [phone],
    "skills": [", ".join(skills)]
}

df = pd.DataFrame(data)
df.to_csv("applicants.csv", index=False)

print("Saved to applicants.csv ✅")

