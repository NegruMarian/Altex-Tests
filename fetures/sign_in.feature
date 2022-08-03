Feature: Altex create account test
  Background:
    Given sign in: I am a user on altex sign in page


    @Altex_creare_cont
    Scenario: Create gmail account


      When sign in: I click account button
      When sign_in: I clic inregistrare button
##      When sign in: I set my first name to "Marian"
#      When sign_in: I set my last name "Albu"
      When sign in : I set email to "negru.marianalexandru@gmail.com"
      When sign_in: I set my password to "parola1"
