# Refined Product Backlog

## Project

Student Assignment and Study Planner

## Priority Convention

The project uses the following priority scale:

- 50 — Critical: Required for the core application
- 40 — High: Important for normal use
- 30 — Medium: Useful but not required for the first working version
- 20 — Low: Implemented only after core features
- 10 — Optional: Extension feature

Higher numbers represent higher priority.

## Effort Estimation

Effort is estimated in individual development days.

One development day represents approximately four to six hours of
focused development, testing and documentation work.

## Refined User Stories

| ID | Title | User Story | Priority | Estimated Effort |
|---|---|---|---:|---:|
| US-01 | User Registration | As a university student, I want to create an account so that I can securely store my academic planning information. | 40 | 0.5 day |
| US-02 | User Login and Logout | As a registered student, I want to log in and log out so that my information remains private. | 50 | 0.5 day |
| US-03 | Course Management | As a student, I want to create, view, edit and delete courses so that I can organise academic work by subject. | 50 | 1 day |
| US-04 | Course Colour and Archive | As a student, I want to assign colours and archive inactive courses so that courses are visually organised without permanently deleting old information. | 30 | 0.5 day |
| US-05 | Assessment Management | As a student, I want to create, view, edit and delete assignments and examinations so that I can track academic deadlines. | 50 | 1.5 days |
| US-06 | Study Task Management | As a student, I want to create smaller study tasks linked to a course or assessment so that large assignments become easier to complete. | 50 | 1.5 days |
| US-07 | Priority, Status and Overdue Detection | As a student, I want to assign priorities and statuses to tasks and clearly see overdue work so that I can decide what to complete next. | 50 | 1 day |
| US-08 | Student Dashboard | As a student, I want a dashboard showing work due today, this week, upcoming assessments and overdue tasks so that I can understand my current workload. | 50 | 1.5 days |
| US-09 | Search, Filter and Sort | As a student, I want to filter and sort tasks by course, due date, priority and status so that I can quickly find relevant work. | 40 | 1 day |
| US-10 | Personal Data Ownership | As a student, I want to access only my own courses, assessments and tasks so that other users cannot view or modify my information. | 50 | 1 day |
| US-11 | Assessment Weighting and Effort | As a student, I want to record assessment weighting and estimated task effort so that I can plan work according to value and workload. | 30 | 0.5 day |
| US-12 | Progress Summary | As a student, I want to see basic completed, unfinished and overdue task statistics so that I can monitor my progress. | 20 | 0.75 day |
| US-13 | Configurable Reminders | As a student, I want to configure reminders before deadlines so that I receive advance notice of important work. | 10 | 2 days |
| US-14 | Weekly Calendar View | As a student, I want to view tasks and assessments in a weekly calendar so that I can identify workload conflicts. | 10 | 2 days |

## Acceptance Criteria

### US-01: User Registration

- A visitor can open a registration page.
- A visitor can create an account with a unique username.
- Invalid or duplicate information displays an error.
- A successful registration allows the user to log in.

### US-02: User Login and Logout

- A registered user can log in using valid credentials.
- Invalid credentials display an error.
- An authenticated user can log out.
- Protected pages redirect unauthenticated visitors to the login page.

### US-03: Course Management

- A user can add a course code and course name.
- A user can view their courses.
- A user can edit their own courses.
- A user can delete their own courses.
- A user cannot view another user's courses.

### US-05: Assessment Management

- A user can create an assignment or examination.
- Each assessment is connected to a course.
- An assessment can contain a title, type, start date and due date.
- A user can edit and delete their own assessments.
- Invalid dates display a validation error.

### US-06: Study Task Management

- A user can create a task.
- A task can be connected to a course.
- A task may also be connected to an assessment.
- A user can edit and delete their own tasks.
- A task can contain a title, due date and notes.

### US-07: Priority, Status and Overdue Detection

- A task supports high, medium and low priority.
- A task supports to-do, in-progress and completed statuses.
- A task past its due date is displayed as overdue.
- Completed tasks are not displayed as overdue.

### US-08: Student Dashboard

- The dashboard displays tasks due today.
- The dashboard displays tasks due during the next seven days.
- The dashboard displays overdue tasks.
- The dashboard displays upcoming assessments.
- Dashboard information only belongs to the logged-in user.

### US-09: Search, Filter and Sort

- Tasks can be filtered by course.
- Tasks can be filtered by status.
- Tasks can be filtered by priority.
- Tasks can be sorted by due date.

### US-10: Personal Data Ownership

- Every course belongs to one user.
- Every assessment belongs to one user.
- Every task belongs to one user.
- Users cannot access another user's records by changing a URL.

## Implementation Order

### Iteration 1 — Foundation

1. US-02 User Login and Logout
2. US-01 User Registration
3. US-10 Personal Data Ownership
4. US-03 Course Management
5. US-04 Course Colour and Archive

### Iteration 2 — Academic Planning

1. US-05 Assessment Management
2. US-06 Study Task Management
3. US-07 Priority, Status and Overdue Detection
4. US-11 Assessment Weighting and Effort

### Iteration 3 — Usability and Reporting

1. US-08 Student Dashboard
2. US-09 Search, Filter and Sort
3. US-12 Progress Summary
4. Automated testing and interface refinement

### Optional Extensions

1. US-13 Configurable Reminders
2. US-14 Weekly Calendar View

## Scope Decision

The first working version will focus on US-01 to US-10.

US-11 and US-12 will be implemented after the core workflow is stable.

US-13 and US-14 are optional because reminders and calendar interfaces
require additional development and testing effort.