from browser import Browser
from pages.sign_in_page import Sign_in


def before_all(context):
    context.browser = Browser()
    context.sign_in_page = Sign_in



def after_all(context):
    context.browser.close()