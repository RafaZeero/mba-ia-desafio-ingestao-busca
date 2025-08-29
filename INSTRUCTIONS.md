# MBA em Engenharia de Software com IA — Desafio Técnico

## Ingestão e Busca Semântica com LangChain e Postgres

## Objetivo

Entregar um software capaz de:

1. **Ingestão**: Ler um arquivo PDF e salvar suas informações em um banco de dados PostgreSQL com extensão **pgVector**.
2. **Busca**: Permitir que o usuário faça perguntas via **linha de comando (CLI)** e receba respostas **baseadas apenas** no conteúdo do PDF. &#x20;

---

## Exemplo no CLI

**Faça sua pergunta:**

**PERGUNTA:** Qual o faturamento da Empresa SuperTechIABrazil?
**RESPOSTA:** O faturamento foi de 10 milhões de reais.

**Perguntas fora do contexto:**

* **PERGUNTA:** Quantos clientes temos em 2024?
  **RESPOSTA:** Não tenho informações necessárias para responder sua pergunta. &#x20;

---

## Tecnologias obrigatórias

* **Linguagem:** Python
* **Framework:** LangChain
* **Banco de dados:** PostgreSQL + pgVector
* **Execução do banco:** Docker & Docker Compose (docker-compose fornecido no repositório de exemplo) &#x20;

---

## Pacotes recomendados

* **Split:** `from langchain_text_splitters import RecursiveCharacterTextSplitter`
* **Embeddings:** `from langchain_openai import OpenAIEmbeddings`
* **PDF:** `from langchain_community.document_loaders import PyPDFLoader`
* **Ingestão:** `from langchain_postgres import PGVector`
* **Busca:** `similarity_search_with_score(query, k=10)` &#x20;

---

## Provedores e modelos

* **OpenAI**

  * Crie uma API Key.
  * **Embeddings:** `text-embedding-3-small`
  * **LLM para responder:** `gpt-5-nano`
* **Gemini**

  * Crie uma API Key.
  * **Embeddings:** `text-embedding-3-small`
  * **LLM para responder:** `gemini-2.5-flash-lite` &#x20;

> Observação: os nomes de modelos acima são os especificados no documento de referência deste desafio.

---

## Requisitos

### 1) Ingestão do PDF

* Dividir o PDF em *chunks* de **1000** caracteres com **150** de *overlap*.
* Converter cada *chunk* em *embedding*.
* Armazenar os vetores no PostgreSQL com **pgVector**. &#x20;

### 2) Consulta via CLI

Criar um script Python que simula um chat no terminal. Ao receber uma pergunta:

1. Vetorizar a pergunta.
2. Buscar os **10** resultados mais relevantes (**k=10**) no banco vetorial.
3. Montar o **prompt** e chamar a **LLM**.
4. Retornar a resposta ao usuário. &#x20;

#### Prompt (usar exatamente estas regras)

```
CONTEXTO:

{resultados concatenados do banco de dados}

REGRAS:
- Responda somente com base no CONTEXTO.
- Se a informação não estiver explicitamente no CONTEXTO, responda:
  "Não tenho informações necessárias para responder sua pergunta."
- Nunca invente ou use conhecimento externo.
- Nunca produza opiniões ou interpretações além do que está escrito.

EXEMPLOS DE PERGUNTAS FORA DO CONTEXTO:
Pergunta: "Qual é a capital da França?"
Resposta: "Não tenho informações necessárias para responder sua pergunta."

Pergunta: "Quantos clientes temos em 2024?"
Resposta: "Não tenho informações necessárias para responder sua pergunta."

Pergunta: "Você acha isso bom ou ruim?"
Resposta: "Não tenho informações necessárias para responder sua pergunta."

PERGUNTA DO USUÁRIO:
{pergunta do usuário}

RESPONDA A "PERGUNTA DO USUÁRIO"
```



---

## Estrutura obrigatória do projeto

> Faça um fork do repositório base e mantenha a estrutura:

```
├── docker-compose.yml
├── requirements.txt      # Dependências
├── .env.example          # Template da variável OPENAI_API_KEY
├── src/
│   ├── ingest.py         # Script de ingestão do PDF
│   ├── search.py         # Script de busca
│   ├── chat.py           # CLI para interação com usuário
├── document.pdf          # PDF para ingestão
└── README.md             # Instruções de execução
```

<!-- Se algum trecho acima já tiver sido mostrado em outra seção, considerar este bloco como repetição do mesmo conteúdo. -->



---

## Ambiente virtual (Python)

Crie e ative um ambiente virtual antes de instalar dependências:

```bash
python3 -m venv venv
source venv/bin/activate
```



---

## Ordem de execução

1. **Subir o banco de dados:**

```bash
docker compose up -d
```

2. **Executar a ingestão do PDF:**

```bash
python src/ingest.py
```

3. **Rodar o chat:**

```bash
python src/chat.py
```



---

## Entregável

* **Repositório público no GitHub** com todo o código-fonte e um **README** com instruções claras de execução. &#x20;

---

## Referências

* **Documento base do desafio (PDF / plataforma Full Cycle)**.&#x20;
* **Repositório template do desafio:** [https://github.com/devfullcycle/mba-ia-desafio-ingestao-busca/](https://github.com/devfullcycle/mba-ia-desafio-ingestao-busca/)
* **Curso de nivelamento com LangChain:** [https://github.com/devfullcycle/mba-ia-niv-introducao-langchain/](https://github.com/devfullcycle/mba-ia-niv-introducao-langchain/) &#x20;

---

*Este arquivo foi extraído e reorganizado em Markdown a partir do documento de referência do desafio.*

