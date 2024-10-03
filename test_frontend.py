from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

@pytest.fixture
def browser():
    # Configura o WebDriver (neste caso, Chrome)
    driver = webdriver.Chrome(executable_path="path/to/chromedriver")  # Atualize o caminho para o chromedriver
    driver.implicitly_wait(10)  # Espera até 10 segundos para encontrar elementos
    yield driver
    driver.quit()

# Testando a listagem de dados na página inicial
def test_listagem_dados(browser):
    browser.get("http://localhost:3000")  # URL do frontend
    itens = browser.find_elements(By.CLASS_NAME, "list-item")  # Ajuste o seletor de acordo com sua página
    assert len(itens) > 0, "Esperado que a lista contenha itens"

# Testando responsividade (tamanho da janela simulando mobile)
def test_responsividade_mobile(browser):
    browser.set_window_size(375, 667)  # Tamanho do iPhone 6/7/8
    browser.get("http://localhost:3000")
    navbar_toggle = browser.find_element(By.CLASS_NAME, "navbar-toggle")  # Ajuste o seletor de acordo com sua página
    assert navbar_toggle.is_displayed(), "Esperado que o menu esteja visível em modo mobile"
