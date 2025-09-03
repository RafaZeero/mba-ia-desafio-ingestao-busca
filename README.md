# Desafio MBA Engenharia de Software com IA - Full Cycle

## Setup

### Dependências

Para fazer inicializar o projeto, você precisa do UV, um package e project manager.
Rode o comando abaixo, em caso de dúvidas, acesse: https://docs.astral.sh/uv/getting-started/installation/

```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
```

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
