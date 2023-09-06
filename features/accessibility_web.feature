Feature: Validate Portfolio Accessibility

  Scenario: Validate Title
    Given I navigate to "https://www.petudeveloper.com/"
    When I wait for page finish loading
    Then I verify page title is "David Alvarez Portfolio"

  Scenario: Validate main Heading structure
    Given I navigate to "https://www.petudeveloper.com/"
    When I wait for page finish loading
    Then I can see "David Alvarez" main heading

  Scenario: Validate images alternate text
    Given I navigate to david's portfolio
    When I wait for page finish loading
    Then I verify the presence of alternate text for all images

#  Scenario: Validate color contrast
#    Given I navigate to david's portfolio
#    When I wait for page finish loading
#    Then I verify the color contrast of the portfolio image
