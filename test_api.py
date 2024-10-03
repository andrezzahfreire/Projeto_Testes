import requests

# URL base da API
BASE_URL = "http://localhost:5000"

# Testando o método GET para listagem de dados
def test_listar_dados():
    response = requests.get(f"{BASE_URL}/listar")
    assert response.status_code == 200
    assert isinstance(response.json(), list), "Esperado que a resposta seja uma lista"

# Testando o método POST para criar novos dados
def test_criar_item():
    payload = {"campo1": "valor1", "campo2": "valor2"}
    response = requests.post(f"{BASE_URL}/postar", json=payload)
    assert response.status_code == 201, "Esperado status 201 Created"
    assert response.json().get("message") == "Item criado com sucesso"

# Testando erro no método POST com dados inválidos
def test_criar_item_invalido():
    payload = {"campo1": "valor1"}  # campo2 ausente
    response = requests.post(f"{BASE_URL}/postar", json=payload)
    assert response.status_code == 400, "Esperado status 400 Bad Request"
