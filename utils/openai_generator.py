import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize OpenAI client using API key
client = OpenAI(api_key=os.getenv("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"))

def generate_tailored_resume(resume_text, job_desc):
    prompt = f"""You're a resume optimization expert. Rewrite the resume below to better align with the job description. Make it sound more relevant and ATS-optimized.

Resume:
{resume_text}

Job Description:
{job_desc}

Tailored Resume:"""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    return response.choices[0].message.content.strip()

def generate_cover_letter(resume_text, job_desc):
    prompt = f"""You're a professional career writer. Based on the resume and job description below, write a short, tailored, and impactful cover letter.

Resume:
{resume_text}

Job Description:
{job_desc}

Cover Letter:"""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    return response.choices[0].message.content.strip()
