Feature: Validate David Alvarez Portfolio Accessibility

  Background:
    Given I navigate to "https://www.petudeveloper.com/"
    When I wait for page finish loading

  Scenario: Validate Title
    Then I verify that the title has the name "David Alvarez"

  Scenario: Validate main Heading structure
    Then I can see "David Alvarez" main heading

  Scenario: Validate images alternate text
    Then I verify the presence of alternate text for all images

  Scenario: Validate accessibility using axe
    Then I check the accessibility of the page using axe tool

  Scenario Outline: Validate the presence of sections
    Then I validate "<section>" in David Alvarez Portfolio
    Examples:
      | section     |
      | About       |
      | Experience  |
      | Work        |
      | Contact     |
