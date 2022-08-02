Feature: Altex create account test
  Background:
    Given sign in: I am a user on altex sign in page


    @jules
    Scenario: Create gmail account


      When sign in: I click account button
      When sign_in: I clic inregistrare button
      When sign in: I set my first name to "Marian"
      When sign_in: I set my last name ti "Albu"
      Then sign in : I set email to "{negru.marianalexandru@gmail.com}"

