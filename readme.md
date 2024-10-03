
# Projeto de Testes Automatizados

Este projeto tem como objetivo automatizar os testes de uma API e de um frontend utilizando **PyTest** para testes de API e **Selenium** para testes de interface.

## Estrutura do Projeto

```markdown
test_project/
│
├── test_api.py              # Testes para a API
├── requirements.txt         # Dependências do projeto
└── selenium_tests/
    └── test_frontend.py     # Testes para o frontend
```

## Tecnologias Utilizadas

- [Python](https://www.python.org/) - Linguagem de programação
- [PyTest](https://docs.pytest.org/en/stable/) - Framework de testes para Python
- [Requests](https://docs.python-requests.org/en/latest/) - Biblioteca para fazer requisições HTTP
- [Selenium](https://www.selenium.dev/) - Ferramenta para automação de testes de navegador

## Pré-requisitos

- Python 3.x
- [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) ou outro driver de navegador (ex.: GeckoDriver para Firefox) deve estar instalado e acessível no PATH do sistema.

## Instalação

1. Clone o repositório:

   ```bash
   git clone <URL_DO_REPOSITÓRIO>
   cd test_project
   ```

2. Crie um ambiente virtual (opcional, mas recomendado):

   ```bash
   python -m venv venv
   source venv/bin/activate   # Para Linux/Mac
   venv\Scripts\activate      # Para Windows
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

## Execução dos Testes

### Testes de API

Para executar os testes da API, execute o seguinte comando:

```bash
pytest test_api.py
```

### Testes de Frontend

Para executar os testes do frontend, execute o seguinte comando:

```bash
pytest selenium_tests/test_frontend.py
```

## Documentação dos Testes

Os testes incluem:

- **Testes de API**:
  - Validação do método `GET` para listagem de dados.
  - Validação do método `POST` para criação de novos dados.
  - Testes para verificar respostas para dados inválidos.

- **Testes de Frontend**:
  - Validação da renderização correta de dados.
  - Testes de responsividade da interface.

## Automação de Testes

Os testes podem ser automatizados usando ferramentas de integração contínua, como GitHub Actions. Um exemplo de configuração de CI está incluído em `.github/workflows/test.yml`.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).


