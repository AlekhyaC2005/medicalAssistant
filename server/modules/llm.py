from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def get_llm_chain(retriever):
    llm = ChatGroq(
        groq_api_key=GROQ_API_KEY,
        model_name="llama-3.1-8b-instant",
        temperature=0.0  # important for medical safety
    )

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                """
        You are MediBot, an AI assistant for medical document understanding.
        
        RULES:
        - Answer ONLY from the provided context.
        - If the answer is not present, say:
          "I'm sorry, but I couldn't find relevant information in the provided documents."
        - Do NOT diagnose or give treatment advice.
        - Do NOT hallucinate.
        """
            ),
            ("human", "Context:\n{context}"),
            ("human", "Question:\n{question}")
        ]
    )

    rag_chain = (
        {
            "context": retriever,
            "question": RunnablePassthrough()
        }
        | prompt
        | llm
        | StrOutputParser()
    )

    return rag_chain
