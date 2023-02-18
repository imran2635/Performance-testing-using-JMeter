Feature: Login
  As a user
  I want to be able to log in to the website
  So that i can access yb account

  Scenario: Successful login
    Given I am on the login page
    When I enter my username and password
    When I click on login button
    Then I should be redirect to dashboard page and close browser