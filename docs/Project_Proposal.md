# Project Proposal

## Project Title

Student Assignment and Study Planner

## 1. Project Overview

The purpose of this project is to develop a web-based assignment and
study planning application for university students.

University students are required to manage multiple courses,
assignments, examinations, practical activities and personal study
tasks. This information may be distributed across learning management
systems, emails, calendars and handwritten notes. As a result, students
may find it difficult to maintain a clear overview of their academic
responsibilities.

The proposed application will provide a centralised system where
students can record their courses, assessments, deadlines and study
tasks. It will also allow users to prioritise work, update task status
and view an overview of upcoming academic activities.

The system will be developed as a database-driven web application using
Django, Bootstrap and a relational database.

## 2. Problem Statement

Students frequently manage academic deadlines using several unrelated
tools. This can result in:

- Missing or overlooking assessment deadlines
- Difficulty identifying high-priority work
- Inconsistent study planning
- Limited visibility of completed and unfinished tasks
- Duplication of academic information across different applications

The project will address these problems by providing one structured
application for managing academic information.

## 3. Target Users

The primary target users are university students who study multiple
subjects and need to manage assessments, examinations, study tasks and
deadlines.

Potential target users include:

- Undergraduate students
- Postgraduate students
- International students
- Students completing multiple concurrent subjects

## 4. Project Objectives

The objectives of the project are to:

1. Develop a secure web application with user registration and login.
2. Allow students to create and manage their courses.
3. Allow students to record assessments and examination dates.
4. Allow students to create study tasks associated with courses.
5. Support task priorities, due dates and completion status.
6. Provide filtering and sorting of academic tasks.
7. Provide a dashboard containing upcoming and completed work.
8. Store project data in a relational database.
9. Apply Agile iterative development throughout the project.
10. Develop and document appropriate automated tests.

## 5. Planned Features

### 5.1 User Account Management

- Register a new account
- Log in to the application
- Log out securely
- View and update basic account information

### 5.2 Course Management

- Add a course
- View existing courses
- Edit course information
- Delete a course

### 5.3 Assessment Management

- Add an assignment or examination
- Record the assessment title
- Select the related course
- Record the due date
- Record the assessment type
- Edit or delete assessment information

### 5.4 Study Task Management

- Create study tasks
- Associate tasks with courses or assessments
- Assign due dates
- Assign priorities
- Update task status
- Mark tasks as completed

### 5.5 Dashboard

- Display upcoming assessments
- Display overdue tasks
- Display high-priority tasks
- Display recently completed tasks
- Summarise academic progress

### 5.6 Search and Filtering

- Filter tasks by course
- Filter tasks by completion status
- Filter tasks by priority
- Sort tasks by due date

## 6. Technology Stack

### Backend

- Python 3.13
- Django 5.2

### Frontend

- HTML
- CSS
- Bootstrap 5
- JavaScript

### Database

- SQLite during initial development
- MySQL planned for the final application

### Testing

- Django TestCase
- Python unittest
- Coverage.py

### Software Engineering Tools

- Git and GitHub for version control
- GitHub Issues for task tracking
- GitHub Projects for the project board
- Visual Studio Code for development
- Online UML and database diagram tools for design documentation

## 7. Development Approach

The project will follow an iterative Agile development process.

The work will be divided into three main iterations:

### Iteration 1

- User account functionality
- Initial course management
- Initial user interface
- Basic database models

### Iteration 2

- Assessment management
- Study task management
- Filtering and priorities
- Automated testing

### Iteration 3

- Dashboard
- Progress summaries
- Interface improvements
- Additional testing and deployment preparation

The backlog may be updated after user interviews, testing and feedback.

## 8. Data and Privacy

The application will store user account information and academic
planning data.

The project will apply the following principles:

- Passwords will be processed using Django's authentication system.
- Passwords will not be stored as plain text.
- Users will only be able to access their own academic data.
- Development passwords and secret values will not be committed to GitHub.
- Personally identifiable information will be kept to the minimum required.
- Test data will be used during development instead of real confidential data.

## 9. Project Scope

### Included in the Core Scope

- Authentication
- Course management
- Assessment management
- Study task management
- Priorities and due dates
- Completion tracking
- Search and filtering
- Dashboard
- Relational database
- Automated testing

### Possible Extension Features

These features will only be considered if the core project is completed:

- Weekly study schedule
- Progress charts
- Dark mode
- Data export
- Email reminders

### Out of Scope

The following features are not currently planned:

- Real-time chat
- Online payment
- Complex artificial intelligence features
- Mobile push notifications
- Multi-user collaborative editing
- Direct integration with university systems

## 10. Expected Outcome

The expected outcome is a functional and documented web application
that demonstrates requirements analysis, software design, database
development, implementation, testing, version control and Agile
software engineering.