# ✅ pipeline.py
import os
import json
from parser import extract_pdf_sections
from retriever import get_relevant_sections
from scorer import extract_subsection_texts
from utils import get_current_timestamp

def run_pipeline(collection_path):
    input_path = os.path.join(collection_path, "challenge1b_input.json")
    output_path = os.path.join(collection_path, "challenge1b_output.json")

    with open(input_path, "r", encoding='utf-8') as f:
        config = json.load(f)

    documents = config["documents"]
    persona = config["persona"]["role"]
    job = config["job_to_be_done"]["task"]

    # Extract all sections from all PDFs
    sections_by_doc = {}
    for doc in documents:
        pdf_file = os.path.join(collection_path, "PDFs", doc["filename"])
        sections = extract_pdf_sections(pdf_file)
        for s in sections:
            s["document"] = doc["filename"]
            s["collection_folder"] = collection_path
        sections_by_doc[doc["filename"]] = sections

    # Get top sections per persona-task
    top_sections = get_relevant_sections(sections_by_doc, f"{persona}: {job}", top_k=5)

    # Attach collection folder info for scoring
    for sec in top_sections:
        sec["collection_folder"] = collection_path

    # Extract full paragraphs/subsections
    subsection_texts = extract_subsection_texts(top_sections, base_folder=".")

    # Final Output
    output = {
        "metadata": {
            "input_documents": [doc["filename"] for doc in documents],
            "persona": persona,
            "job_to_be_done": job,
            "processing_timestamp": get_current_timestamp()
        },
        "extracted_sections": [
            {
                "document": s["document"],
                "section_title": s["section_title"],
                "importance_rank": i + 1,
                "page_number": s["page_number"]
            } for i, s in enumerate(top_sections)
        ],
        "subsection_analysis": subsection_texts
    }

    with open(output_path, "w", encoding="utf-8") as out_f:
        json.dump(output, out_f, indent=2, ensure_ascii=False)

    print(f"\u2705 Completed {collection_path}")

if __name__ == "__main__":
    for folder in os.listdir():
        if folder.startswith("Collection_") and os.path.isdir(folder):
            run_pipeline(folder)
