## Project Documentation

The repository contains documentation covering the complete software
engineering process, including requirements, design, implementation,
testing, iterative development and defect tracking.

### Requirements and Research

- [Project Proposal](docs/Project_Proposal.md)
- [Initial Product Backlog](docs/Initial_Backlog.md)
- [User Interview Plan](docs/User_Interview_Plan.md)
- [Forum Research Findings](docs/Forum_Research_Findings.md)
- [Refined Product Backlog](docs/Refined_Product_Backlog.md)
- [Requirements and Product Planning](docs/Requirements.md)

### Design and Implementation

- [System Design](docs/Design.md)
- [Implementation and Delivered Solution](docs/Implementation.md)
- [Development and Building Tools](docs/Development_Tools.md)

### Iterative Development

- [Iteration 1 Review](docs/Iteration_1_Review.md)
- [Iteration 2 Test Plan](docs/Iteration_2_Test_Plan.md)
- [Iteration 2 Review](docs/Iteration_2_Review.md)
- [Iteration 3 Review](docs/Iteration_3_Review.md)

### Testing and Quality Assurance

- [Testing and Quality Assurance](docs/Testing.md)
- [System Testing Plan and Results](docs/System_Testing_Plan.md)
- [GitHub Bug Report Template](.github/ISSUE_TEMPLATE/bug_report.md)

## Development Summary

The project was completed through three agile iterations.

### Iteration 1

Iteration 1 delivered the core application:

- User registration
- Login and logout
- Course management
- Assessment management
- Study-task management
- Initial dashboard
- Personal data ownership

### Iteration 2

Iteration 2 improved usability and automated testing:

- Task search
- Course, priority and status filtering
- Task sorting
- Dashboard progress summaries
- Automated tests
- Code-coverage measurement

### Iteration 3

Iteration 3 focused on quality assurance:

- Test-driven development
- Quick Mark complete
- Mock testing
- System testing
- GitHub defect tracking
- Regression testing
- Final demonstration

## Testing Summary

The final automated test suite contains nineteen tests.

Run the complete suite using:

```cmd
python manage.py test planner -v 2
```

Final result:

```text
Ran 19 tests
OK
```

The project also includes twelve browser-based system tests covering
authentication, CRUD workflows, validation, search, filtering, status
management, dashboard updates and user-data isolation.

One defect was identified during system testing:

- GitHub Issue #15: Editing a completed task caused a NameError.

The defect was fixed, protected by a regression test, successfully
retested and closed.

## GitHub Repository

Repository:

https://github.com/ZhangDawei-14833577/CP3407-Student-Planner

The repository contains the source code, Git history, user-story Issues,
Project Board evidence, testing documentation and defect-resolution
records.