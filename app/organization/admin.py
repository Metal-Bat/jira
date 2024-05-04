from django.contrib import admin

from app.common.comment.admin import CommentInline
from app.organization.models import Organization, Sprint, Task


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at", "modified_at")
    raw_id_fields = ("owners", "managers", "developers")

    inlines = [
        CommentInline,
    ]


@admin.register(Sprint)
class SprintAdmin(admin.ModelAdmin):
    list_display = ("organization", "name", "state", "created_at", "modified_at")
    list_filter = ("organization", "state")
    ordering = ("order_id", "organization")
    inlines = [
        CommentInline,
    ]


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("get_organization", "get_sprint", "name", "state", "created_at", "modified_at")
    search_fields = ("name", "sprint__name", "sprint__organization__name")
    raw_id_fields = ("signed_to", "review_by", "sprint")
    ordering = ("order_id", "sprint")
    inlines = [
        CommentInline,
    ]

    @admin.display(description="sprint name", ordering="sprint.order_id")
    def get_sprint(self, obj):
        return obj.sprint.name

    @admin.display(description="organization name", ordering="sprint.order_id")
    def get_organization(self, obj):
        return obj.sprint.organization
