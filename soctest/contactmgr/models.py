from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)


# NOTE: If contacts were always going to be in the US i would model
#       something like this, where i get pre made validations

# from django.db import models
# from localflavor.us.us_states import STATE_CHOICES
# from localflavor.us.models import PhoneNumberField, USZipCodeField
#
#
# class Contact(models.Model):
#     name = models.CharField(max_length=255)
#     address = models.CharField(max_length=255)
#     city = models.CharField(max_length=255)
#     state = models.CharField(max_length=2, choices=STATE_CHOICES)
#     postal_code = USZipCodeField(max_length=255)
#     country = models.CharField(max_length=255)
#     phone = PhoneNumberField(max_length=255)
