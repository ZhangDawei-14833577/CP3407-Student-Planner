from django.contrib import admin

from .models import Assessment, Course, StudyTask


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = (
        "code",
        "name",
        "owner",
        "color",
        "is_archived",
        "updated_at",
    )
    list_filter = ("is_archived",)
    search_fields = ("code", "name", "owner__username")
    ordering = ("code",)


@admin.register(Assessment)
class AssessmentAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "course",
        "owner",
        "assessment_type",
        "status",
        "due_date",
        "overdue",
    )
    list_filter = (
        "assessment_type",
        "status",
        "course",
        "due_date",
    )
    search_fields = (
        "title",
        "course__code",
        "course__name",
        "owner__username",
    )
    ordering = ("due_date",)

    @admin.display(boolean=True, description="Overdue")
    def overdue(self, obj):
        return obj.is_overdue


@admin.register(StudyTask)
class StudyTaskAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "course",
        "assessment",
        "owner",
        "priority",
        "status",
        "due_date",
        "overdue",
    )
    list_filter = (
        "priority",
        "status",
        "course",
        "due_date",
    )
    search_fields = (
        "title",
        "course__code",
        "course__name",
        "assessment__title",
        "owner__username",
    )
    ordering = ("due_date",)

    @admin.display(boolean=True, description="Overdue")
    def overdue(self, obj):
        return obj.is_overdue