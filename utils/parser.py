import docx
from pdfminer.high_level import extract_text

def extract_text_from_file(file):
    """
    Extracts raw text from uploaded PDF, DOCX, or TXT files.
    """
    if file.name.endswith(".pdf"):
        return extract_text(file)
    elif file.name.endswith(".docx"):
        return extract_text_from_docx(file)
    elif file.name.endswith(".txt"):
        return file.read().decode("utf-8")
    else:
        return "❌ Unsupported file type"

def extract_text_from_docx(file):
    doc = docx.Document(file)
    return "\n".join([para.text for para in doc.paragraphs])
