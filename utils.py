import re
from datetime import datetime

def clean_text(text):
    return re.sub(r'\s+', ' ', text).strip()

def is_likely_heading(text, font_size, avg_font_size=12):
    if not text or len(text) < 4:
        return False
    # Heuristics: All caps, title-case, short and large font
    return (
        font_size >= avg_font_size + 2 and
        (text.istitle() or text.isupper()) and
        len(text.split()) <= 12
    )

def classify_heading_level(font_size, avg_font_size):
    if font_size > avg_font_size + 5:
        return "H1"
    elif font_size > avg_font_size + 3:
        return "H2"
    elif font_size > avg_font_size + 1:
        return "H3"
    else:
        return "H4"

def get_current_timestamp():
    return datetime.now().isoformat()
