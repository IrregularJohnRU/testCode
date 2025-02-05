import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


@pytest.fixture() #фикстура с открытием браузера (предусловие) у нас одна, а тестов в разных файлах будет много, поэтому вынесли её в отдельный файл
def driver(): #driver = browser
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Firefox(options=options)
    driver.maximize_window()
    driver.implicitly_wait(3)
    yield driver
    driver.close()