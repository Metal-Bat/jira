from celery import shared_task

from app.users.models import User


@shared_task()
def email_users_count() -> int:
    """A pointless Celery task to demonstrate usage."""
    return User.objects.count()
