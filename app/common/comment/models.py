from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import gettext_lazy as _

from app.core.models import BaseModel
from app.users.models import User


class DeletedComment(BaseModel):
    delete_data = models.TextField(_("info about deleting comment"))

    def save(self, *args, **kwargs) -> "DeletedComment":
        return super().save(*args, **kwargs)

    def update(self, *args, **kwargs) -> "DeletedComment":
        return super().save(*args, **kwargs)

    def delete(self, *args, **kwargs) -> None:
        return super().delete(*args, **kwargs)


class Comment(BaseModel):
    class CommentCategory(models.TextChoices):
        REVIEW = "REVIEW"
        PERSONAL = "PERSONAL"
        APPRECIATION = "APPRECIATION"

    category = models.CharField(
        _("comment category"), max_length=255, choices=CommentCategory, default=CommentCategory.REVIEW
    )
    mention = models.ManyToManyField(User, related_name="mentions")

    text = models.TextField(_("comment text"), null=True, blank=True)

    # to be able connect it to all
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField(null=True, blank=True)
    content_object = GenericForeignKey("content_type", "object_id")

    def save(self, *args, **kwargs) -> "Comment":
        return super().save(*args, **kwargs)

    def update(self, *args, **kwargs) -> "Comment":
        return super().save(*args, **kwargs)

    def delete(self, *args, **kwargs) -> None:
        comment_db_log = f"from table '{self.content_type}' row: '{self.object_id}'"
        deleted_image = DeletedComment.objects.create(delete_data=comment_db_log)
        content_type = ContentType.objects.get_for_model(DeletedComment)
        self.content_type = content_type
        self.object_id = deleted_image.id
        self.save()
        return super().delete(*args, **kwargs)
