from django.db import models


class BaseModel(models.Model):
    """
    abstract base Model that provides self-updating
    ``created_at`` and ``modified_at`` fields
    """

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True

    def delete(self, *args, **kwargs) -> None:  # type: ignore[no-untyped-def, override]
        self.is_active = False
        self.save()
        return None
