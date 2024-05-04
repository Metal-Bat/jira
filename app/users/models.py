from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    class UserState(models.TextChoices):
        BUSY = "BUSY"
        IN_MEETING = "IN_MEETING"
        OFF_DUTY = "OFF_DUTY"
        AVAILABLE = "AVAILABLE"

    first_name = models.CharField(_("first name of user"), max_length=255, blank=True, null=True)
    last_name = models.CharField(_("last name of user"), max_length=255, blank=True, null=True)
    show_contact_info = models.BooleanField(_("show user info to others"), default=False)
    current_state = models.CharField(
        _("current state of user"),
        max_length=255,
        choices=UserState.choices,
        default=UserState.AVAILABLE,
        help_text=_("selecting this can help others when to contact you"),
    )
    avatar = models.ImageField(_("avatar image of user"), upload_to="user_avatar", blank=True, null=True)
    description = models.TextField(_("user information to show to others"), blank=True, null=True)
    mobile = models.CharField(_("mobile number of user"), max_length=255, blank=True, null=True)
    email = models.EmailField(_("email of user"), max_length=255, blank=True, null=True)

    def get_full_name(self) -> str:
        """return fullname of user

        Returns:
            str: fullname
        """
        return str(self.first_name) + " " + str(self.last_name)
