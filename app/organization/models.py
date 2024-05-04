from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.utils.translation import gettext_lazy as _

from app.common.comment.models import Comment
from app.core.models import BaseModel
from app.users.models import User


class Organization(BaseModel):
    name = models.CharField(_("organization name"), max_length=255)
    owners = models.ManyToManyField(User, related_name="organization_owners", null=True, blank=True)
    managers = models.ManyToManyField(User, related_name="organization_managers", null=True, blank=True)
    developers = models.ManyToManyField(User, related_name="organization_developers", null=True, blank=True)
    comments = GenericRelation(Comment, related_query_name="organization_comments", null=True, blank=True)

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs) -> "Organization":
        saved_data = super().save(*args, **kwargs)
        return saved_data

    def update(self, *args, **kwargs) -> "Organization":
        saved_data = super().save(*args, **kwargs)
        return saved_data

    def delete(self, *args, **kwargs) -> None:
        self.is_active = False
        self.save()


class Sprint(BaseModel):
    class SprintState(models.TextChoices):
        BACKLOG = "BACKLOG"
        ACTIVE = "ACTIVE"
        FUTURE = "FUTURE"

    organization = models.ForeignKey(Organization, related_name="organization_sprint", on_delete=models.CASCADE)
    state = models.CharField(
        _("state of this sprint"), max_length=255, choices=SprintState, default=SprintState.FUTURE
    )
    name = models.CharField(_("organization sprint"), max_length=255)
    order_id = models.IntegerField(_("order of sprint to show"), default=0)
    comments = GenericRelation(Comment, related_query_name="sprint_comments")

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs) -> "Organization":
        saved_data = super().save(*args, **kwargs)
        return saved_data

    def update(self, *args, **kwargs) -> "Organization":
        saved_data = super().save(*args, **kwargs)
        return saved_data

    def delete(self, *args, **kwargs) -> None:
        self.is_active = False
        self.save()


class Task(BaseModel):
    class TaskState(models.TextChoices):
        PEND = "PEND"
        TO_DEVELOP = "TO_DEVELOP"
        DEVELOPING = "DEVELOPING"
        TO_REVIEW = "TO_REVIEW"
        APPROVED = "APPROVED"
        TO_TEST = "TO_TEST"
        DELIVERED = "DELIVERED"

    name = models.CharField(_("task name"), max_length=255)
    sprint = models.ForeignKey(Sprint, related_name="sprint_tasks", on_delete=models.CASCADE)
    state = models.CharField(_("state of this task"), max_length=255, choices=TaskState, default=TaskState.TO_DEVELOP)
    comments = GenericRelation(Comment, related_query_name="task_comments")
    signed_to = models.ForeignKey(User, related_name="assigned_task", on_delete=models.CASCADE)
    review_by = models.ForeignKey(User, related_name="review_task", on_delete=models.CASCADE)
    due_date = models.DateTimeField(_("due date of task"), null=True, blank=True)
    order_id = models.IntegerField(_("order of task to show"), default=0)

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs) -> "Organization":
        saved_data = super().save(*args, **kwargs)
        return saved_data

    def update(self, *args, **kwargs) -> "Organization":
        saved_data = super().save(*args, **kwargs)
        return saved_data

    def delete(self, *args, **kwargs) -> None:
        self.is_active = False
        self.save()
