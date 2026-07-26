from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Course


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