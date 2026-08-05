# Requirements and Product Planning

## 1. Project Purpose

The Student Assignment and Study Planner was developed to help
university students manage courses, assessments, academic deadlines and
smaller study tasks.

The requirements were refined before and during development using user
research, backlog review, implementation feedback and system testing.

## 2. Requirement Sources

The project requirements were identified and refined using:

- Project proposal
- Initial product backlog
- Student interview plan
- Forum research findings
- Refined product backlog
- GitHub user-story issues
- Feedback obtained during development and testing

## 3. Prioritisation Method

Requirements were prioritised according to:

1. Dependency on other features
2. Importance to the main student-planning workflow
3. User value
4. Implementation risk
5. Available development time

Authentication and the three core record-management features were given
high priority because the remaining features depended on them.

Search, filtering and progress summaries were implemented after the core
CRUD workflows were stable.

Testing, defect tracking and quick task completion were completed during
the final iteration.

## 4. Prioritised User Stories

| ID | User Story | Priority | Estimate | Planned Iteration | Final Result |
|---|---|---|---:|---:|---|
| US-01 | User registration | High | 3 | 1 | Completed |
| US-02 | User login and logout | High | 3 | 1 | Completed |
| US-03 | Course management | High | 5 | 1 | Completed |
| US-05 | Assessment management | High | 5 | 1 | Completed |
| US-06 | Study-task management | High | 8 | 1 | Completed |
| US-09 | Search, filtering and sorting | Medium | 5 | 2 | Completed |
| US-10 | Personal data ownership | High | 5 | 1 | Completed |
| US-12 | Dashboard progress summary | Medium | 5 | 2 | Completed |
| US-13 | Quick task completion | Medium | 3 | 3 | Completed |

## 5. Implementation Order

The implementation order was selected according to feature
dependencies.

1. Authentication was implemented first so that records could be linked
   to individual users.
2. Course management was implemented before assessments and tasks.
3. Assessment management was implemented after the Course model was
   available.
4. Study-task management was implemented after the related Course and
   Assessment structures were stable.
5. Search, filtering and progress summaries were added after the core
   data-management workflows worked correctly.
6. TDD, system testing and bug tracking were used in the final iteration
   to improve software quality.

## 6. Acceptance Criteria Summary

The main acceptance criteria included:

- A user can register, log in and log out.
- A user can create, view, edit and delete courses.
- A user can create, view, edit and delete assessments.
- A user can divide academic work into study tasks.
- Invalid dates and incompatible relationships are rejected.
- Tasks can be searched, filtered and sorted.
- Task progress appears on the dashboard.
- A user cannot access another user's records.
- A task can be marked as completed.
- Completed tasks can be changed back to an unfinished status.

## 7. Requirement Outcome

All high-priority core requirements were completed.

The selected medium-priority usability and progress-tracking features
were also completed within the three planned iterations.

Future enhancements such as email reminders, calendar integration and
public deployment were excluded from the final development scope because
the core planner and testing requirements had higher priority.