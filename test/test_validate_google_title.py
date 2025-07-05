from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def test_browser_title():
    options = Options()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get('https://www.google.com/')
    expected_title = 'Google'
    actual_title = driver.title
    assert actual_title == expected_title
    driver.quit()
