from PyPDF2 import PdfReader

def extract_pdf_sections(pdf_path):
    reader = PdfReader(pdf_path)
    sections = []
    for page_num, page in enumerate(reader.pages):
        text = page.extract_text()
        if not text:
            continue

        # Basic heuristic: look for line breaks or headings
        lines = [line.strip() for line in text.split('\n') if line.strip()]
        for i, line in enumerate(lines):
            # Heading candidate: Capitalized or short
            if line.isupper() or (line.istitle() and len(line.split()) < 10):
                # Get 3-5 lines following the title as context
                content = ' '.join(lines[i+1:i+6])
                sections.append({
                    "text": line,
                    "page_number": page_num + 1,
                    "context": content
                })

    return sections
