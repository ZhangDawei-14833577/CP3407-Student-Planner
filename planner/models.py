from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import (
    MaxValueValidator,
    MinValueValidator,
    RegexValidator,
)
from django.db import models
from django.utils import timezone


class Course(models.Model):
    """A university course belonging to one user."""

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="courses",
    )
    code = models.CharField(
        max_length=20,
        help_text="For example: CP3407",
    )
    name = models.CharField(max_length=150)
    color = models.CharField(
        max_length=7,
        default="#0D6EFD",
        validators=[
            RegexValidator(
                regex=r"^#[0-9A-Fa-f]{6}$",
                message="Enter a valid hexadecimal colour such as #0D6EFD.",
            )
        ],
    )
    description = models.TextField(blank=True)
    is_archived = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["code"]
        constraints = [
            models.UniqueConstraint(
                fields=["owner", "code"],
                name="unique_course_code_per_user",
            )
        ]

    def __str__(self):
        return f"{self.code} - {self.name}"


class Assessment(models.Model):
    """An assignment, examination, project or other assessment."""

    class AssessmentType(models.TextChoices):
        ASSIGNMENT = "assignment", "Assignment"
        EXAMINATION = "examination", "Examination"
        PROJECT = "project", "Project"
        QUIZ = "quiz", "Quiz"
        PRACTICAL = "practical", "Practical"
        PRESENTATION = "presentation", "Presentation"
        OTHER = "other", "Other"

    class Status(models.TextChoices):
        TODO = "todo", "To Do"
        IN_PROGRESS = "in_progress", "In Progress"
        COMPLETED = "completed", "Completed"

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="assessments",
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="assessments",
    )

    title = models.CharField(max_length=200)
    assessment_type = models.CharField(
        max_length=20,
        choices=AssessmentType.choices,
        default=AssessmentType.ASSIGNMENT,
    )
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.TODO,
    )

    start_date = models.DateTimeField(null=True, blank=True)
    due_date = models.DateTimeField()

    weighting = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100),
        ],
        help_text="Assessment weighting as a percentage from 0 to 100.",
    )
    notes = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["due_date", "title"]

    def clean(self):
        errors = {}

        if (
            self.start_date
            and self.due_date
            and self.start_date > self.due_date
        ):
            errors["start_date"] = "Start date cannot be after the due date."

        if (
            self.course_id
            and self.owner_id
            and self.course.owner_id != self.owner_id
        ):
            errors["course"] = "The selected course must belong to this user."

        if errors:
            raise ValidationError(errors)

    @property
    def is_overdue(self):
        return (
            self.status != self.Status.COMPLETED
            and self.due_date < timezone.now()
        )

    def __str__(self):
        return f"{self.course.code}: {self.title}"


class StudyTask(models.Model):
    """A smaller actionable task linked to a course or assessment."""

    class Priority(models.TextChoices):
        HIGH = "high", "High"
        MEDIUM = "medium", "Medium"
        LOW = "low", "Low"

    class Status(models.TextChoices):
        TODO = "todo", "To Do"
        IN_PROGRESS = "in_progress", "In Progress"
        COMPLETED = "completed", "Completed"

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="study_tasks",
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="study_tasks",
    )
    assessment = models.ForeignKey(
        Assessment,
        on_delete=models.SET_NULL,
        related_name="study_tasks",
        null=True,
        blank=True,
    )

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    priority = models.CharField(
        max_length=10,
        choices=Priority.choices,
        default=Priority.MEDIUM,
    )
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.TODO,
    )

    start_date = models.DateTimeField(null=True, blank=True)
    due_date = models.DateTimeField(null=True, blank=True)

    estimated_hours = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True,
        validators=[MinValueValidator(0)],
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    completed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ["due_date", "-priority", "title"]

    def clean(self):
        errors = {}

        if (
            self.start_date
            and self.due_date
            and self.start_date > self.due_date
        ):
            errors["start_date"] = "Start date cannot be after the due date."

        if (
            self.course_id
            and self.owner_id
            and self.course.owner_id != self.owner_id
        ):
            errors["course"] = "The selected course must belong to this user."

        if self.assessment_id:
            if (
                self.course_id
                and self.assessment.course_id != self.course_id
            ):
                errors["assessment"] = (
                    "The assessment must belong to the selected course."
                )

            if (
                self.owner_id
                and self.assessment.owner_id != self.owner_id
            ):
                errors["assessment"] = (
                    "The selected assessment must belong to this user."
                )

        if errors:
            raise ValidationError(errors)

    @property
    def is_overdue(self):
        return (
            self.due_date is not None
            and self.status != self.Status.COMPLETED
            and self.due_date < timezone.now()
        )

    def __str__(self):
        return self.title