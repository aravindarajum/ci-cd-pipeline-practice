
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def test_selenium_browser_title():
    options = Options()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)
    driver.get('http://selenium.dev')
    expected_title = 'Selenium'
    actual_title = driver.title
    assert actual_title == expected_title
    driver.quit()