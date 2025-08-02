Feature: CRUD dependencies through the API

  Scenario: Creates and lists dependencies
    Given I create a "projects" through the API
      | name       | description    | created_at  |
      | Apollo     | Moon mission   | 2024-01-10  |
      | Mars Rover | Exploring Mars | 2024-06-01  |
      | Voyager    | Space probe    | 2025-01-01  |
    When I make the following API call
      | method | endpoint     |
      | GET    | /projects    |
    Then response contains "3" records
    And the response should contain the following "projects"
      | name       | description    | created_at  |
      | Apollo     | Moon mission   | 2024-01-10  |
      | Mars Rover | Exploring Mars | 2024-06-01  |
      | Voyager    | Space probe    | 2025-01-01  |
