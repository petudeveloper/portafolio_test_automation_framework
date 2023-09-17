Feature: Validate Brittany Chiang Portfolio Accessibility

  Background:
    Given I navigate to brittany's portfolio
    When I wait for page finish loading


  Scenario: Validate page Title
    Then I verify that the title has the name "Brittany Chiang"

  Scenario: Validate main Heading structure
    Then I can see "Brittany Chiang" main heading

  Scenario: Validate images alternate text
    When I wait for page finish loading
    Then I verify the presence of alternate text for all images

  Scenario: Validate accessibility using axe
    Then I check the accessibility of the page using axe tool

  Scenario: Validate the presence of sections
    Then I validate the sections of the portfolio
      | section     |
      | About       |
      | Experience  |
      | Projects    |
