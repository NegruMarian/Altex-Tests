from browser import Browser
from pages.sign_in_page import Sign_in
from pages.contact_page import Contact


def before_all(context):
    context.browser = Browser()
    context.sign_in_page = Sign_in()
    context.contact_page = Contact()




def after_all(context):
    context.browser.close()