from factory import Faker, Sequence, post_generation
from factory.django import DjangoModelFactory

from app.users.models import User


class UserFactory(DjangoModelFactory):
    username = Sequence(lambda n: f"person_username{n}")
    email = Sequence(lambda n: f"person{n}@example.com")
    mobile = Sequence(lambda n: f"+98{str(n).zfill(10)}")
    first_name = Faker("first_name")
    last_name = Faker("last_name")
    last_name = Faker("last_name")

    @post_generation
    def password(self, create, extracted, **kwargs):
        self.set_password("password")

    class Meta:
        model = User
        django_get_or_create = ["username"]
