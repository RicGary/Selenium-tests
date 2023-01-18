from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.common.by import By


chromedriver_autoinstaller.install()


driver = webdriver.Chrome()
driver.get("https://pt.wikipedia.org/wiki/Python")

assert "Python" in driver.title

elem = driver.find_elements(By.XPATH, '//span[@class="mw-headline"]')

print(elem)