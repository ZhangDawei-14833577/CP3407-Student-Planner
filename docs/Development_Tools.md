# Development and Building Tools

## 1. Overview

The Student Assignment and Study Planner was developed using a
combination of modern programming frameworks, software libraries,
development tools, testing tools and project-management services.

These tools supported source-code development, database management,
graphical user-interface implementation, automated testing, version
control and agile project tracking.

## 2. Python

Python was used as the main programming language for the server-side
application.

It was used to implement:

- Django models
- Forms and validation
- Views and request handling
- URL configuration
- Business rules
- Automated tests
- Database migrations

Python was selected because it provides clear syntax, extensive library
support and strong integration with Django.

The Python version used during development was Python 3.13.

## 3. Django

Django was used as the main web-development framework.

The project used Django for:

- User registration
- User authentication
- Login and logout
- URL routing
- Database models
- Model forms
- Input validation
- Template rendering
- User messages
- Access control
- Automated testing
- Database migrations

Django reduced the amount of repeated infrastructure code required for
authentication, form handling and database access.

The project used Django's Model-View-Template architecture to separate
data, request handling and interface presentation.

## 4. Django ORM

Django's Object-Relational Mapper was used to communicate with the
relational database.

The ORM was used to:

- Create database tables from models
- Define foreign-key relationships
- Query user-owned records
- Create, update and delete data
- Apply database migrations
- Enforce model constraints
- Retrieve related Course, Assessment and StudyTask records

Using the ORM reduced the need to write repeated SQL statements.

For example, ownership filtering was implemented through queries that
included:

```python
owner=request.user
```

This supported personal data isolation.

## 5. SQLite

SQLite was used as the project's relational database.

The database stores:

- User accounts
- Courses
- Assessments
- Study tasks
- Priorities
- Status values
- Start dates
- Due dates
- Estimated study hours
- Task-completion timestamps

SQLite was suitable for the project because:

- It is integrated with Django
- It requires no separate database server
- It supports relational tables and foreign keys
- It is appropriate for local development and demonstration
- It allows the project to be started quickly on another computer

The database file is:

```text
db.sqlite3
```

SQLite was used for development and demonstration. A larger production
deployment could later migrate to PostgreSQL or MySQL.

## 6. HTML and Django Templates

HTML was used to define the structure of the graphical web interface.

Django Template Language was used to:

- Display database records
- Generate navigation links
- Display form fields
- Display validation messages
- Show different content based on authentication status
- Iterate through courses, assessments and tasks
- Display status and priority information
- Generate edit, delete and completion actions

Templates were separated from the Python request-handling code.

## 7. CSS and Bootstrap

Bootstrap and custom CSS were used to create a consistent graphical user
interface.

Bootstrap components were used for:

- Navigation bars
- Buttons
- Forms
- Tables
- Cards
- Alert messages
- Responsive containers
- Status displays
- Dashboard layouts

Bootstrap helped maintain consistent spacing, typography and interface
behaviour across the application.

The final interface includes separate pages for:

- Registration and login
- Dashboard
- Courses
- Assessments
- Study tasks
- Create, edit and delete forms

## 8. Visual Studio Code

Visual Studio Code was used as the primary development environment.

It was used for:

- Editing Python files
- Editing HTML templates
- Editing Markdown documentation
- Viewing the project directory structure
- Running CMD and terminal commands
- Viewing Git file status
- Selecting the Python virtual environment
- Previewing Markdown documentation
- Locating syntax and import errors

VS Code extensions supported Python development and Markdown preview.

## 9. Python Virtual Environment

A Python virtual environment was created in:

```text
.venv
```

The virtual environment isolated the project's Python packages from
packages installed globally on the computer.

It was activated using:

```cmd
.venv\Scripts\activate.bat
```

This reduced dependency conflicts and helped maintain a consistent
development environment.

## 10. pip and requirements.txt

`pip` was used to install Python packages.

The required project dependencies were recorded in:

```text
requirements.txt
```

This file supports reproducible project setup because another developer
can install the recorded packages using:

```cmd
pip install -r requirements.txt
```

## 11. Django Migration Tools

Django migration commands were used to create and update the database
structure.

The main commands included:

```cmd
python manage.py makemigrations
python manage.py migrate
python manage.py migrate --check
```

Migration files preserved changes to the Course, Assessment and
StudyTask models.

## 12. Django Development Server

The application was run locally using Django's development server.

The command was:

```cmd
python manage.py runserver
```

The application was then accessed through:

```text
http://127.0.0.1:8000/
```

The development server was used for implementation, manual testing and
the final classroom demonstration.

## 13. Git

Git was used for local version control.

Git recorded changes to:

- Source code
- Templates
- Tests
- Documentation
- Database migrations
- Configuration files

Common commands included:

```cmd
git status
git add
git commit
git log
git push
```

Git allowed earlier development states to remain visible and provided a
record of changes completed during each iteration.

## 14. GitHub Repository

GitHub was used to host the project's source code and documentation.

The repository contains:

- Django source code
- HTML templates
- Automated tests
- Migration files
- Requirements file
- README documentation
- Design documentation
- Testing documentation
- Iteration reviews
- System testing evidence

The public repository also allowed the instructors to review the project.

## 15. GitHub Issues

GitHub Issues were used to manage:

- User stories
- Feature requirements
- Defects
- Bug-resolution evidence
- Retest results

GitHub Issue #15 was created after system testing identified a
NameError when a completed task was changed back to In Progress.

The Issue preserved the complete defect history from discovery to
closure.

## 16. GitHub Projects

GitHub Projects was used as the agile iteration board.

Items were tracked using the following statuses:

```text
Todo
In Progress
Done
```

The Project Board was used to:

- Organise user stories
- Track implementation progress
- Record completed work
- Connect Issues with project status
- Provide visible evidence of iterative development

The instructors were provided access to the private Project Board.

## 17. Django TestCase

Django's `TestCase` framework was used for automated testing.

The tests verified:

- Authentication
- Course management
- Assessment management
- Study-task management
- Validation
- Search
- Filtering
- Sorting
- User-data ownership
- Task completion
- Regression behaviour

The final automated test suite contained nineteen passing tests.

## 18. unittest.mock

`unittest.mock.patch` was used to test time-dependent task-completion
behaviour.

The real current time was replaced with a fixed test value.

This allowed the test to verify the exact value stored in the
`completed_at` field.

Mocking made the test repeatable and independent of the time at which it
was executed.

## 19. coverage.py

`coverage.py` was used to measure which Python statements were executed
by the automated test suite.

The commands included:

```cmd
coverage erase
coverage run manage.py test planner
coverage report -m
coverage html
```

The HTML coverage report was generated in:

```text
htmlcov
```

The measured coverage reached approximately 83% during the automated
testing stage.

Coverage information helped identify less-tested form and view paths.

## 20. Markdown

Markdown was used to write project documentation.

The documentation includes:

- Project proposal
- Initial backlog
- Refined product backlog
- User interview plan
- Forum research findings
- Requirements documentation
- System design
- Iteration reviews
- Testing documentation
- System testing plan
- Development-tools documentation

Markdown files can be displayed directly on GitHub, making the project
process accessible to instructors.

## 21. Diagram and Interface Documentation Tools

Architecture, database and interface diagrams were included in the
system-design documentation.

The diagrams document:

- Django application architecture
- Database entities and relationships
- Main user-interface screens

The image files are stored in:

```text
docs/images
```

They are referenced from:

```text
docs/Design.md
```

## 22. Tool Integration

The tools were not used independently. They formed a connected
development workflow.

```text
VS Code
→ Python and Django development
→ SQLite database and migrations
→ Django automated tests
→ coverage.py analysis
→ Git commits
→ GitHub repository
→ GitHub Issues and Project Board
→ Markdown documentation
```

This workflow supported implementation, testing, defect correction,
documentation and iterative project management.

## 23. Benefits and Limitations

The selected tools provided several benefits:

- Django accelerated web development
- SQLite simplified local database setup
- Bootstrap improved interface consistency
- Git preserved the development history
- GitHub supported collaboration and defect tracking
- Automated testing reduced regression risk
- Coverage measurement identified untested code
- Markdown made technical evidence easy to review

The main limitation was that the final application was run locally using
Django's development server rather than a public production server.

For a future production version, the project could use:

- PostgreSQL or MySQL
- A production WSGI or ASGI server
- Environment-variable configuration
- Automated deployment
- Continuous integration
- Automated browser testing

## 24. Conclusion

The project used modern development frameworks, libraries and project
management tools throughout its three iterations.

The selected tools supported the complete software-engineering process:

```text
Requirements
→ Design
→ Implementation
→ Testing
→ Defect correction
→ Version control
→ Demonstration
→ Documentation
```

The combination of Django, SQLite, Bootstrap, GitHub, automated tests,
mock testing and code-coverage measurement provided a suitable
development environment for the Student Assignment and Study Planner.