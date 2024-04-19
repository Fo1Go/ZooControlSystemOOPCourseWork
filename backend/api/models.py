from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from .validators import positive_check
from django.utils.translation import gettext_lazy as _
from django.utils.timezone import now
from django.contrib.auth.validators import UnicodeUsernameValidator
from .managers import UserManager

base_model = models.Model


class ChoicesTypes:
    @staticmethod
    def types_operations_choices():
        types = {
            "CM": "Comes",
            "EX": "Experiences",
        }
        return types

    @staticmethod
    def animal_genders_choices():
        genders = {
            "F": "Female",
            "M": "Male"
        }
        return genders

    @staticmethod
    def ticket_types_choices():
        types = {
            "CH": "Children",
            "AD": "Adult",
            "PR": "Preferential",
        }
        return types

    @staticmethod
    def feeding_types_choices():
        types = {
            "VT": "vegetables mix",
            "MT": "meat",
        }
        return types


class User(AbstractUser):
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(_("username"),
                                null=True,
                                blank=True,
                                max_length=150,
                                help_text=_("Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."),
                                validators=[username_validator])
    email = models.EmailField(_("email address"), unique=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return f"User({self.email})"


class JobPosition(base_model):
    position = models.CharField(max_length=150, unique=True, blank=False, null=False)
    base_salary_rate = models.FloatField(validators=[positive_check], default=1, null=False)

    class Meta:
        ordering = ["position"]
        db_table = "job_positions"
        verbose_name = _("Position")
        verbose_name_plural = _("Positions")

    def __str__(self):
        return f"Position({self.name} {self.base_salary_rate})"


class Employer(base_model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    position = models.ForeignKey(JobPosition, related_name="employer",
                                 on_delete=models.SET_NULL, null=True, blank=True)
    salary_multiplier = models.FloatField(validators=[positive_check],
                                         default=1, blank=False, null=False)

    class Meta:
        db_table = "employers"
        verbose_name = _("employer")
        verbose_name_plural = _("employers")

    def __str__(self):
        return f"Employer({self.email} {self.position})"


class Client(base_model):
    user = models.OneToOneField(User, related_name='client', on_delete=models.CASCADE)
    phone_number = models.CharField(unique=True, null=True, blank=False)

    class Meta:
        db_table = "clients"
        verbose_name = _("client")
        verbose_name_plural = _("clients")

    def __str__(self):
        return f"Client({self.email})"


class Ticket(base_model):
    client = models.ForeignKey(Client, related_name='tickets', on_delete=models.SET_NULL,
                               null=True, blank=False)
    type = models.CharField(choices=ChoicesTypes.ticket_types_choices)
    visit_date = models.DateField(null=False, blank=False)
    purchase_date = models.DateField(null=False, blank=False, default=now)
    ticket_number = models.CharField(unique=True)
    price = models.FloatField(null=False)

    class Meta:
        db_table = "tickets"
        verbose_name = _("ticket")
        verbose_name_plural = _("tickets")

    def __str__(self):
        return f"Ticket({self.client.email} {self.type})"


class Feedback(base_model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    user = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="reviews", null=True)

    def __str__(self):
        return f'Feedback({self.title}, {self.description})'


class Species(base_model):
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=2048, null=True, blank=True)

    def __str__(self):
        return f'Species({self.title})'

    class Meta:
        db_table = "species"
        verbose_name = _("species")
        verbose_name_plural = _("species")


class Animal(base_model):
    species = models.ForeignKey(Species, null=True, related_name="animals",
                                on_delete=models.SET_NULL, blank=True)
    description = models.TextField(max_length=1500)
    nickname = models.CharField(max_length=150, unique=True, null=True, blank=True)
    age_in_month = models.IntegerField(validators=[positive_check], default=0, blank=False, null=False)
    gender = models.CharField(choices=ChoicesTypes.animal_genders_choices)

    class Meta:
        db_table = "animals"
        ordering = ["nickname", "species"]
        verbose_name = _("Animal")
        verbose_name_plural = _("Animals")

    def __str__(self):
        return f"Animal({self.species}, {self.nickname}, {self.gender})"


class MedicalCheckup(base_model):
    animal = models.ForeignKey(Animal, related_name="checkups", on_delete=models.CASCADE)
    last_date_check = models.DateField(null=True, blank=True)
    diagnosis = models.TextField(default="", blank=True, null=False)
    recommended_actions = models.TextField(default="", blank=True, null=False)

    class Meta:
        db_table = "medical_checkups"
        verbose_name = _("Medical Checkup")
        verbose_name_plural = _("Medical Checkups")

    def __str__(self):
        return f"Checkup({self.animal} {self.last_date_check})"


class Feeding(base_model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    date_feeding = models.DateField(default=now)
    type_of_feeding = models.CharField(choices=ChoicesTypes.feeding_types_choices)
    count_of_feeding = models.IntegerField(validators=[positive_check], default=1, null=True, blank=True)

    class Meta:
        db_table = "feeding"
        verbose_name = _("Feeding")
        verbose_name_plural = _("Feeding")

    def __str__(self):
        return f"Feeding({self.animal.nickname} {self.date_feeding}"


class Finance(base_model):
    date_of_operation = models.DateField(default=now, null=True, blank=True)
    type_of_operation = models.CharField(choices=ChoicesTypes.types_operations_choices)
    amount = models.IntegerField(validators=[positive_check], null=False, blank=False)
    description = models.TextField(default="", null=True, blank=True)

    def __str__(self):
        return f"Finance({self.date_of_operation} {self.type_of_operation})"


class ContactInformation(base_model):
    cost_adult_ticket = models.IntegerField(null=True, blank=True)
    cost_children_ticket = models.IntegerField(null=True, blank=True)
    open_time = models.DateTimeField(null=True, blank=True)
    close_time = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "contact_information"
        verbose_name = _("contact information")
        verbose_name_plural = verbose_name


def create_permissions():
    from django.contrib.auth.models import Group, Permission
    from django.contrib.contenttypes.models import ContentType

    content_type = ContentType.objects.get_for_model(Employer)
    permission = Permission.objects.create(
        codename='Employer',
        name='Employer',
        content_type=content_type
    )

    # Step 2: Add permissions to a group
    group = Group.objects.create(name='My Group')
    group.permissions.add(permission)
