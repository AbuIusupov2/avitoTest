import os
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

# URL страницы
url = "https://www.avito.ru/avito-care/eco-impact"

# Открыть страницу
driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()

# Локатор для счётчиков
locator = "//div[@class='desktop-impact-items-F7T6E']"

def findElement(driver, locator):
    action = ActionChains(driver)
    element = driver.find_element(By.XPATH, locator)
    ActionChains(driver).move_to_element(element).perform()

findElement(driver, locator)

# Создание папки для скриншотов, если она не существует
folder_path = 'output'
os.makedirs(folder_path, exist_ok=True)

# Путь для сохранения скриншота
screenshot_path = os.path.join(folder_path, 'Тест-кейс 1: Проверка начального отображения всех счетчиков.png')

# Делаем скриншот и сохраняем его в файл
driver.save_screenshot(screenshot_path)
