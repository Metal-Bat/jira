import pytest
from django.test import Client, TestCase


@pytest.mark.django_db
class UserApiTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_user_get_otp_validation(self) -> None:
        response = self.client.get("/api/v1/user/info")
        self.assertEqual(response.status_code, 401)
