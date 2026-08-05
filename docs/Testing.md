# Testing and Quality Assurance

## 1. Testing Overview

Testing was performed throughout the development of the Student
Assignment and Study Planner.

The project used several complementary testing approaches:

- Django automated testing
- Test-driven development
- Mock testing
- Code-coverage measurement
- Browser-based system testing
- Defect tracking using GitHub Issues
- Regression testing after defect correction

Automated tests checked individual workflows and business rules, while
system testing verified the complete application from the user's
perspective.

## 2. Automated Testing

Automated tests were implemented using Django's `TestCase` framework.

The final automated test suite contained nineteen tests covering the
main application workflows.

The tested areas included:

- User registration
- User login and logout
- Authentication protection
- Course creation and management
- Duplicate course-code validation
- Assessment creation and management
- Assessment date validation
- Study-task creation and management
- Course and assessment relationship validation
- Task search
- Course filtering
- Priority filtering
- Status filtering
- Task sorting
- Personal data ownership
- Quick task completion
- Completion timestamp behaviour
- Changing a completed task back to In Progress
- Regression testing for GitHub Issue #15

## 3. Running the Automated Tests

The complete test suite can be executed from the project directory using:

```cmd
python manage.py test planner -v 2
```

The final result was:

```text
Ran 19 tests
OK
```

This result confirmed that all nineteen automated tests passed after the
final code changes.

## 4. Test-Driven Development

The quick Mark complete feature was implemented using the
Red-Green-Refactor test-driven development process.

### 4.1 Red

Tests were written before the feature was implemented.

The tests initially failed because the required URL, view logic and
interface control did not exist.

This demonstrated that the tests could detect the missing behaviour.

### 4.2 Green

The required URL pattern, view logic and template button were
implemented.

The feature allowed a logged-in user to mark an unfinished study task as
completed directly from the task list.

The implementation was continued until the new tests passed.

### 4.3 Refactor

Task completion-time behaviour was kept in the `StudyTask` model through
the following method:

```python
sync_completion_time()
```

This avoided repeating the same completion logic across multiple views.

The model manages the task state, while the views remain responsible for
processing requests and returning responses.

## 5. Mock Testing

The task-completion feature depends on the current date and time.

To make the test deterministic, `unittest.mock.patch` was used to
replace `timezone.now()` with a fixed value during testing.

The mocked time allowed the test to verify that:

- The task status changed to Completed
- The completion timestamp was created
- The timestamp matched the expected fixed time
- Repeated test runs produced the same result

Without mocking, the expected timestamp would change whenever the test
was executed.

## 6. Code Coverage

Code coverage was measured using `coverage.py`.

The following commands were used:

```cmd
coverage erase
coverage run manage.py test planner
coverage report -m
coverage html
```

The text report identified the number of executed and unexecuted
statements in each Python file.

The HTML report was generated in the following directory:

```text
htmlcov
```

The measured project coverage reached approximately 83% during the
automated-testing stage.

The report showed stronger coverage in the models and lower coverage in
some form and view branches.

Coverage information was used to identify code paths that needed
additional tests.

## 7. System Testing

Automated testing was followed by browser-based system testing.

A system testing plan containing twelve test cases was created in:

```text
docs/System_Testing_Plan.md
```

The system tests covered:

| Test ID | Test Area |
|---|---|
| ST-01 | User registration |
| ST-02 | Login and logout |
| ST-03 | Course create, view, edit and delete |
| ST-04 | Duplicate course-code validation |
| ST-05 | Assessment create, view, edit and delete |
| ST-06 | Assessment date validation |
| ST-07 | Study-task create, view, edit and delete |
| ST-08 | Course and assessment relationship validation |
| ST-09 | Search, filtering and sorting |
| ST-10 | Overdue and task-completion behaviour |
| ST-11 | Dashboard statistic updates |
| ST-12 | User-data isolation |

Each system test recorded:

- Test purpose
- Preconditions
- Test steps
- Expected result
- Actual result
- Pass or Fail status
- Related GitHub Issue when applicable

## 8. System Testing Data

Dedicated testing records were used to avoid damaging the demonstration
data.

Examples included:

```text
Course code: SYS1001
Course name: System Testing Course

Assessment title: System Testing Assessment

Study-task title: Prepare final testing evidence
Priority: High
Status: To Do
```

Additional temporary records were created specifically for deletion
testing.

Two separate normal user accounts were used to test data ownership and
access control.

Invalid data was also used to verify validation behaviour, including:

- A duplicate course code
- An assessment start date later than its due date
- A task linked to an assessment from a different course
- Direct access to another user's record URL

## 9. Defect Identified During System Testing

System testing identified GitHub Issue #15:

> Editing a completed task causes a NameError.

The error occurred during this workflow:

```text
Completed task
→ Edit
→ Change status to In Progress
→ Save
```

Instead of saving the task, Django displayed:

```text
NameError:
name '_update_task_completion_time' is not defined
```

The task-update view contained an obsolete function call:

```python
_update_task_completion_time(task)
```

The function was no longer defined after the completion-time logic had
been moved to the `StudyTask` model.

## 10. Defect Tracking

The defect was recorded using GitHub Issues.

The Issue contained:

- Bug description
- Related user story
- Related system test case
- Test environment
- Steps to reproduce
- Expected result
- Actual result
- Severity
- Resolution
- Retest result

The Issue was also added to the GitHub Project Board so its progress
could be tracked.

## 11. Defect Resolution

The obsolete function call was replaced with:

```python
task.sync_completion_time()
```

This used the existing model method instead of duplicating the
completion-time logic inside the view.

## 12. Regression Testing

A regression test was added after Bug #15 was fixed.

The regression test verified that:

- A Completed task could be changed to In Progress
- The request did not produce a server error
- The new task status was saved
- The `completed_at` field was cleared
- The user was redirected to the task list

The full automated test suite was then executed again.

The final result remained:

```text
Ran 19 tests
OK
```

The workflow was also retested manually through the browser.

After successful retesting, GitHub Issue #15 was updated and closed.

## 13. User-Data Isolation Testing

Data isolation was tested using two normal student accounts.

The first user created courses, assessments and tasks.

After logging in as the second user:

- The first user's courses were not displayed
- The first user's assessments were not displayed
- The first user's tasks were not displayed
- Direct access to the first user's edit URL returned a 404 response

The 404 response was intentional because records are retrieved using
both the record identifier and the logged-in owner.

This behaviour prevents one student from accessing another student's
academic data.

## 14. Validation Testing

The following validation rules were tested:

### Course validation

A user cannot create two courses using the same course code.

### Assessment date validation

An assessment cannot have a start date later than its due date.

### Study-task relationship validation

A selected assessment must belong to the selected course.

### Ownership validation

Users can only create and manage records that belong to their own
accounts.

These rules were tested through automated tests and browser-based system
testing.

## 15. Final Testing Result

The final quality-assurance evidence included:

- Nineteen passing automated tests
- Approximately 83% measured code coverage
- Twelve completed browser-based system tests
- Test-driven development evidence
- Mock testing for time-dependent behaviour
- GitHub defect tracking
- One identified defect fixed and closed
- A regression test protecting the corrected workflow
- Successful final demonstration

The final automated-testing result was:

```text
Ran 19 tests
OK
```

The final system-testing result was Pass.

## 16. Testing Limitations

The testing process had several limitations:

- Testing was performed using SQLite rather than a production database
- The application was tested locally using Django's development server
- Automated browser testing was not implemented
- Email notifications were not included in the final system
- Public-server deployment was not tested
- Performance testing with large datasets was outside the project scope

These limitations do not affect the demonstrated core workflows but
would need to be addressed before a large-scale production deployment.

## 17. Testing Conclusion

Testing was integrated into the development process rather than being
performed only at the end.

Automated tests verified the main workflows and business rules.

TDD and mock testing supported the implementation of task completion,
while system testing verified complete user interactions through the
graphical interface.

The discovery and resolution of GitHub Issue #15 demonstrated the full
defect-management process:

```text
System test failure
→ GitHub Issue
→ Code correction
→ Regression test
→ Manual retest
→ Issue closure
```

The final test results provided evidence that the delivered application
matched the planned core requirements.