# Iteration 3 Review

## 1. Iteration Objective

The objective of Iteration 3 was to complete the final feature work,
apply test-driven development, perform system testing and establish a
formal defect-tracking process.

This iteration also prepared the application and supporting evidence for
the final Week 10 demonstration.

## 2. Planned Work

The planned work for Iteration 3 included:

- Implementing quick task completion
- Applying test-driven development
- Using mock testing for completion timestamps
- Preparing a system testing plan
- Executing browser-based system tests
- Recording defects using GitHub Issues
- Fixing and retesting identified defects
- Updating the GitHub Project Board
- Preparing the final project demonstration

## 3. Test-Driven Development

The quick Mark complete feature was implemented using the
Red-Green-Refactor process.

### 3.1 Red

Automated tests were written before the feature was implemented.

The initial tests failed because the required URL, view behaviour and
interface control did not yet exist.

This confirmed that the tests were able to detect the missing feature.

### 3.2 Green

The required URL pattern, view logic and template button were then
implemented.

The implementation allowed the logged-in user to mark an unfinished
study task as completed directly from the task list.

The feature also recorded the completion timestamp.

The code was developed until the new tests passed.

### 3.3 Refactor

The completion-time behaviour was placed in the `StudyTask` model using:

```python
sync_completion_time()
```

This avoided duplicating completion-time logic across different views.

The view remained responsible for handling the request, while the model
was responsible for maintaining the task's completion state.

## 4. Mock Testing

`unittest.mock.patch` was used to replace `timezone.now()` with a fixed
date and time during testing.

This allowed the completion timestamp to be checked predictably without
depending on the computer's actual current time.

Mock testing made the test repeatable and prevented timing differences
from affecting the result.

## 5. System Testing

A system testing plan containing twelve test cases was prepared.

The system tests covered:

- User registration
- Login and logout
- Course creation, viewing, editing and deletion
- Duplicate course-code validation
- Assessment creation, viewing, editing and deletion
- Assessment date validation
- Study-task creation, viewing, editing and deletion
- Course and assessment relationship validation
- Search, filtering and sorting
- Overdue and completion behaviour
- Dashboard statistic updates
- User-data isolation

Each test case included:

- Test steps
- Expected result
- Actual result
- Final status
- Related Bug Issue when applicable

## 6. Defect Identified During System Testing

System testing identified GitHub Issue #15:

> Editing a completed task causes a NameError.

The error occurred when a completed study task was edited and changed
back to In Progress.

The task-update view still called an obsolete function:

```python
_update_task_completion_time(task)
```

The function was no longer defined, so Django displayed a NameError page
when the form was submitted.

## 7. Defect Tracking

The defect was recorded using GitHub Issues.

The Bug Issue included:

- Bug description
- Related user story
- Related system test case
- Test environment
- Steps to reproduce
- Expected result
- Actual result
- Severity
- Resolution information
- Retest result

The Issue was also linked to the GitHub Project Board so that its status
could be tracked.

## 8. Defect Resolution

The obsolete function call was replaced with:

```python
task.sync_completion_time()
```

A regression test was added to verify that:

- A Completed task can be changed back to In Progress
- The update request completes without a server error
- The task status is saved correctly
- The `completed_at` value is cleared
- The user is redirected back to the task list

The defect was then retested manually through the browser.

The task was successfully changed from Completed to In Progress without
displaying an error.

GitHub Issue #15 was updated with the resolution and retest result and
was then closed.

## 9. Final Automated Test Result

After the regression test was added, the final automated test suite
contained nineteen tests.

The test suite was executed using:

```cmd
python manage.py test planner -v 2
```

The final result was:

```text
Ran 19 tests
OK
```

This confirmed that the existing workflows and the Bug #15 regression
test passed after the final code changes.

## 10. Final System Testing Result

The twelve planned system tests were executed from the user's
perspective.

The tests covered the complete workflow from account registration to
course, assessment and study-task management.

One defect was identified during testing:

```text
GitHub Issue #15
```

The defect was fixed, retested and closed.

The final system-testing result was Pass.

## 11. Final Demonstration

The completed application was demonstrated during the Week 10 practical.

The demonstration included:

- User registration
- Login and logout
- Course management
- Assessment management
- Study-task management
- Task priorities and statuses
- Search, filtering and sorting
- Quick task completion
- Dashboard statistics
- Form validation
- User-data isolation
- Automated testing
- GitHub defect tracking

After the demonstration, the instructor was provided with access to the
GitHub repository and the private GitHub Project Board.

## 12. Feedback and Final Review

The final demonstration confirmed that the main user workflows could be
completed through the graphical web interface.

The instructor was able to review the repository, project documentation,
Issues and Project Board.

No additional major feature was added after the final demonstration.
The remaining work focused on technical documentation and final report
preparation.

## 13. Lessons Learned

Iteration 3 showed that automated testing and browser-based system
testing identify different types of problems.

The existing automated tests did not initially detect the obsolete
function call in the task-update workflow.

Manual system testing exposed the problem because it followed a complete
user interaction:

```text
Completed
→ Edit
→ In Progress
→ Save
```

The regression test then protected the workflow from the same defect
occurring again.

The iteration also demonstrated the value of GitHub Issues because the
defect history, resolution and retest evidence remained visible after
the Issue was closed.

## 14. Iteration Outcome

Iteration 3 was completed successfully.

The final project contained:

- Three completed development iterations
- A working Django web application
- Registration, authentication and user-data isolation
- Course, assessment and study-task management
- Search, filtering and sorting
- Dashboard progress summaries
- Quick task completion
- Nineteen passing automated tests
- Twelve completed system test cases
- Formal GitHub defect tracking
- One identified defect fixed and closed
- A completed final demonstration