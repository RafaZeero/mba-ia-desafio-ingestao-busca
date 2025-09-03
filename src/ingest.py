import os

from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings
from langchain_postgres import PGVector
from langchain_text_splitters import RecursiveCharacterTextSplitter
from pydantic import SecretStr

load_dotenv()

PDF_PATH = os.getenv("PDF_PATH")

if not PDF_PATH:
    raise RuntimeError("Environment variable PDF_PATH not set")


def ingest_pdf(pdf_path: str):
    docs_to_split = PyPDFLoader(pdf_path).load()
    print("doc loaded")

    chunks = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=150,
    ).split_documents(docs_to_split)
    print(f"chunks splitted: {len(chunks)}")

    if not chunks:
        print("could not split docs into chunks")
        return

    doc_list = [
        Document(
            page_content=chunk.page_content,
            metadata={k: v for k, v in chunk.metadata.items() if v not in ("", None)},
        )
        for chunk in chunks
    ]
    print(f"doc_list created: {len(doc_list)}")

    ids = [f"doc-{i}" for i in range(len(doc_list))]
    print(f"ids generated: {len(ids)}")

    embeddings = OpenAIEmbeddings(
        model=os.getenv("OPENAI_MODEL", "text-embedding-3-small"),
        api_key=SecretStr(os.getenv("LLM_API_KEY", "")),
    )
    print("embeddings completed")

    store = PGVector(
        embeddings=embeddings,
        collection_name=os.getenv("PGVECTOR_COLLECTION", ""),
        connection=os.getenv("DATABASE_URL", ""),
        use_jsonb=True,
    )

    store.add_documents(documents=doc_list, ids=ids)
    print("process completed")


if __name__ == "__main__":
    ingest_pdf(PDF_PATH)
