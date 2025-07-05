from selenium import webdriver

def test_browser_title():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://www.google.com/')
    expected_title = 'Google'
    actual_title = driver.title
    assert actual_title == expected_title
    driver.quit()
