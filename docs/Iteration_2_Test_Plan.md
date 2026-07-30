# Iteration 2 Automated Test Plan

## Project

Student Assignment and Study Planner

## Testing Objective

The objective is to verify the main application workflows, validation
rules and user-data access restrictions.

The tests use Django TestCase and an isolated temporary test database.

## Selected User Stories

- US-02 User Login and Logout
- US-03 Course Management
- US-05 Assessment Management
- US-06 Study Task Management
- US-09 Search, Filter and Sort

## Test Cases

| ID | User Story | Test Case | Expected Result |
|---|---|---|---|
| T01 | US-02 | Anonymous user opens dashboard | User is redirected to login |
| T02 | US-02 | User submits valid login credentials | User is redirected to dashboard |
| T03 | US-02 | Logged-in user submits logout request | User is logged out and redirected |
| T04 | US-03 | User creates a valid course | Course is stored for that user |
| T05 | US-03 | User enters a duplicate course code | Validation error is displayed |
| T06 | US-03 | User accesses another user's course | Request returns 404 |
| T07 | US-05 | User creates a valid assessment | Assessment is stored |
| T08 | US-05 | Assessment start date is after due date | Validation error is displayed |
| T09 | US-05 | User accesses another user's assessment | Request returns 404 |
| T10 | US-06 | User creates a task linked to an assessment | Task is stored correctly |
| T11 | US-06 | Task course and assessment do not match | Validation error is displayed |
| T12 | US-06 | User creates a completed task | completed_at is automatically set |
| T13 | US-09 | User searches by task title | Only matching tasks are displayed |
| T14 | US-09 | User filters tasks by priority | Only matching priorities are displayed |
| T15 | US-09 | User sorts task titles in descending order | Tasks appear in Z–A order |

## Automated Test Count

A total of 15 automated tests are planned.

## Test Command

```cmd
python manage.py test planner -v 2