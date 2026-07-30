# System Testing Plan

## Project

Student Assignment and Study Planner

## Testing Stage

Week 9 — Iteration 3

## 1. Objective

The objective of system testing is to verify that the complete
Student Assignment and Study Planner works correctly from the user's
perspective.

The system tests will also be used as the execution plan for the
final project demonstration.

## 2. Test Environment

- Operating system: Windows development computer
- Browser: Google Chrome
- Python: 3.13.7
- Django: 5.2
- Database: SQLite
- Application address: http://127.0.0.1:8000/
- Repository: CP3407-Student-Planner

## 3. Test Accounts

### Administrator Account

- Username: david
- Role: Superuser and administrator

### Standard User Account 1

- Username: student1
- Role: Standard student user

### Standard User Account 2

- Username: student2
- Role: Standard student user used for data-isolation testing

Passwords are stored locally and are not included in the repository.

## 4. Test Data

The following sample data may be used during testing:

### Course

- Code: CP3501
- Name: Data Science

### Assessment

- Title: Data Analysis Report
- Type: Assignment
- Weighting: 30%

### Study Task

- Title: Write report introduction
- Priority: High
- Status: To Do
- Estimated effort: 2 hours

Temporary data should be used when testing delete operations.

## 5. Entry Criteria

System testing can begin when:

- The development server starts successfully.
- All database migrations have been applied.
- All automated tests pass.
- User registration and login are available.
- Course, assessment and task pages can be opened.
- The GitHub Issues and Project Board are available.

## 6. Exit Criteria

System testing is complete when:

- All planned system test cases have been executed.
- Every test case has a Pass or Fail result.
- Every discovered defect has a GitHub Issue.
- High-severity defects have been fixed and retested.
- The final demonstration workflow can be completed successfully.
- The instructor has access to the repository and project board.

## 7. Bug Tracking Process

Bugs identified during system testing will be recorded as separate
GitHub Issues.

Each bug report must contain:

- Related user story
- Test case that identified the problem
- Steps to reproduce
- Expected result
- Actual result
- Severity
- Evidence
- Resolution
- Retest result

The bug workflow is:

1. Open
2. In Progress
3. Fixed
4. Retested
5. Closed

A bug will only be closed after the relevant system test has been
repeated successfully.

## 8. System Test Cases

| ID | Related Story | Test Scenario | Main Steps | Expected Result | Actual Result | Status | Bug Issue |
|---|---|---|---|---|---|---|---|
| ST-01 | US-01 | Register a new user | Open Register, enter valid details, submit | Account is created and user enters Dashboard | Not executed | Not Run | — |
| ST-02 | US-02 | Login and logout | Log out, enter valid credentials, log in, then log out | Login succeeds, protected pages are available, logout returns to login | Not executed | Not Run | — |
| ST-03 | US-03 | Course CRUD | Create, view, edit and delete a temporary course | All four operations complete successfully | Not executed | Not Run | — |
| ST-04 | US-03 | Duplicate course validation | Create the same course code twice for one user | Second course is rejected with a validation message | Not executed | Not Run | — |
| ST-05 | US-05 | Assessment CRUD | Create, view, edit and delete a temporary assessment | All four operations complete successfully | Not executed | Not Run | — |
| ST-06 | US-05 | Assessment date validation | Enter a start date later than the due date | Assessment is rejected and an error is displayed | Not executed | Not Run | — |
| ST-07 | US-06 | Study task CRUD | Create, view, edit and delete a temporary task | All four operations complete successfully | Not executed | Not Run | — |
| ST-08 | US-06 | Course and assessment validation | Select a course and an assessment belonging to another course | Task is rejected with a validation message | Not executed | Not Run | — |
| ST-09 | US-09 | Search, filter and sort | Search by title, filter by status and priority, change sorting | Only matching tasks appear in the selected order | Not executed | Not Run | — |
| ST-10 | US-07 | Overdue and completion behaviour | Give an unfinished task a past due date, then mark it complete | It first shows Overdue, then Completed and no longer Overdue | Not executed | Not Run | — |
| ST-11 | US-08 / US-12 | Dashboard progress | Change task and assessment statuses and return to Dashboard | Counts, completion percentage and lists update correctly | Not executed | Not Run | — |
| ST-12 | US-10 | Personal data isolation | Create data as student1, log in as student2 and attempt to access it | student2 cannot view or modify student1's records | Not executed | Not Run | — |

## 9. Automated Test Evidence

The project currently contains 18 automated tests.

Command:

```cmd
python manage.py test planner -v 2