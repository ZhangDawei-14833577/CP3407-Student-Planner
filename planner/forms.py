from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Assessment, Course, StudyTask


class RegisterForm(UserCreationForm):
    """Form used to create a new student account."""

    email = forms.EmailField(
        required=True,
        help_text="Enter a valid email address.",
    )

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password1",
            "password2",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update(
                {
                    "class": "form-control",
                }
            )

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]

        if commit:
            user.save()

        return user


class CourseForm(forms.ModelForm):
    """Form used to create and update a course."""

    class Meta:
        model = Course
        fields = (
            "code",
            "name",
            "color",
            "description",
            "is_archived",
        )
        widgets = {
            "code": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "For example: CP3407",
                }
            ),
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Course name",
                }
            ),
            "color": forms.TextInput(
                attrs={
                    "class": "form-control form-control-color",
                    "type": "color",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Optional course description",
                }
            ),
            "is_archived": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                }
            ),
        }

    def __init__(self, *args, user=None, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)

    def clean_code(self):
        """Prevent one user from creating duplicate course codes."""

        code = self.cleaned_data["code"].strip().upper()

        existing_courses = Course.objects.filter(
            owner=self.user,
            code__iexact=code,
        )

        if self.instance.pk:
            existing_courses = existing_courses.exclude(
                pk=self.instance.pk
            )

        if existing_courses.exists():
            raise forms.ValidationError(
                "You already have a course with this code."
            )

        return code

class AssessmentForm(forms.ModelForm):
    """Form used to create and update an assessment."""

    class Meta:
        model = Assessment
        fields = (
            "course",
            "title",
            "assessment_type",
            "status",
            "start_date",
            "due_date",
            "weighting",
            "notes",
        )
        widgets = {
            "course": forms.Select(
                attrs={"class": "form-select"}
            ),
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "For example: Software Project",
                }
            ),
            "assessment_type": forms.Select(
                attrs={"class": "form-select"}
            ),
            "status": forms.Select(
                attrs={"class": "form-select"}
            ),
            "start_date": forms.DateTimeInput(
                format="%Y-%m-%dT%H:%M",
                attrs={
                    "class": "form-control",
                    "type": "datetime-local",
                },
            ),
            "due_date": forms.DateTimeInput(
                format="%Y-%m-%dT%H:%M",
                attrs={
                    "class": "form-control",
                    "type": "datetime-local",
                },
            ),
            "weighting": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "min": "0",
                    "max": "100",
                    "step": "0.01",
                }
            ),
            "notes": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                }
            ),
        }

    def __init__(self, *args, user=None, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)

        self.fields["start_date"].input_formats = [
            "%Y-%m-%dT%H:%M"
        ]
        self.fields["due_date"].input_formats = [
            "%Y-%m-%dT%H:%M"
        ]

        if user is None:
            self.fields["course"].queryset = Course.objects.none()
        else:
            self.fields["course"].queryset = Course.objects.filter(
                owner=user,
            ).order_by(
                "is_archived",
                "code",
            )

    def clean(self):
        cleaned_data = super().clean()

        course = cleaned_data.get("course")
        start_date = cleaned_data.get("start_date")
        due_date = cleaned_data.get("due_date")

        if course and course.owner != self.user:
            self.add_error(
                "course",
                "The selected course does not belong to you.",
            )

        if start_date and due_date and start_date > due_date:
            self.add_error(
                "start_date",
                "Start date cannot be after the due date.",
            )

        return cleaned_data

class StudyTaskForm(forms.ModelForm):
    """Form used to create and update a study task."""

    class Meta:
        model = StudyTask
        fields = (
            "course",
            "assessment",
            "title",
            "description",
            "priority",
            "status",
            "start_date",
            "due_date",
            "estimated_hours",
        )
        widgets = {
            "course": forms.Select(
                attrs={"class": "form-select"}
            ),
            "assessment": forms.Select(
                attrs={"class": "form-select"}
            ),
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "For example: Write report introduction",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Optional task description",
                }
            ),
            "priority": forms.Select(
                attrs={"class": "form-select"}
            ),
            "status": forms.Select(
                attrs={"class": "form-select"}
            ),
            "start_date": forms.DateTimeInput(
                format="%Y-%m-%dT%H:%M",
                attrs={
                    "class": "form-control",
                    "type": "datetime-local",
                },
            ),
            "due_date": forms.DateTimeInput(
                format="%Y-%m-%dT%H:%M",
                attrs={
                    "class": "form-control",
                    "type": "datetime-local",
                },
            ),
            "estimated_hours": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "min": "0",
                    "step": "0.25",
                    "placeholder": "For example: 2.5",
                }
            ),
        }

    def __init__(self, *args, user=None, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)

        self.fields["start_date"].input_formats = [
            "%Y-%m-%dT%H:%M"
        ]
        self.fields["due_date"].input_formats = [
            "%Y-%m-%dT%H:%M"
        ]

        self.fields["assessment"].required = False
        self.fields["assessment"].help_text = (
            "Optional. The assessment must belong to the selected course."
        )

        if user is None:
            self.fields["course"].queryset = Course.objects.none()
            self.fields["assessment"].queryset = (
                Assessment.objects.none()
            )
        else:
            self.fields["course"].queryset = Course.objects.filter(
                owner=user,
            ).order_by(
                "is_archived",
                "code",
            )

            self.fields["assessment"].queryset = (
                Assessment.objects.filter(
                    owner=user,
                )
                .select_related("course")
                .order_by("due_date", "title")
            )

    def clean(self):
        cleaned_data = super().clean()

        course = cleaned_data.get("course")
        assessment = cleaned_data.get("assessment")
        start_date = cleaned_data.get("start_date")
        due_date = cleaned_data.get("due_date")

        if course and course.owner != self.user:
            self.add_error(
                "course",
                "The selected course does not belong to you.",
            )

        if assessment:
            if assessment.owner != self.user:
                self.add_error(
                    "assessment",
                    "The selected assessment does not belong to you.",
                )

            if course and assessment.course_id != course.id:
                self.add_error(
                    "assessment",
                    "The assessment must belong to the selected course.",
                )

        if start_date and due_date and start_date > due_date:
            self.add_error(
                "start_date",
                "Start date cannot be after the due date.",
            )

        return cleaned_data