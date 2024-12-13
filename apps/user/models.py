# apps/user/models

# django modules
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


# Model: User manager
class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError("The given username must be set")
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


# Model: Custom user
class User(AbstractBaseUser, PermissionsMixin):

    DOCUMENT_CHOICES = [
        (_("Voter Id"), _("Voter ID")),
        (_("Passport"), _("Passport")),
        (_("Citizenship Number"), _("Citizenship Number")),
    ]

    BLOOD_GROUP_CHOICES = [
        ("A+", "A+"),
        ("A-", "A-"),
        ("B+", "B+"),
        ("B-", "B-"),
        ("O+", "O+"),
        ("O-", "O-"),
        ("AB+", "AB+"),
        ("AB-", "AB-"),
    ]


    email = models.EmailField(_("Email Address"), max_length=254, unique=True)
    first_name = models.CharField(_("First Name"), max_length=30, blank=True)
    middle_name = models.CharField(
        _("Middle Name"), max_length=30, null=True, blank=True
    )
    last_name = models.CharField(_("Last Name"), max_length=30, blank=True)
    date_of_birth = models.DateField(
        _("Date of Birth"),
        null=True,
        blank=True,
        help_text="Enter Date in this Format: Year-Month-Day",
    )
    gender = models.CharField(
        _("Gender"), max_length=1, choices=[("M", "Male"), ("F", "Female")], null=True
    )
    blood_group = models.CharField(
        _("Blood Group"), max_length=3, null=True, choices=BLOOD_GROUP_CHOICES
    )
    identity_document_type = models.CharField(
        _("Identity Document Type"), max_length=32, null=True, choices=DOCUMENT_CHOICES
    )
    identity_document_number = models.CharField(
        _("Identity Document Number"), max_length=32
    )
    photo = models.ImageField(
        verbose_name=_("Profile Picture"), upload_to="profileImage/", null=True
    )
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)
    created = models.DateTimeField(_("Last updated"), auto_now=True)
    last_updated = models.DateTimeField(_("Last updated"), auto_now=True)
    is_email_verified = models.BooleanField(_("Email Verified"), default=False)
    is_active = models.BooleanField(_("active"), default=True)
    is_staff = models.BooleanField(_("staff status"), default=False)
    is_superuser = models.BooleanField(_("superuser status"), default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"

    def __str__(self):
        return self.get_full_name()

    def get_full_name(self):
        """
        Returns the full name of user
        """
        return f"{self.first_name} {self.middle_name} {self.last_name}"

    def has_submitted_identity_documents(self):
        """
        Returns true if patient has submitted identity documents
        """
        if (
            self.identity_document_type is None
            and self.identity_document_number is None
        ):
            return False

        return True