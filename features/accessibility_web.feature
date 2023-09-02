Feature: Validate Portfolio Accessibility

  Scenario: Validate Portfolio Title
    Given I navigate to "https://www.petudeveloper.com/"
    When I wait for page finish loading
    Then I verify page title is "David Alvarez Portfolio"

  Scenario: Validate Portfolio main heading
    Given I navigate to "https://www.petudeveloper.com/"
    When I wait for page finish loading
    Then I can see "David Alvarez" main heading
