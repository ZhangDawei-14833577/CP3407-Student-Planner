from datetime import datetime, timedelta
from unittest.mock import patch

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Assessment, Course, StudyTask


User = get_user_model()


def datetime_local(value):
    """Convert a timezone-aware datetime for datetime-local forms."""

    return timezone.localtime(value).strftime("%Y-%m-%dT%H:%M")


class AuthenticationTests(TestCase):
    """Automated tests for US-02."""

    def setUp(self):
        self.user = User.objects.create_user(
            username="student1",
            email="student1@example.com",
            password="StrongPass123!",
        )

    def test_dashboard_redirects_anonymous_user_to_login(self):
        response = self.client.get(reverse("dashboard"))

        expected_url = (
            f"{reverse('login')}?next={reverse('dashboard')}"
        )

        self.assertRedirects(response, expected_url)

    def test_valid_login_redirects_to_dashboard(self):
        response = self.client.post(
            reverse("login"),
            {
                "username": "student1",
                "password": "StrongPass123!",
            },
        )

        self.assertRedirects(response, reverse("dashboard"))

    def test_logout_redirects_to_login(self):
        self.client.login(
            username="student1",
            password="StrongPass123!",
        )

        response = self.client.post(reverse("logout"))

        self.assertRedirects(response, reverse("login"))


class CourseManagementTests(TestCase):
    """Automated tests for US-03."""

    def setUp(self):
        self.user = User.objects.create_user(
            username="student1",
            password="StrongPass123!",
        )
        self.other_user = User.objects.create_user(
            username="student2",
            password="StrongPass123!",
        )

        self.client.login(
            username="student1",
            password="StrongPass123!",
        )

    def test_user_can_create_course(self):
        response = self.client.post(
            reverse("course_create"),
            {
                "code": "CP3501",
                "name": "Data Science",
                "color": "#0D6EFD",
                "description": "Data science subject",
            },
        )

        self.assertRedirects(response, reverse("course_list"))

        course = Course.objects.get(
            owner=self.user,
            code="CP3501",
        )

        self.assertEqual(course.name, "Data Science")
        self.assertFalse(course.is_archived)

    def test_duplicate_course_code_is_rejected(self):
        Course.objects.create(
            owner=self.user,
            code="CP3501",
            name="Data Science",
            color="#0D6EFD",
        )

        response = self.client.post(
            reverse("course_create"),
            {
                "code": "cp3501",
                "name": "Duplicate Course",
                "color": "#198754",
                "description": "",
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            Course.objects.filter(
                owner=self.user,
                code__iexact="CP3501",
            ).count(),
            1,
        )
        self.assertIn(
            "You already have a course with this code.",
            response.context["form"].errors["code"],
        )

    def test_user_cannot_edit_another_users_course(self):
        other_course = Course.objects.create(
            owner=self.other_user,
            code="CP1404",
            name="Programming",
            color="#DC3545",
        )

        response = self.client.get(
            reverse(
                "course_update",
                args=[other_course.pk],
            )
        )

        self.assertEqual(response.status_code, 404)


class AssessmentManagementTests(TestCase):
    """Automated tests for US-05."""

    def setUp(self):
        self.user = User.objects.create_user(
            username="student1",
            password="StrongPass123!",
        )
        self.other_user = User.objects.create_user(
            username="student2",
            password="StrongPass123!",
        )

        self.course = Course.objects.create(
            owner=self.user,
            code="CP3501",
            name="Data Science",
            color="#0D6EFD",
        )
        self.other_course = Course.objects.create(
            owner=self.other_user,
            code="CP1404",
            name="Programming",
            color="#DC3545",
        )

        self.client.login(
            username="student1",
            password="StrongPass123!",
        )

    def test_user_can_create_assessment(self):
        start_date = timezone.now() + timedelta(days=1)
        due_date = timezone.now() + timedelta(days=7)

        response = self.client.post(
            reverse("assessment_create"),
            {
                "course": self.course.pk,
                "title": "Data Analysis Report",
                "assessment_type": Assessment.AssessmentType.ASSIGNMENT,
                "status": Assessment.Status.TODO,
                "start_date": datetime_local(start_date),
                "due_date": datetime_local(due_date),
                "weighting": "30",
                "notes": "Complete and submit the report.",
            },
        )

        self.assertRedirects(
            response,
            reverse("assessment_list"),
        )

        assessment = Assessment.objects.get(
            owner=self.user,
            title="Data Analysis Report",
        )

        self.assertEqual(assessment.course, self.course)
        self.assertEqual(assessment.weighting, 30)

    def test_start_date_after_due_date_is_rejected(self):
        start_date = timezone.now() + timedelta(days=7)
        due_date = timezone.now() + timedelta(days=1)

        response = self.client.post(
            reverse("assessment_create"),
            {
                "course": self.course.pk,
                "title": "Invalid Assessment",
                "assessment_type": Assessment.AssessmentType.ASSIGNMENT,
                "status": Assessment.Status.TODO,
                "start_date": datetime_local(start_date),
                "due_date": datetime_local(due_date),
                "weighting": "20",
                "notes": "",
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertFalse(
            Assessment.objects.filter(
                title="Invalid Assessment"
            ).exists()
        )
        self.assertIn(
            "Start date cannot be after the due date.",
            response.context["form"].errors["start_date"],
        )

    def test_user_cannot_edit_another_users_assessment(self):
        other_assessment = Assessment.objects.create(
            owner=self.other_user,
            course=self.other_course,
            title="Programming Assignment",
            assessment_type=Assessment.AssessmentType.ASSIGNMENT,
            status=Assessment.Status.TODO,
            due_date=timezone.now() + timedelta(days=7),
        )

        response = self.client.get(
            reverse(
                "assessment_update",
                args=[other_assessment.pk],
            )
        )

        self.assertEqual(response.status_code, 404)


class StudyTaskManagementTests(TestCase):
    """Automated tests for US-06."""

    def setUp(self):
        self.user = User.objects.create_user(
            username="student1",
            password="StrongPass123!",
        )

        self.course = Course.objects.create(
            owner=self.user,
            code="CP3501",
            name="Data Science",
            color="#0D6EFD",
        )
        self.second_course = Course.objects.create(
            owner=self.user,
            code="CP3407",
            name="Advanced Software Engineering",
            color="#198754",
        )

        self.assessment = Assessment.objects.create(
            owner=self.user,
            course=self.course,
            title="Data Analysis Report",
            assessment_type=Assessment.AssessmentType.ASSIGNMENT,
            status=Assessment.Status.TODO,
            due_date=timezone.now() + timedelta(days=7),
        )
        self.second_assessment = Assessment.objects.create(
            owner=self.user,
            course=self.second_course,
            title="Software Project",
            assessment_type=Assessment.AssessmentType.PROJECT,
            status=Assessment.Status.IN_PROGRESS,
            due_date=timezone.now() + timedelta(days=10),
        )

        self.client.login(
            username="student1",
            password="StrongPass123!",
        )

    def test_user_can_create_task_linked_to_assessment(self):
        response = self.client.post(
            reverse("task_create"),
            {
                "course": self.course.pk,
                "assessment": self.assessment.pk,
                "title": "Write report introduction",
                "description": "Draft the report introduction.",
                "priority": StudyTask.Priority.HIGH,
                "status": StudyTask.Status.TODO,
                "start_date": datetime_local(timezone.now()),
                "due_date": datetime_local(
                    timezone.now() + timedelta(days=2)
                ),
                "estimated_hours": "2",
            },
        )

        self.assertRedirects(response, reverse("task_list"))

        task = StudyTask.objects.get(
            owner=self.user,
            title="Write report introduction",
        )

        self.assertEqual(task.course, self.course)
        self.assertEqual(task.assessment, self.assessment)
        self.assertEqual(task.priority, StudyTask.Priority.HIGH)

    def test_assessment_from_different_course_is_rejected(self):
        response = self.client.post(
            reverse("task_create"),
            {
                "course": self.course.pk,
                "assessment": self.second_assessment.pk,
                "title": "Invalid linked task",
                "description": "",
                "priority": StudyTask.Priority.MEDIUM,
                "status": StudyTask.Status.TODO,
                "start_date": "",
                "due_date": "",
                "estimated_hours": "1",
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertFalse(
            StudyTask.objects.filter(
                title="Invalid linked task"
            ).exists()
        )
        self.assertIn(
            "The assessment must belong to the selected course.",
            response.context["form"].errors["assessment"],
        )

    def test_completed_task_sets_completion_time(self):
        response = self.client.post(
            reverse("task_create"),
            {
                "course": self.course.pk,
                "assessment": self.assessment.pk,
                "title": "Submit completed report",
                "description": "",
                "priority": StudyTask.Priority.HIGH,
                "status": StudyTask.Status.COMPLETED,
                "start_date": "",
                "due_date": datetime_local(
                    timezone.now() + timedelta(days=1)
                ),
                "estimated_hours": "1",
            },
        )

        self.assertRedirects(response, reverse("task_list"))

        task = StudyTask.objects.get(
            title="Submit completed report"
        )

        self.assertIsNotNone(task.completed_at)


class SearchFilterSortTests(TestCase):
    """Automated tests for US-09."""

    def setUp(self):
        self.user = User.objects.create_user(
            username="student1",
            password="StrongPass123!",
        )

        self.course = Course.objects.create(
            owner=self.user,
            code="CP3501",
            name="Data Science",
            color="#0D6EFD",
        )

        self.assessment = Assessment.objects.create(
            owner=self.user,
            course=self.course,
            title="Data Analysis Report",
            assessment_type=Assessment.AssessmentType.ASSIGNMENT,
            status=Assessment.Status.TODO,
            due_date=timezone.now() + timedelta(days=10),
        )

        StudyTask.objects.create(
            owner=self.user,
            course=self.course,
            assessment=self.assessment,
            title="Write report",
            priority=StudyTask.Priority.HIGH,
            status=StudyTask.Status.IN_PROGRESS,
            due_date=timezone.now() + timedelta(days=3),
        )
        StudyTask.objects.create(
            owner=self.user,
            course=self.course,
            assessment=self.assessment,
            title="Read chapter",
            priority=StudyTask.Priority.MEDIUM,
            status=StudyTask.Status.TODO,
            due_date=timezone.now() + timedelta(days=2),
        )
        StudyTask.objects.create(
            owner=self.user,
            course=self.course,
            assessment=self.assessment,
            title="Analyse data",
            priority=StudyTask.Priority.LOW,
            status=StudyTask.Status.COMPLETED,
            due_date=timezone.now() + timedelta(days=1),
        )

        self.client.login(
            username="student1",
            password="StrongPass123!",
        )

    def test_search_returns_matching_task(self):
        response = self.client.get(
            reverse("task_list"),
            {"search": "report"},
        )

        titles = list(
            response.context["tasks"].values_list(
                "title",
                flat=True,
            )
        )

        self.assertEqual(titles, ["Write report"])

    def test_priority_filter_returns_only_high_priority_tasks(self):
        response = self.client.get(
            reverse("task_list"),
            {"priority": StudyTask.Priority.HIGH},
        )

        tasks = list(response.context["tasks"])

        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0].title, "Write report")
        self.assertEqual(
            tasks[0].priority,
            StudyTask.Priority.HIGH,
        )

    def test_title_descending_sort(self):
        response = self.client.get(
            reverse("task_list"),
            {"sort": "title_desc"},
        )

        titles = list(
            response.context["tasks"].values_list(
                "title",
                flat=True,
            )
        )

        self.assertEqual(
            titles,
            [
                "Write report",
                "Read chapter",
                "Analyse data",
            ],
        )

class QuickTaskCompletionTests(TestCase):
    """TDD and mock tests for quick task completion."""

    def setUp(self):
        self.owner = User.objects.create_user(
            username="task_owner",
            password="StrongPass123!",
        )
        self.other_user = User.objects.create_user(
            username="other_student",
            password="StrongPass123!",
        )

        self.course = Course.objects.create(
            owner=self.owner,
            code="CP3407",
            name="Advanced Software Engineering",
            color="#0D6EFD",
        )

        self.task = StudyTask.objects.create(
            owner=self.owner,
            course=self.course,
            title="Complete automated testing",
            priority=StudyTask.Priority.HIGH,
            status=StudyTask.Status.TODO,
            due_date=timezone.now() + timedelta(days=2),
        )

    def test_anonymous_user_is_redirected_to_login(self):
        url = reverse(
            "task_mark_complete",
            args=[self.task.pk],
        )

        response = self.client.post(url)

        self.assertRedirects(
            response,
            f"{reverse('login')}?next={url}",
        )

    @patch("planner.models.timezone.now")
    def test_owner_can_mark_task_as_completed(self, mock_now):
        fixed_time = timezone.make_aware(
            datetime(2026, 7, 30, 9, 0)
        )
        mock_now.return_value = fixed_time

        self.client.login(
            username="task_owner",
            password="StrongPass123!",
        )

        response = self.client.post(
            reverse(
                "task_mark_complete",
                args=[self.task.pk],
            )
        )

        self.assertRedirects(response, reverse("task_list"))

        self.task.refresh_from_db()

        self.assertEqual(
            self.task.status,
            StudyTask.Status.COMPLETED,
        )
        self.assertEqual(
            self.task.completed_at,
            fixed_time,
        )

    def test_user_cannot_complete_another_users_task(self):
        self.client.login(
            username="other_student",
            password="StrongPass123!",
        )

        response = self.client.post(
            reverse(
                "task_mark_complete",
                args=[self.task.pk],
            )
        )

        self.assertEqual(response.status_code, 404)

        self.task.refresh_from_db()

        self.assertEqual(
            self.task.status,
            StudyTask.Status.TODO,
        )
        self.assertIsNone(self.task.completed_at)