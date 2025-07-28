import os
from PyPDF2 import PdfReader

def extract_subsection_texts(top_sections, base_folder="."):
    results = []

    for sec in top_sections:
        pdf_path = os.path.join(base_folder, sec["collection_folder"], "PDFs", sec["document"])
        reader = PdfReader(pdf_path)
        page_num = sec["page_number"] - 1  # 0-indexed

        if page_num < len(reader.pages):
            page = reader.pages[page_num]
            text = page.extract_text()
            if text:
                results.append({
                    "document": sec["document"],
                    "refined_text": text.strip()[:2000],  # Limit for quality
                    "page_number": sec["page_number"]
                })

    return results
