from browser import Browser
from selenium.webdriver.common.by import By
from pages.base_page import Base_page
from time import sleep
from selenium.webdriver.common.keys import Keys


class Sign_in(Base_page):
    CONT_BTN = (By.XPATH, '/html/body/div[2]/div[1]/div[1]/div/div/div[2]/div[2]/a/span[2]/span')
    INREGISTRARE_BTN = (By.LINK_TEXT, 'Inregistrare')
    FIRST_NAME_BTN = (By.NAME, 'first_name')
    LAST_NAME_BTN = (By.NAME, 'last_name')
    INPUT_EMAIL = (By.NAME, 'email')
    INPUT_PASS = (By.NAME, 'password')

    def navigate_to_first_page(self):
        self.chrome.get('https://altex.ro/')

    def click_cont_btn(self):
        self.chrome.find_element(*self.CONT_BTN).click()
        sleep(3)

    def inregistrare_btn(self):
        self.chrome.find_element(*self.INREGISTRARE_BTN).click()
        sleep(3)

    # def input_first_name(self, name):
    #     self.chrome.find_element(*self.FIRST_NAME_BTN).send_keys(name)
    #     sleep(1)

    # def input_last_name(self, name):
    #     self.chrome.find_element(*self.LAST_NAME_BTN).send_keys(name)

    def input_email(self, email):
        self.chrome.find_element(*self.INPUT_EMAIL).send_keys(email)


    def input_pass(self,password):
        self.chrome.find_element(*self.INPUT_PASS).send_keys(password)