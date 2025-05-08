import openai
import os

# Option 1: use environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

# Option 2 (unsafe): hardcode temporarily
# openai.api_key = "your-openai-api-key"

def generate_tailored_resume(resume_text, job_desc):
    prompt = f"""
You're a resume optimization expert. Rewrite the resume below so it better aligns with the job description. Emphasize relevant skills, keywords, and responsibilities.

Resume:
{resume_text}

Job Description:
{job_desc}

Tailored Resume:
"""
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    return response['choices'][0]['message']['content'].strip()

def generate_cover_letter(resume_text, job_desc):
    prompt = f"""
Write a compelling, personalized cover letter based on the following resume and job description.

Resume:
{resume_text}

Job Description:
{job_desc}

Cover Letter:
"""
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    return response['choices'][0]['message']['content'].strip()
