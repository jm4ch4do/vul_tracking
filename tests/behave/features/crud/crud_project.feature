Feature: CRUD dependencies through the API

  Scenario: Creates and lists projects
    Given I create a "projects" through the API
      | name       | description    | created_at  | dependencies                                            |
      | Apollo     | Moon mission   | 2024-01-10  | ["django==2.2.10", "requests==2.18.4", "pytest==7.4.0"] |
      | Mars Rover | Exploring Mars | 2024-06-01  | ["pillow==6.2.1", "jinja2==2.10", "urllib3==1.24.1"]    |
      | Voyager    | Space probe    | 2025-01-01  | ["sqlalchemy==1.3.0", "pyyaml==5.1", "celery==4.3.0"]   |
    When I make the following API call
      | method | endpoint     |
      | GET    | /projects    |
    Then response contains "3" records
    And the response should contain the following "projects"
      | name       | description    | created_at  |
      | Apollo     | Moon mission   | 2024-01-10  |
      | Mars Rover | Exploring Mars | 2024-06-01  |
      | Voyager    | Space probe    | 2025-01-01  |
    When I make the following API call
      | method | endpoint      |
      | GET    | /dependencies |
    Then response contains "9" records
    And the response should contain the following "dependencies"
      | name       | version  |
      | django     | 2.2.10   |
      | requests   | 2.18.4   |
      | pytest     | 7.4.0    |
      | pillow     | 6.2.1    |
      | jinja2     | 2.10     |
      | urllib3    | 1.24.1   |
      | sqlalchemy | 1.3.0    |
      | pyyaml     | 5.1      |
      | celery     | 4.3.0    |

 