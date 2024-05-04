import pytest
from celery.result import EagerResult

from app.users.tasks import email_users_count
from app.users.tests.factories import UserFactory

pytestmark = pytest.mark.django_db


def test_user_count(settings):
    """A basic test to execute the email_users_count Celery task."""
    batch_size = 100
    UserFactory.create_batch(batch_size)
    settings.CELERY_TASK_ALWAYS_EAGER = True
    task_result = email_users_count.delay()
    assert isinstance(task_result, EagerResult)
    assert task_result.result == batch_size
