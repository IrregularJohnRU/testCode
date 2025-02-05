import time  # табу автотестов, используется для конкретного примера, т.к. тут неявное ожидание
from pages.homepage import HomePage
from pages.product import ProductPage


def test_open_s6(driver):
    homepage = HomePage(driver)
    homepage.open()
    homepage.click_galaxy_s6()
    product_page = ProductPage(driver)
    product_page.check_title_is('Samsung galaxy s6')

    
def test_two_monitors(driver):
    homepage = HomePage(driver)
    homepage.open()
    # driver.get('https://demoblaze.com/index.html')
    homepage.click_monitor()
    # monitor_link = driver.find_element(By.CSS_SELECTOR, value='''[onclick="byCat('monitor')"]''')
    # monitor_link.click()
    time.sleep(2) # табу автотестов, используется для конкретного примера, т.к. тут неявное ожидание
    homepage.check_products_count(2)
    # monitors = driver.find_elements(By.CSS_SELECTOR, value='.card')
    # assert len(monitors) == 2 #функция len - количество мониторов = 2 шт.
