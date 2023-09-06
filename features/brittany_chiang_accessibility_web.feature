Feature: Validate David Alvarez Portfolio Accessibility

  Scenario: Validate Title
    Given I navigate to "https://brittanychiang.com/"
    When I wait for page finish loading
    Then I verify page title is "Brittany Chiang"

  Scenario: Validate main Heading structure
    Given I navigate to "https://brittanychiang.com/"
    When I wait for page finish loading
    Then I can see "Brittany Chiang" main heading

  Scenario: Validate images alternate text
    Given I navigate to brittany's portfolio
    When I wait for page finish loading
    Then I verify the presence of alternate text for all images

  Scenario: Validate accessibility using axe
    Given I navigate to brittany's portfolio
    When I wait for page finish loading
    Then I check the accessibility of the page using axe tool

#  Scenario: Validate color contrast
#    Given I navigate to david's portfolio
#    When I wait for page finish loading
#    Then I verify the color contrast of the portfolio image
