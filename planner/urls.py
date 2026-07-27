from django.urls import path

from . import views


urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("register/", views.register, name="register"),

    path(
        "courses/",
        views.course_list,
        name="course_list",
    ),
    path(
        "courses/add/",
        views.course_create,
        name="course_create",
    ),
    path(
        "courses/<int:pk>/edit/",
        views.course_update,
        name="course_update",
    ),
    path(
        "courses/<int:pk>/delete/",
        views.course_delete,
        name="course_delete",
    ),
        path(
        "assessments/",
        views.assessment_list,
        name="assessment_list",
    ),
    path(
        "assessments/add/",
        views.assessment_create,
        name="assessment_create",
    ),
    path(
        "assessments/<int:pk>/edit/",
        views.assessment_update,
        name="assessment_update",
    ),
    path(
        "assessments/<int:pk>/delete/",
        views.assessment_delete,
        name="assessment_delete",
    ),
]