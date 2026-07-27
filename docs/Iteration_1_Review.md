# Iteration 1 Review

## Project

Student Assignment and Study Planner

## Iteration Period

Weeks 3–5

## Iteration Objective

The objective of Iteration 1 was to establish the application's core
technical foundation and implement the main academic planning workflow.

The iteration focused on authentication, user data ownership, course
management, assessment management, study task management and the
student dashboard.

## Completed User Stories

| ID | User Story | Estimated Effort | Status |
|---|---|---:|---|
| US-01 | User Registration | 0.5 day | Completed |
| US-02 | User Login and Logout | 0.5 day | Completed |
| US-03 | Course Management | 1.0 day | Completed |
| US-04 | Course Colour and Archive | 0.5 day | Completed |
| US-05 | Assessment Management | 1.5 days | Completed |
| US-06 | Study Task Management | 1.5 days | Completed |
| US-07 | Priority, Status and Overdue Detection | 1.0 day | Completed |
| US-08 | Student Dashboard | 1.5 days | Completed |
| US-10 | Personal Data Ownership | 1.0 day | Completed |

## Partially Completed User Stories

| ID | User Story | Estimated Effort | Current Status |
|---|---|---:|---|
| US-09 | Search, Filter and Sort | 1.0 day | In Progress |

Filtering by course, task status and task priority has been implemented.

A selectable sorting interface has not yet been implemented. Tasks are
currently sorted automatically by due date and title.

## Unfinished User Stories

| ID | User Story | Status |
|---|---|---|
| US-11 | Assessment Weighting and Estimated Effort | Partially implemented |
| US-12 | Progress Summary | Backlog |
| US-13 | Configurable Reminders | Optional backlog |
| US-14 | Weekly Calendar View | Optional backlog |

Assessment weighting and estimated task effort are stored by the
application, but additional reporting and interface improvements may
still be required.

## Iteration Velocity

Velocity is calculated using the estimated development effort of fully
completed user stories.

Completed effort:

- US-01: 0.5 day
- US-02: 0.5 day
- US-03: 1.0 day
- US-04: 0.5 day
- US-05: 1.5 days
- US-06: 1.5 days
- US-07: 1.0 day
- US-08: 1.5 days
- US-10: 1.0 day

**Actual Iteration 1 velocity: 9.0 estimated development days**

Partially completed stories are not included in the velocity.

## Delivered Functionality

Iteration 1 delivered:

- User registration
- User login and logout
- Protected application pages
- User-specific data ownership
- Course CRUD operations
- Course colour and archive status
- Assessment CRUD operations
- Study task CRUD operations
- Task priorities and statuses
- Overdue detection
- Task filtering
- Student dashboard
- Django administration interface
- Relational database models
- Git and GitHub version control

## SRP Review

The project was reviewed against the Single Responsibility Principle.

### Positive Findings

- Models define database structures and domain validation.
- Forms validate user input and restrict selectable records.
- Views handle requests, responses and navigation.
- Templates handle presentation.
- URLs define application routing.

### Refactoring Completed

Task completion timestamp logic was moved from the view layer into the
StudyTask model.

This change places task-status business logic inside the class that owns
the relevant data.

### Future SRP Improvement

The views.py file now contains authentication, dashboard, course,
assessment and study-task views.

As the project grows, these views may be separated into smaller modules:

- views_auth.py
- views_dashboard.py
- views_courses.py
- views_assessments.py
- views_tasks.py

This refactoring is deferred until the current functionality is covered
by automated tests.

## DRY Review

Several repeated patterns were identified:

- Create and update views use similar form-processing logic.
- Course, assessment and task forms repeat some Bootstrap widget setup.
- Delete views use similar confirmation and redirect logic.
- Form templates use similar field-rendering structures.

These areas could be reduced using class-based views, shared form
helpers or reusable template includes.

Large structural changes were not made during this review because
automated test coverage is not yet available. Avoiding risky
refactoring before testing reduces the chance of introducing defects.

## Defects and Issues Found

The following issues occurred during Iteration 1:

- Missing planner URL configuration
- Missing template files
- Incorrect template directory structure
- Missing AssessmentForm import
- HTML editor warnings caused by Django template variables

All blocking issues were corrected.

## Iteration Outcome

Iteration 1 successfully delivered a functional academic-planning
workflow:

Course → Assessment → Study Task

The application now provides a usable foundation for testing,
refactoring and future interface improvements.

## Iteration 2 Priorities

Iteration 2 will focus on:

1. Completing search, filtering and sorting
2. Improving the dashboard and progress summary
3. Adding automated tests
4. Measuring test coverage
5. Reviewing SRP and DRY with test protection
6. Improving interface usability