from behave import *

@given ('contact: I am a user and looking for contact phone')
def step_impl(context):
    context.contact_page.navigate_to_page

@When ('contact:I click contact button')
def step_impl(context):
    context.contact_page.click_contact_btn

@Then('contact:I check the call center number')
def step_impl(context):
    context.contact_page.check_call_center_nr