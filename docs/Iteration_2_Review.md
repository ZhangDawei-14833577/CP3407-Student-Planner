# Iteration 2 Review

## 1. Iteration Objective

The objective of Iteration 2 was to improve task discovery, progress
monitoring and software quality after the core record-management
features had been completed in Iteration 1.

## 2. Planned Work

The planned work for this iteration included:

- Search study tasks using keywords
- Filter tasks by course
- Filter tasks by priority
- Filter tasks by status
- Sort tasks by title and due date
- Improve the dashboard progress summary
- Add automated tests for the main user stories
- Measure automated-test coverage

## 3. Completed Work

The search, filtering and sorting features were implemented for study
tasks.

Users can:

- Search using task titles and descriptions
- Filter tasks by course
- Filter tasks by priority
- Filter tasks by status
- Sort tasks by title
- Sort tasks by due date
- Clear all active filters

The dashboard was also improved to display:

- Total task count
- Completed task count
- Overdue task count
- Task completion percentage
- Task counts by status
- Assessment summaries
- Upcoming tasks and assessments

## 4. Testing Performed

Automated tests were added and expanded for:

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