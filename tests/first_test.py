from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By

def test_page_title():
    '''
    En el caso al service no se le agrega el path toma la variable de entorno del OS
    En el caso le agregamos el path es donde esta la ruta del archivo
    '''
    browser = webdriver.Edge(service=Service())
    browser.get("https://github.com")
    titleElement = browser.find_element(By.ID, "hero-section-brand-heading")

    assert titleElement.text == "Build and ship software on a single, collaborative platform"

    browser.quit()