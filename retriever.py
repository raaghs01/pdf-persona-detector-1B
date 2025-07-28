# ✅ retriever.py
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

def get_relevant_sections(sections_by_doc, persona_task, top_k=5):
    task_embedding = model.encode(persona_task, convert_to_tensor=True)
    scored_sections = []

    for doc_name, sections in sections_by_doc.items():
        for sec in sections:
            if not sec.get("text"):
                continue
            section_embedding = model.encode(sec["text"], convert_to_tensor=True)
            score = float(util.cos_sim(task_embedding, section_embedding)[0])
            scored_sections.append({
                "document": sec["document"],
                "section_title": sec.get("title", sec["text"][:60]),
                "score": score,
                "page_number": sec["page_number"]
            })

    top_sections = sorted(scored_sections, key=lambda x: x["score"], reverse=True)[:top_k]
    return top_sections
