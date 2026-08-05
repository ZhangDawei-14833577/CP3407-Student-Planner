# Iteration 2 Review

## 1. Iteration Objective

The objective of Iteration 2 was to improve task discovery, progress
monitoring and software quality after the core record-management
features had been completed during Iteration 1.

The main focus was to make the application easier to use and to introduce
automated testing for the main user workflows.

## 2. Planned Work

The planned work for Iteration 2 included:

- Searching study tasks using keywords
- Filtering tasks by course
- Filtering tasks by priority
- Filtering tasks by status
- Sorting tasks by title
- Sorting tasks by due date
- Improving the dashboard progress summary
- Adding automated tests for the main user stories
- Measuring automated-test coverage

## 3. Completed Work

All planned search, filtering and sorting functions were implemented.

Users can now:

- Search using task titles and descriptions
- Filter tasks by course
- Filter tasks by priority
- Filter tasks by status
- Sort tasks alphabetically by title
- Sort tasks by due date
- Clear active search and filter conditions

The dashboard was also improved to display:

- Active course count
- Total study-task count
- Completed task count
- Overdue task count
- Task-completion percentage
- Task counts by status
- Assessment summaries
- Tasks due today
- Tasks due within the next seven days
- Upcoming assessments

## 4. Automated Testing

Automated tests were added for the following areas:

- Authentication
- Course management
- Assessment management
- Study-task management
- Search
- Filtering
- Sorting
- User-data ownership

The test suite was executed using:

```cmd
python manage.py test planner -v 2
```

At the end of this iteration, the automated test suite contained
approximately fifteen tests covering the main workflows.

## 5. Code Coverage

Code coverage was measured using the following commands:

```cmd
coverage erase
coverage run manage.py test planner
coverage report -m
coverage html
```

The measured project coverage reached approximately 83% during this
testing stage.

The coverage report showed that the models had strong coverage, while
some form and view branches had lower coverage.

This information helped identify areas that required additional testing
during Iteration 3.

## 6. Review of Results

The planned usability features were successfully implemented.

Search, filtering and sorting could be used together while still
restricting results to records belonging to the logged-in user.

The dashboard correctly calculated progress information from the user's
courses, assessments and study tasks.

Automated testing provided evidence that the main workflows were working
correctly and helped identify less-tested code paths.

## 7. Problems and Challenges

The main challenge was constructing task queries that could combine
multiple search and filter conditions without exposing another user's
records.

Every query still needed to include the ownership condition:

```python
owner=request.user
```

The task filters also needed to work correctly when one or more filter
fields were empty.

Another challenge was ensuring that the dashboard statistics changed
correctly after records were created, edited, completed or deleted.

## 8. Lessons Learned

Iteration 2 demonstrated that usability features such as search and
filtering require careful testing because multiple conditions can be
combined.

The iteration also showed that a coverage percentage alone is not enough.
The detailed coverage report is needed to identify which functions and
branches have not been executed.

Automated testing made later changes safer because the existing workflows
could be checked after each modification.

## 9. Changes Planned for Iteration 3

The following work was planned for Iteration 3:

- Apply test-driven development to a new feature
- Implement quick task completion
- Use mock testing for time-dependent behaviour
- Perform complete browser-based system testing
- Track defects using GitHub Issues
- Add regression tests for defects found during testing
- Prepare the final project demonstration

## 10. Iteration Outcome

Iteration 2 was completed successfully.

The system became easier to use through search, filtering, sorting and
progress summaries.

Automated testing and coverage measurement also provided a stronger
quality-assurance foundation for the final iteration.