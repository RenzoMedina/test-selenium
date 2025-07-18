from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By

def test_page_title():
    '''
    En el caso al service no se le agrega el path toma la variable de entorno del OS
    En el caso le agregamos el path es donde esta la ruta del archivo
    '''
    options = Options()
    options.use_chromium = True
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--remote-debugging-port=9222")
    options.add_argument("--user-data-dir=/tmp/edge-profile")

    browser = webdriver.Edge(service=Service(),options=options)
    browser.get("https://github.com")
    titleElement = browser.find_element(By.ID, "hero-section-brand-heading")

    assert titleElement.text == "Build and ship software on a single, collaborative platform"

    browser.quit()