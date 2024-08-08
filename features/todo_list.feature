Feature: Todo List

  Scenario: Add a task
    Given the task list is empty
    When I add the task "Buy milk"
    Then the task list should contain 1 task

  Scenario: List tasks
    Given the task list contains
      | Buy milk |
      | Call doctor |
    When I list the tasks
    Then it should show
      | 1. Buy milk - Incomplete |
      | 2. Call doctor - Incomplete |

  Scenario: Mark a task as completed
    Given the task list contains
      | Buy milk |
    When I mark task 1 as completed
    Then task 1 should appear as completed

  Scenario: Edit a task
    Given the task list contains
      | Buy milk |
    When I edit task 1 to "Buy skim milk"
    Then task 1 should say "Buy skim milk"

  Scenario: Clear the task list
    Given the task list contains
      | Buy milk |
      | Call doctor |
    When I clear the task list
    Then the task list should be empty