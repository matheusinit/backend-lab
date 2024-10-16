# API REST com FastAPI

Este projeto é um exemplo de como criar uma API REST utilizando o FastAPI. O FastAPI é um framework moderno, rápido (alta performance) e fácil de usar para construir APIs com Python 3.6+ baseado em padrões como OpenAPI e JSON Schema.

## Tabela de conteúdo

- [Tabela de conteúdo](#tabela-de-conteúdo)
- [Requisitos](#requisitos)
- [Instalação](#instalação)
- [Executando a Aplicação (em desenvolvimento)](#executando-a-aplicação-em-desenvolvimento)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Endpoints](#endpoints)
- [Contribuição](#contribuição)
- [Licença](#licença)

## Requisitos

- Python 3.11+
- FastAPI

## Instalação

1. Clone o repositório:
  ```bash
  git clone https://github.com/matheusinit/fastapi-k8s.git
  ```
2. Navegue até o diretório do projeto:
  ```bash
  cd fastapi-k8s
  ```
3. Entre no ambiente virtual:
  ```bash
  poetry shell
  ```
4. Instale as dependências:
  ```bash
  poetry install
  ```

## Executando a Aplicação

1. Inicie o servidor:
  ```bash
  fastapi run app/server.py
  ```

> Para desenvolvimento, use `fastapi dev ...`

2. Acesse a documentação interativa da API em [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

## Estrutura do Projeto

```plaintext
.
├── fast_api_k8s
│   ├── api                   # API Routes
│   │   └── book.py           # Routes to book resource
│   ├── config.py             # Project configuration
│   ├── database.py           # Database
│   ├── dtos.py               # DTOs
│   ├── models.py             # Models' classes
│   └── server.py             # Server configuration
├── .env.sample
├── docker-compose.yml        # Docker Compose configuration
├── LICENSE
├── poetry.lock               # Poetry lock file
├── pyproject.toml            # Poetry configuration file
└── README.md                 
```

## Endpoints

- `GET /books/`: Retorna uma lista de itens.
- `POST /books/`: Cria um novo item.
- `GET /books/{book_id}`: Retorna um item específico.
- `PUT /books/{book_id}`: Atualiza um item específico.
- `DELETE /books/{book_id}`: Deleta um item específico.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [MIT](./LICENSE) para mais detalhes.