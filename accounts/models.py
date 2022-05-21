from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser, UserManager
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    email = models.EmailField(_('email address'), max_length=60, unique=True)
    balance = models.DecimalField(_('balance'), null=True, max_digits=8, decimal_places=4)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('staff status'), default=False)
    is_premium = models.BooleanField(_('premium account'), default=False)

    class Meta:
        db_table = "user"

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return "Username: " + self.username + " , " + "email: " + self.email


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, verbose_name=_("user"), on_delete=models.CASCADE)
    fullname = models.CharField(_("full name"), max_length=60, null=False, blank=False)
    avatar = models.ImageField(_("profile picture"), null=True, blank=True, upload_to="avatars/")
    phone_no = models.CharField(_("phone number"), max_length=30)
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now, editable=False)
    modified = models.DateTimeField(_("modified"), default=timezone.now, editable=False)

    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name = _("profile")
        verbose_name_plural = _("profiles")

