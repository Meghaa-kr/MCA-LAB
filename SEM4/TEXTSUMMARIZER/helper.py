import fitz  # PyMuPDF
from transformers import pipeline
import requests
from bs4 import BeautifulSoup
#pip install pytesseract
import pytesseract
from PIL import Image
import io

model_path = r"C:\Users\megha\Downloads\local_summarizer-20250306T080019Z-001\local_summarizer"
print(model_path)  # Update this path if needed
summarizer = pipeline("summarization", model=model_path, tokenizer=model_path)
def summarize_text(text, max_chunk_size=1000):
    chunks = [text[i:i + max_chunk_size] for i in range(0, len(text), max_chunk_size)]
    summaries = [summarizer(chunk, max_length=150, min_length=50, do_sample=False)[0]['summary_text'] for chunk in chunks]
    return " ".join(summaries)

def summarize_pdf(pdf_file):
    try:
        text = extract_text_from_pdf(pdf_file)
        if text.startswith("No extractable text"):
            return text
        return summarize_text(text)
    except Exception as e:
        return f"Error processing PDF: {e}"
    
def summarize_webpage(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        paragraphs = soup.find_all("p")
        text = " ".join([p.get_text() for p in paragraphs])

        if len(text.strip()) == 0:
            return "No valid text found on the webpage."
        if len(text) < 50:  # Avoids summarization errors
            return "Text is too short to summarize."

        return summarize_text(text)

    return "Failed to fetch webpage content."

def extract_text_from_pdf(pdf_file):
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    text = " ".join([page.get_text("text") for page in doc])

    if text.strip():
        return text  # Return extracted text if available

    # If no text is found, try extracting from images (OCR)
    text = ""
    for page_num in range(len(doc)):
        pix = doc[page_num].get_pixmap()
        img = Image.open(io.BytesIO(pix.tobytes()))
        text += pytesseract.image_to_string(img) + " "

    return text.strip() if text.strip() else "No extractable text found in the PDF."
