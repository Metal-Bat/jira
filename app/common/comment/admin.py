from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline

from app.common.comment.models import Comment, DeletedComment


class CommentInline(GenericTabularInline):
    model = Comment
    extra = 3


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "content_object", "object_id")


@admin.register(DeletedComment)
class DeleteCommentAdmin(admin.ModelAdmin):
    list_display = ("id", "delete_data")
