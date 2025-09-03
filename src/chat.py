import os
import sys

from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_postgres import PGVector
from pydantic import SecretStr

from search import search_prompt

load_dotenv()


def main():
    chain = search_prompt()

    if not chain:
        print("Não foi possível iniciar o chat. Verifique os erros de inicialização.")
        return

    embeddings = OpenAIEmbeddings(
        model=os.getenv("OPENAI_MODEL", "text-embedding-3-small"),
        api_key=SecretStr(os.getenv("LLM_API_KEY", "")),
    )

    store = PGVector(
        embeddings=embeddings,
        collection_name=os.getenv("PGVECTOR_COLLECTION", ""),
        connection=os.getenv("DATABASE_URL", ""),
        use_jsonb=True,
    )

    print("Faça sua pergunta:")

    if sys.stdin.isatty():
        print("PERGUNTA: ", end="", flush=True)
    for query in sys.stdin:
        if not query or query == "q" or query == "quit":
            print("tchau")
            return

        embedding_results = store.similarity_search_with_score(query, k=10)

        ctx = "".join([doc.page_content for doc, _ in embedding_results])

        result = chain.invoke(
            {
                "contexto": ctx,
                "pergunta": query,
            }
        )

        print(f"RESPOSTA: {result}")

        print("=" * 30)
        if sys.stdin.isatty():
            print("PERGUNTA: ", end="", flush=True)


if __name__ == "__main__":
    main()
