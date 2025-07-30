# summarizer.py
from transformers import pipeline

# Load model once at startup
summarizer = pipeline("summarization")

def summarize_text(text, max_length=120, min_length=30):
    if len(text.split()) < 50:
        return "Text too short to summarize meaningfully."
    
    summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
    return summary[0]['summary_text']
