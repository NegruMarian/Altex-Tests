Feature: Altex, verificare contact
  Background:
    Given contact: I am a user and looking for contact phone

    @Contact
    Scenario: check contact number

      When contact:I click contact button
      Then contact:I check the call center number