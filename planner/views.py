from datetime import timedelta

from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.db.models import Q

from .forms import (
    AssessmentForm,
    CourseForm,
    RegisterForm,
    StudyTaskForm,
)
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
    """Display academic progress for the logged-in user."""

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

    user_assessments = Assessment.objects.filter(
        owner=request.user,
    ).select_related(
        "course",
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

    upcoming_assessments = user_assessments.filter(
        due_date__gte=now,
    ).exclude(
        status=Assessment.Status.COMPLETED,
    ).order_by("due_date")[:5]

    total_task_count = user_tasks.count()

    completed_task_count = user_tasks.filter(
        status=StudyTask.Status.COMPLETED,
    ).count()

    todo_task_count = user_tasks.filter(
        status=StudyTask.Status.TODO,
    ).count()

    in_progress_task_count = user_tasks.filter(
        status=StudyTask.Status.IN_PROGRESS,
    ).count()

    if total_task_count:
        completion_rate = round(
            completed_task_count / total_task_count * 100
        )
    else:
        completion_rate = 0

    total_assessment_count = user_assessments.count()

    completed_assessment_count = user_assessments.filter(
        status=Assessment.Status.COMPLETED,
    ).count()

    upcoming_assessment_count = user_assessments.filter(
        due_date__gte=now,
    ).exclude(
        status=Assessment.Status.COMPLETED,
    ).count()

    context = {
        "course_count": user_courses.count(),
        "task_count": total_task_count,
        "completed_task_count": completed_task_count,
        "todo_task_count": todo_task_count,
        "in_progress_task_count": in_progress_task_count,
        "overdue_task_count": overdue_tasks.count(),
        "completion_rate": completion_rate,
        "total_assessment_count": total_assessment_count,
        "completed_assessment_count": completed_assessment_count,
        "upcoming_assessment_count": upcoming_assessment_count,
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

@login_required
def assessment_list(request):
    """Display assessments belonging to the logged-in user."""

    assessments = Assessment.objects.filter(
        owner=request.user,
    ).select_related(
        "course",
    ).order_by(
        "due_date",
        "title",
    )

    return render(
        request,
        "planner/assessment_list.html",
        {"assessments": assessments},
    )


@login_required
def assessment_create(request):
    """Create an assessment for the logged-in user."""

    if not Course.objects.filter(owner=request.user).exists():
        messages.warning(
            request,
            "Create a course before adding an assessment.",
        )
        return redirect("course_create")

    if request.method == "POST":
        form = AssessmentForm(
            request.POST,
            user=request.user,
        )

        if form.is_valid():
            assessment = form.save(commit=False)
            assessment.owner = request.user
            assessment.save()

            messages.success(
                request,
                f"{assessment.title} was created successfully.",
            )

            return redirect("assessment_list")
    else:
        form = AssessmentForm(user=request.user)

    return render(
        request,
        "planner/assessment_form.html",
        {
            "form": form,
            "page_title": "Add assessment",
            "button_text": "Create assessment",
        },
    )


@login_required
def assessment_update(request, pk):
    """Update an assessment belonging to the logged-in user."""

    assessment = get_object_or_404(
        Assessment,
        pk=pk,
        owner=request.user,
    )

    if request.method == "POST":
        form = AssessmentForm(
            request.POST,
            instance=assessment,
            user=request.user,
        )

        if form.is_valid():
            assessment = form.save()

            messages.success(
                request,
                f"{assessment.title} was updated successfully.",
            )

            return redirect("assessment_list")
    else:
        form = AssessmentForm(
            instance=assessment,
            user=request.user,
        )

    return render(
        request,
        "planner/assessment_form.html",
        {
            "form": form,
            "assessment": assessment,
            "page_title": "Edit assessment",
            "button_text": "Save changes",
        },
    )


@login_required
def assessment_delete(request, pk):
    """Delete an assessment belonging to the logged-in user."""

    assessment = get_object_or_404(
        Assessment,
        pk=pk,
        owner=request.user,
    )

    if request.method == "POST":
        assessment_title = assessment.title
        assessment.delete()

        messages.success(
            request,
            f"{assessment_title} was deleted successfully.",
        )

        return redirect("assessment_list")

    return render(
        request,
        "planner/assessment_confirm_delete.html",
        {"assessment": assessment},
    )



@login_required
def task_list(request):
    """Display, search, filter and sort the user's study tasks."""

    tasks = StudyTask.objects.filter(
        owner=request.user,
    ).select_related(
        "course",
        "assessment",
    )

    search_query = request.GET.get("search", "").strip()
    selected_course = request.GET.get("course", "")
    selected_status = request.GET.get("status", "")
    selected_priority = request.GET.get("priority", "")
    selected_sort = request.GET.get("sort", "due_asc")

    if search_query:
        tasks = tasks.filter(
            Q(title__icontains=search_query)
            | Q(description__icontains=search_query)
            | Q(course__code__icontains=search_query)
            | Q(course__name__icontains=search_query)
            | Q(assessment__title__icontains=search_query)
        )

    if selected_course.isdigit():
        tasks = tasks.filter(course_id=selected_course)

    if selected_status in StudyTask.Status.values:
        tasks = tasks.filter(status=selected_status)

    if selected_priority in StudyTask.Priority.values:
        tasks = tasks.filter(priority=selected_priority)

    sort_options = {
        "due_asc": ("due_date", "title"),
        "due_desc": ("-due_date", "title"),
        "title_asc": ("title",),
        "title_desc": ("-title",),
        "newest": ("-created_at",),
        "oldest": ("created_at",),
    }

    if selected_sort not in sort_options:
        selected_sort = "due_asc"

    tasks = tasks.order_by(*sort_options[selected_sort])

    courses = Course.objects.filter(
        owner=request.user,
        is_archived=False,
    ).order_by("code")

    context = {
        "tasks": tasks,
        "courses": courses,
        "status_choices": StudyTask.Status.choices,
        "priority_choices": StudyTask.Priority.choices,
        "search_query": search_query,
        "selected_course": selected_course,
        "selected_status": selected_status,
        "selected_priority": selected_priority,
        "selected_sort": selected_sort,
    }

    return render(
        request,
        "planner/task_list.html",
        context,
    )


@login_required
def task_create(request):
    """Create a study task for the logged-in user."""

    if not Course.objects.filter(
        owner=request.user,
        is_archived=False,
    ).exists():
        messages.warning(
            request,
            "Create an active course before adding a study task.",
        )
        return redirect("course_create")

    if request.method == "POST":
        form = StudyTaskForm(
            request.POST,
            user=request.user,
        )

        if form.is_valid():
            task = form.save(commit=False)
            task.owner = request.user

            task.sync_completion_time()

            task.save()

            messages.success(
                request,
                f"{task.title} was created successfully.",
            )

            return redirect("task_list")
    else:
        form = StudyTaskForm(user=request.user)

    return render(
        request,
        "planner/task_form.html",
        {
            "form": form,
            "page_title": "Add study task",
            "button_text": "Create task",
        },
    )


@login_required
def task_update(request, pk):
    """Update a study task belonging to the logged-in user."""

    task = get_object_or_404(
        StudyTask,
        pk=pk,
        owner=request.user,
    )

    if request.method == "POST":
        form = StudyTaskForm(
            request.POST,
            instance=task,
            user=request.user,
        )

        if form.is_valid():
            task = form.save(commit=False)
            task.owner = request.user

            _update_task_completion_time(task)

            task.save()

            messages.success(
                request,
                f"{task.title} was updated successfully.",
            )

            return redirect("task_list")
    else:
        form = StudyTaskForm(
            instance=task,
            user=request.user,
        )

    return render(
        request,
        "planner/task_form.html",
        {
            "form": form,
            "task": task,
            "page_title": "Edit study task",
            "button_text": "Save changes",
        },
    )


@login_required
def task_delete(request, pk):
    """Delete a study task belonging to the logged-in user."""

    task = get_object_or_404(
        StudyTask,
        pk=pk,
        owner=request.user,
    )

    if request.method == "POST":
        task_title = task.title
        task.delete()

        messages.success(
            request,
            f"{task_title} was deleted successfully.",
        )

        return redirect("task_list")

    return render(
        request,
        "planner/task_confirm_delete.html",
        {"task": task},
    )