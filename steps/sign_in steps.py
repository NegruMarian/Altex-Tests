from behave import *
#
@given('sign in: I am a user on altex sign in page')
def step_impl(context):
    context.sign_in_page.navigate_to_first_page()

@When ('sign in: I click account button')
def step_impl(context):
    context.sign_in_page.click_cont_btn()

@When('sign_in: I clic inregistrare button')
def step_impl(context):
    context.sign_in_page.inregistrare_btn()

@When('sign in: I set my first name to "Marian"')
def step_impl(context, name):
    context.sign_in_page.input_first_name(name)

@When('sign_in: I set my last name ti "Albu"')
def step_impl(context, name):
    context.sign_in_page.input_last_name(name)
@Then('sign in : I set email to "{negru.marianalexandru@gmail.com}"')
def step_impl(context, email):
    context.sign_in_page.input_email(email)

