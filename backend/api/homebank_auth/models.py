from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from common.utils import file_upload_path


class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    email_confirmed = models.BooleanField(_('email address confirmed'), default=True,
                                          help_text="Designates that this user's email address is confirmed")
    password_expired = models.BooleanField(_('password expired status'), default=False,
                                           help_text="Designates that this user's password has expired")

    class Meta(AbstractUser.Meta):
        ordering = ('email',)

    def __str__(self):
        return self.email


GENDER_UNSPECIFIED = 'U'
GENDER_MALE = 'M'
GENDER_FEMALE = 'F'
GENDER_NOTSAY = 'N'
GENDER_CHOICES = (
    (GENDER_FEMALE, _('Female')),
    (GENDER_MALE, _('Male')),
    (GENDER_NOTSAY, _('Rather not say')),
    (GENDER_UNSPECIFIED, _('Unspecified')),
)


def user_avatar_path(instance, filename):
    return file_upload_path("avatars", filename)


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    avatar = models.ImageField(upload_to=user_avatar_path, null=True, blank=True)

    class Meta:
        ordering = ('user__email', )

