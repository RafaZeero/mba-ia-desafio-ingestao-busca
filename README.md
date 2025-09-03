# Desafio MBA Engenharia de Software com IA - Full Cycle

## Setup

### Dependências

Para fazer inicializar o projeto, você precisa do UV, um package e project manager.
Rode o comando abaixo, em caso de dúvidas, acesse: https://docs.astral.sh/uv/getting-started/installation/

```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Configuração das Variáveis de Ambiente

Antes de iniciar o projeto, você precisa configurar as variáveis de ambiente:

1. Copie o arquivo `.env.example` para `.env`:
```sh
cp .env.example .env
```

2. Edite o arquivo `.env` e configure as seguintes variáveis:
   - `LLM_API_KEY`: Sua chave de API para o modelo de linguagem
   - `DATABASE_URL`: URL de conexão com o PostgreSQL (ex: `postgresql://user:password@localhost:5432/dbname`)
   - `PG_VECTOR_COLLECTION_NAME`: Nome da coleção no pgvector
   - `PDF_PATH`: Caminho para o arquivo PDF que será processado

### Passo a passo

Para iniciar o setup do projeto, execute o seguinte:

```sh
uv sync
```

Isso vai criar uma pasta `.venv` e instalar as dependencias que estao no arquivo `pyproject.toml`

Ao instalar as dependencias, você precisa iniciar a ingestao de documentos. Isso requer o container rodando com o pgvector
seguido da adicao do(s) documento(s) vetorizados nessa vector store.
Para isso, execute os seguintes comandos:

```sh
docker compose up -d
poe ingest
```


O setup está pronto, agora você pode rodar o projeto com o comando:


```sh
poe chat
```
