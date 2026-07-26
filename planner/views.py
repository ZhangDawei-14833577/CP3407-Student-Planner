from datetime import timedelta

from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from .forms import CourseForm, RegisterForm
from .models import Assessment, Course, StudyTask


def register(request):
    """Create a new user account and log the user in."""

    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)

            messages.success(
                request,
                "Your account has been created successfully.",
            )

            return redirect("dashboard")
    else:
        form = RegisterForm()

    return render(
        request,
        "planner/register.html",
        {"form": form},
    )


@login_required
def dashboard(request):
    """Display academic information belonging to the current user."""

    now = timezone.now()
    seven_days_later = now + timedelta(days=7)

    user_courses = Course.objects.filter(
        owner=request.user,
        is_archived=False,
    )

    user_tasks = StudyTask.objects.filter(
        owner=request.user,
    ).select_related(
        "course",
        "assessment",
    )

    incomplete_tasks = user_tasks.exclude(
        status=StudyTask.Status.COMPLETED,
    )

    tasks_due_today = incomplete_tasks.filter(
        due_date__date=timezone.localdate(),
    ).order_by("due_date")

    tasks_due_soon = incomplete_tasks.filter(
        due_date__gt=now,
        due_date__lte=seven_days_later,
    ).order_by("due_date")

    overdue_tasks = incomplete_tasks.filter(
        due_date__lt=now,
    ).order_by("due_date")

    upcoming_assessments = Assessment.objects.filter(
        owner=request.user,
        due_date__gte=now,
    ).exclude(
        status=Assessment.Status.COMPLETED,
    ).select_related(
        "course",
    ).order_by("due_date")[:5]

    context = {
        "course_count": user_courses.count(),
        "task_count": user_tasks.count(),
        "completed_task_count": user_tasks.filter(
            status=StudyTask.Status.COMPLETED,
        ).count(),
        "overdue_task_count": overdue_tasks.count(),
        "tasks_due_today": tasks_due_today,
        "tasks_due_soon": tasks_due_soon[:5],
        "overdue_tasks": overdue_tasks[:5],
        "upcoming_assessments": upcoming_assessments,
    }

    return render(
        request,
        "planner/dashboard.html",
        context,
    )


@login_required
def course_list(request):
    """Display courses belonging to the logged-in user."""

    courses = Course.objects.filter(
        owner=request.user,
    ).order_by(
        "is_archived",
        "code",
    )

    return render(
        request,
        "planner/course_list.html",
        {"courses": courses},
    )


@login_required
def course_create(request):
    """Create a new course for the logged-in user."""

    if request.method == "POST":
        form = CourseForm(
            request.POST,
            user=request.user,
        )

        if form.is_valid():
            course = form.save(commit=False)
            course.owner = request.user
            course.save()

            messages.success(
                request,
                f"{course.code} was created successfully.",
            )

            return redirect("course_list")
    else:
        form = CourseForm(user=request.user)

    return render(
        request,
        "planner/course_form.html",
        {
            "form": form,
            "page_title": "Add course",
            "button_text": "Create course",
        },
    )


@login_required
def course_update(request, pk):
    """Update a course belonging to the logged-in user."""

    course = get_object_or_404(
        Course,
        pk=pk,
        owner=request.user,
    )

    if request.method == "POST":
        form = CourseForm(
            request.POST,
            instance=course,
            user=request.user,
        )

        if form.is_valid():
            course = form.save()

            messages.success(
                request,
                f"{course.code} was updated successfully.",
            )

            return redirect("course_list")
    else:
        form = CourseForm(
            instance=course,
            user=request.user,
        )

    return render(
        request,
        "planner/course_form.html",
        {
            "form": form,
            "course": course,
            "page_title": "Edit course",
            "button_text": "Save changes",
        },
    )


@login_required
def course_delete(request, pk):
    """Delete a course belonging to the logged-in user."""

    course = get_object_or_404(
        Course,
        pk=pk,
        owner=request.user,
    )

    if request.method == "POST":
        course_code = course.code
        course.delete()

        messages.success(
            request,
            f"{course_code} was deleted successfully.",
        )

        return redirect("course_list")

    return render(
        request,
        "planner/course_confirm_delete.html",
        {"course": course},
    )