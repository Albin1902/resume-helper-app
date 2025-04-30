import google.generativeai as genai

# Configure Gemini API
genai.configure(api_key="AIzaSyCc7ihu4uLsyDxfRirnJ-onXRha8gV4RPA")  # Replace with your key

# Load model
model = genai.GenerativeModel("models/gemini-1.5-pro-latest")

def generate_tailored_resume(resume_text, jd_text):
    prompt = f"""
You are a professional resume writer. Improve and tailor the following resume for the job description provided.

Resume:
{resume_text}

Job Description:
{jd_text}

Rewrite the resume to focus only on the relevant skills and experiences. Optimize for clarity, action verbs, and ATS keyword matching.
Output only the improved resume.
"""
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"❌ Error generating tailored resume: {e}"

def generate_cover_letter(resume_text, jd_text):
    prompt = f"""
Using the following resume and job description, write a personalized cover letter for the job.

Resume:
{resume_text}

Job Description:
{jd_text}

Address the letter to 'Hiring Manager'. Keep it professional, enthusiastic, and relevant.
"""
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"❌ Error generating cover letter: {e}"
