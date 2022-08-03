from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep


class Browser:
    chrome = webdriver.Chrome("D:\Marian\pers\chromeDriver\chromedriver.exe")
    chrome.maximize_window()
    chrome.implicitly_wait(10)
    chrome.set_page_load_timeout(15)
    chrome.maximize_window()
    chrome.get("https://altex.ro/")

    def close(self):
        self.chrome.quit()
