import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

class SearchTest(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--disable-notifications')
        options.add_experimental_option("useAutomationExtension", False)
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("prefs", {'intl.accept_languages': 'en'})
        service = Service('chromedriver.exe')
        self.driver = webdriver.Chrome(service=service, options=options)

    def test_search_selenide_duckduckgo(self):
        driver = self.driver

        # 1
        driver.get('https://duckduckgo.com/')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'searchbox_input')))
        assert 'DuckDuckGo' in driver.title, 'Главная страница не загрузилась'
        print('1: Главная страница duckduckgo')

        # 2
        search_input = driver.find_element(By.ID, 'searchbox_input')
        search_input.send_keys('selenide')
        search_input.send_keys(Keys.ENTER)
        print('2: Поиск selenide')

        # 3
        first_link = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'a[data-testid="result-extras-url-link"]'))
        )
        href = first_link.get_attribute('href')
        assert href == 'https://selenide.org/', f'Первая ссылка не https://selenide.org/: {href}'
        print('3: https://selenide.org/ - это 1 ссылка')

        # 4
        images_tab = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//a[contains(@href, "ia=images") and contains(text(), "Images")]'))
        )
        images_tab.click()
        print('4: Вкладка Images')

        # 5
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-testid="zci-images"] img[alt]'))
        )
        images_container = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-testid="zci-images"]'))
        )
        first_image = images_container.find_element(By.CSS_SELECTOR, 'img[alt]')
        alt_text = first_image.get_attribute('alt')
        assert 'selenide' in alt_text.lower(), f'В alt первой картинки нет слова selenide: {alt_text}'
        print('5: Первая картинка связана с selenide')

        # 6
        duckbar = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div#react-duckbar[data-testid="duckbar"]'))
        )
        all_tab = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, '//a[contains(normalize-space(.), "All")]'))
        )
        all_tab.click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'a[data-testid="result-extras-url-link"]'))
        )
        print('6: Вкладка All')

        # 7
        first_link = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'a[data-testid="result-extras-url-link"]'))
        )
        href = first_link.get_attribute('href')
        assert href == 'https://selenide.org/', f'Первая ссылка на вкладке All не https://selenide.org/: {href}'
        print('7: https://selenide.org/ - это 1 ссылка')

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
