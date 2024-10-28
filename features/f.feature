Feature: Github register page check
  Scenario:
    Given I launch Chrome browser
    When I open github sign up page
    And I enter and email address "valamiesvalami@gmail.com"
    And I click on the Continue button
    And I enter a password "123"
    Then Invalid password error should be visible
