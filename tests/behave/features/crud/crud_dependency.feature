Feature: CRUD dependencies through the API

  Scenario: Creates and lists dependencies
    Given I create a "dependencies" through the API
      | name       | version   |
      | django     | 2.2.10    |
      | requests   | 2.18.4    | 
      | pytest     | 3.6.4     |
    When I make the following API call
      | method | endpoint      |
      | GET    | /dependencies |
    Then response contains "3" records
    And the response should contain the following "dependencies"
      | name       | version   |
      | django     | 2.2.10    |
      | requests   | 2.18.4    |
      | pytest     | 3.6.4     |
