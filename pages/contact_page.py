from selenium.webdriver.common.by import By
from pages.base_page import Base_page
from time import sleep

class Contact(Base_page):
    CONTACT_BTN = (By.NAME,'Contact')
    CALL_CENTER_NR = (By.LINK_TEXT,'tel:021 9196')

    def navigate_to_page(self):
        self.chrome.get('https://altex.ro/')

    def click_contact_btn(self):
        self.chrome.find_element(*self.CONTACT_BTN).click()

    def check_call_center_nr(self):
        expected = 'tel:021 9196'
        actual = self.chrome.find_element(*self.CALL_CENTER_NR)
        self.assertEqual(expected,actual, 'nr nu se potriveste')
