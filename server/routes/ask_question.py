# routes/ask_question.py
from fastapi import APIRouter, Form
from modules.mem_client import mem_client
from modules.llm import get_llm_chain

router = APIRouter()

@router.post("/ask/")
async def ask_question(question: str = Form(...)):
    # 1️⃣ Search memory
    results = mem_client.search(query=question, limit=3)

    if not results:
        return {"answer": "No relevant information found in the document."}

    # 2️⃣ Build context
    context = "\n\n".join(
        r["content"] for r in results
    )

    # 3️⃣ Generate answer
    chain = get_llm_chain()
    answer = chain.invoke({
        "context": context,
        "question": question
    })

    return {
        "answer": answer,
        "sources": [
            r.get("metadata", {}) for r in results
        ]
    }
