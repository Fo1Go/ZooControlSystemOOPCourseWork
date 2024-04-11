from django.core.exceptions import ValidationError


def positive_check(number):
    if number < 0:
        raise ValidationError(f"{number} is negative")
