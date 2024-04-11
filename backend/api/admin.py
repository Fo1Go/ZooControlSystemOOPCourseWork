from django.contrib.admin import register, ModelAdmin
from .models import (User, Client, Employer, Ticket, Finance,
                    Feeding, MedicalCheckup, Animal, JobPosition, ContactInformation)


@register(MedicalCheckup)
class MedicalCheckupAdmin(ModelAdmin):
    ...


@register(JobPosition)
class JobPositionAdmin(ModelAdmin):
    ...


@register(Animal)
class AnimalAdmin(ModelAdmin):
    ...


@register(ContactInformation)
class ContactInformationAdmin(ModelAdmin):
    ...


@register(User)
class UserAdmin(ModelAdmin):
    ...


@register(Finance)
class FinanceAdmin(ModelAdmin):
    ...


@register(Feeding)
class FeedingAdmin(ModelAdmin):
    ...


@register(Client)
class ClientAdmin(ModelAdmin):
    ...


@register(Employer)
class EmployerAdmin(ModelAdmin):
    ...


@register(Ticket)
class TicketAdmin(ModelAdmin):
    ...
