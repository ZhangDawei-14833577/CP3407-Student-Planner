# Implementation and Delivered Solution

## 1. Implementation Overview

The Student Assignment and Study Planner is a Django web application
developed to help university students organise courses, assessments,
deadlines and smaller study tasks.

The final application provides a graphical browser-based interface and a
relational database.

The system was developed through three iterations. Each iteration
delivered a working improvement to the previous version.

## 2. Delivered Core Features

The final application includes:

- User registration
- User login and logout
- Authentication-protected pages
- Course creation, viewing, editing and deletion
- Assessment creation, viewing, editing and deletion
- Study-task creation, viewing, editing and deletion
- Course, assessment and task ownership
- Task priorities
- Task statuses
- Start dates and due dates
- Estimated study hours
- Overdue-task detection
- Search
- Filtering
- Sorting
- Dashboard progress summaries
- Quick task completion
- Input validation
- User-data isolation
- Automated testing
- System testing
- GitHub defect tracking

## 3. User Authentication

Django's authentication framework was used to manage user accounts.

The authentication workflow includes:

- User registration
- Login
- Logout
- Authentication checks
- Redirecting unauthenticated users to the login page
- Displaying the logged-in username
- Restricting application pages to authenticated users

Protected views use Django's authentication controls, including:

```python
@login_required
```

Each academic record is associated with its owner.

This ensures that records created by one student are not displayed to
another student.

## 4. Course Management

Course management was implemented as the first main academic-record
feature.

A user can:

- Create a course
- View a list of their courses
- Edit a course
- Delete a course
- Assign a course code
- Assign a course name
- Add a description
- Select a display colour
- Mark a course as archived

A uniqueness rule prevents the same user from creating two courses with
the same course code.

Course records provide the foundation for assessments and study tasks.

## 5. Assessment Management

Assessment management allows users to record major academic requirements.

A user can:

- Create an assessment
- Select its course
- Enter a title
- Select an assessment type
- Select a status
- Record a start date
- Record a due date
- Record a weighting
- Add notes
- Edit an assessment
- Delete an assessment

Validation prevents an assessment start date from being later than its
due date.

Each assessment belongs to:

- One user
- One course

The ownership and course relationships are checked before the record is
saved.

## 6. Study-Task Management

Study tasks allow a large assessment or study goal to be divided into
smaller actions.

A user can:

- Create a task
- Select a course
- Optionally select an assessment
- Add a title
- Add a description
- Select a priority
- Select a status
- Record start and due dates
- Record estimated study hours
- Edit the task
- Delete the task
- Mark the task as completed

The available task statuses are:

```text
To Do
In Progress
Completed
```

The available priorities include:

```text
Low
Medium
High
```

Validation ensures that a selected assessment belongs to the selected
course.

## 7. Quick Task Completion

A quick Mark complete function was implemented during Iteration 3.

This allows the user to complete a task directly from the task list
without opening the full edit form.

When the action is used:

- The task status becomes Completed
- A completion timestamp is recorded
- The task is no longer treated as overdue
- Dashboard completion statistics are updated
- The Mark complete action is removed for that task

Completion-state logic is maintained in the `StudyTask` model using:

```python
sync_completion_time()
```

Keeping this logic in the model avoids duplicating it across different
views.

## 8. Search, Filtering and Sorting

Task search, filtering and sorting were implemented during Iteration 2.

Users can search tasks using keywords.

Tasks can be filtered by:

- Course
- Priority
- Status

Tasks can be sorted by:

- Title from A to Z
- Title from Z to A
- Earliest due date
- Latest due date

The search and filtering options can be combined.

All queries remain restricted to:

```python
owner=request.user
```

This prevents search results from exposing another user's records.

## 9. Dashboard

The dashboard provides a summary of the currently logged-in user's
academic data.

It displays:

- Active course count
- Total study-task count
- Completed task count
- Overdue task count
- Task-completion percentage
- To Do task count
- In Progress task count
- Completed task count
- Total assessment count
- Upcoming assessment count
- Completed assessment count
- Tasks due today
- Tasks due within the next seven days
- Overdue tasks
- Upcoming assessments

The values are calculated from current database records.

When a task is created, edited, completed or deleted, the dashboard
statistics update accordingly.

## 10. Validation

Validation was implemented at the model and form levels.

The main validation rules include:

### 10.1 Duplicate Course Code

A user cannot create two courses using the same course code.

### 10.2 Assessment Date Order

An assessment start date cannot be later than its due date.

### 10.3 Task Date Order

A task start date cannot be later than its due date.

### 10.4 Course and Assessment Relationship

A task cannot be connected to an assessment that belongs to a different
course.

### 10.5 Ownership Validation

Courses, assessments and study tasks must belong to the logged-in user.

Validation messages are displayed through the graphical form interface.

## 11. Personal Data Isolation

Personal data isolation was implemented throughout the application.

Queries retrieve records using both:

- The record identifier
- The currently logged-in user

For example, protected record retrieval follows the principle:

```python
get_object_or_404(
    Course,
    pk=course_id,
    owner=request.user,
)
```

As a result:

- User A cannot see User B's courses
- User A cannot see User B's assessments
- User A cannot see User B's tasks
- User A cannot edit User B's records
- User A cannot delete User B's records
- Direct access to another user's record URL returns a 404 response

The 404 response is intentional because the record is not available to
the current user.

## 12. Application Architecture

The application follows Django's Model-View-Template structure.

### Models

Models define:

- Database fields
- Relationships
- Status choices
- Priority choices
- Constraints
- Business rules
- Completion behaviour

The main models are:

```text
Course
Assessment
StudyTask
```

### Forms

Forms are responsible for:

- Collecting user input
- Displaying fields
- Filtering available Course and Assessment choices
- Validating dates
- Validating ownership
- Validating relationships
- Displaying error messages

### Views

Views are responsible for:

- Receiving HTTP requests
- Checking authentication
- Filtering records by owner
- Processing forms
- Saving valid data
- Displaying success messages
- Redirecting users
- Rendering templates

### Templates

Templates are responsible for:

- Navigation
- Forms
- Tables
- Dashboard cards
- Buttons
- Status labels
- Search controls
- Filter controls
- Delete confirmations
- User messages

### URL Configuration

URL configuration connects browser addresses to the correct views.

The project uses:

```text
config/urls.py
planner/urls.py
```

## 13. Database Implementation

SQLite was used as the relational database through Django's ORM.

The main relationships are:

```text
User 1 → many Courses
User 1 → many Assessments
User 1 → many StudyTasks

Course 1 → many Assessments
Course 1 → many StudyTasks

Assessment 1 → many StudyTasks
```

The Assessment relationship on a StudyTask is optional.

The database design supports:

- Foreign-key relationships
- User ownership
- Data validation
- Migrations
- Related-object queries
- Data isolation

The database file is:

```text
db.sqlite3
```

SQLite was selected because it is reliable for local development,
requires no separate database server and integrates directly with
Django.

For a larger production deployment, the ORM would allow migration to
PostgreSQL or MySQL.

## 14. Graphical User Interface

The application uses HTML, Django templates, Bootstrap and custom CSS.

The interface includes:

- A consistent navigation bar
- Registration and login forms
- Dashboard cards
- Data tables
- Create and edit forms
- Delete-confirmation pages
- Search and filter controls
- Status displays
- Priority displays
- Success and validation messages

The main navigation links are:

```text
Dashboard
Courses
Assessments
Tasks
```

Bootstrap was selected because it provides reusable interface components
and consistent visual presentation.

## 15. Iteration 1 Delivery

Iteration 1 established the core working application.

The delivered features included:

- Project proposal
- Initial product backlog
- User interview plan
- Forum research
- Refined product backlog
- Django project structure
- Database models
- User registration
- Login and logout
- Course management
- Assessment management
- Study-task management
- Initial dashboard
- User ownership controls

At the end of Iteration 1, a user could register, log in and manage their
main academic records.

The Iteration 1 result was documented in:

```text
docs/Iteration_1_Review.md
```

## 16. Iteration 2 Delivery

Iteration 2 improved usability and automated quality verification.

The delivered features included:

- Task keyword search
- Course filtering
- Priority filtering
- Status filtering
- Title sorting
- Due-date sorting
- Clear-filter behaviour
- Improved dashboard summaries
- Automated tests
- Code-coverage measurement

The test suite reached approximately fifteen automated tests during this
stage.

Measured code coverage reached approximately 83%.

The Iteration 2 result was documented in:

```text
docs/Iteration_2_Review.md
```

## 17. Iteration 3 Delivery

Iteration 3 focused on final feature work and quality assurance.

The delivered work included:

- Quick Mark complete
- Test-driven development
- Mock testing
- System testing plan
- Twelve system test cases
- GitHub Bug Issue template
- GitHub defect tracking
- Bug #15 correction
- Regression testing
- Final nineteen-test suite
- Final classroom demonstration

The Iteration 3 result was documented in:

```text
docs/Iteration_3_Review.md
```

## 18. Defect Correction

During system testing, changing a completed task back to In Progress
caused a NameError.

The obsolete code was:

```python
_update_task_completion_time(task)
```

It was replaced with:

```python
task.sync_completion_time()
```

A regression test was added.

The corrected workflow was:

```text
Completed task
→ Edit
→ Change to In Progress
→ Save successfully
```

The defect was recorded as GitHub Issue #15, retested and closed.

## 19. Automated Testing Result

The final automated test suite contained nineteen tests.

It can be executed using:

```cmd
python manage.py test planner -v 2
```

The final result was:

```text
Ran 19 tests
OK
```

The automated tests cover authentication, CRUD workflows, validation,
search, filtering, sorting, ownership and task completion.

## 20. System Testing Result

Twelve system test cases were executed through the graphical interface.

The system tests covered the complete user workflow from registration to
data isolation.

One defect was identified, fixed and retested.

The final system-testing result was Pass.

The complete plan and results are documented in:

```text
docs/System_Testing_Plan.md
```

## 21. Version-Control Delivery

The completed solution is stored in a public GitHub repository.

Git and GitHub were used to preserve:

- Feature-development commits
- Iteration history
- Automated tests
- Documentation
- User Stories
- Bug Issues
- Regression-test evidence
- Project Board status

The instructors were added as repository collaborators and were also
given access to the private GitHub Project Board.

## 22. Local Execution and Deployment

The application was developed and demonstrated locally.

The project environment can be opened using:

```cmd
cd /d C:\Users\David\Documents\CP3407_StudentPlanner
.venv\Scripts\activate.bat
```

The database structure can be checked using:

```cmd
python manage.py migrate --check
```

The project can be checked using:

```cmd
python manage.py check
```

The automated tests can be executed using:

```cmd
python manage.py test planner -v 2
```

The application can be started using:

```cmd
python manage.py runserver
```

It can then be opened at:

```text
http://127.0.0.1:8000/
```

The application currently uses Django's development server.

It has not been deployed to a public production server.

## 23. Demonstration

The completed application was demonstrated during the Week 10 practical.

The demonstration included:

- Registration
- Login and logout
- Course management
- Assessment management
- Study-task management
- Status changes
- Search
- Filtering
- Sorting
- Dashboard updates
- Quick task completion
- Validation
- User-data isolation
- Automated tests
- GitHub Issues
- Project Board evidence

The instructor was provided repository and Project Board access after
the demonstration.

## 24. Feedback Sources

Because this was an individual classroom project, no separate commercial
client was available after every iteration.

Feedback and review evidence came from:

- Initial user-research planning
- Forum-research findings
- Backlog refinement
- Automated-test results
- Code-coverage reports
- Browser-based system testing
- Defect discovery
- Iteration reviews
- Final instructor demonstration
- Instructor access to the repository and Project Board

These sources were used to review the delivered solution and guide later
iterations.

## 25. Implementation Challenges

The main implementation challenges included:

- Configuring Django URL routing
- Creating the correct template directory structure
- Connecting forms, views and templates
- Preserving ownership restrictions
- Validating related Course and Assessment records
- Combining multiple task filters
- Updating dashboard calculations
- Managing task completion timestamps
- Increasing automated-test coverage
- Correcting Bug #15
- Maintaining clear Git commit history

These challenges were addressed through incremental development,
debugging, automated testing and system testing.

## 26. Limitations

The final implementation has several limitations:

- It runs locally rather than on a public production server
- SQLite is used instead of a production database server
- Email reminders are not implemented
- Calendar integration is not implemented
- Automated browser testing is not implemented
- Performance testing with large datasets was not performed
- The interface is primarily designed for desktop browsers
- Continuous integration is not configured

These limitations were outside the selected final project scope.

## 27. Future Improvements

Possible future improvements include:

- Email deadline reminders
- Calendar integration
- Weekly and monthly calendar views
- Mobile-interface optimisation
- Additional progress charts
- Recurring study tasks
- Public deployment
- PostgreSQL or MySQL
- Continuous integration
- Automated browser testing
- Exporting study plans
- Notification preferences

## 28. Implementation Conclusion

The project delivered a functional Django web application that satisfies
the selected core user stories.

Across three iterations, the system progressed from basic authentication
and CRUD functionality to search, progress summaries, automated testing,
TDD, system testing and defect tracking.

The final solution includes:

```text
Requirements
→ Working graphical interface
→ Relational database
→ Core academic workflows
→ Validation and access control
→ Automated and system testing
→ GitHub version control
→ Defect tracking
→ Technical documentation
```

The implementation provides a stable foundation for future deployment
and feature expansion.