from django.db import models


class ContactManager(models.Manager):
    def create_contact(self, row):
        contact = self.create(
            name=row[0],
            address=row[1],
            city=row[2],
            state=row[3],
            postal_code=row[4],
            country=row[5],
            phone=row[6],
        )
        return contact


class Contact(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)

    objects = ContactManager()

    def full_address(self):
        '''
        Gets the full address formated.
        '''
        address = self.address
        if self.city:
            address += ' {}'.format(self.city)
        if self.state:
            address += ' {}'.format(self.state)
        if self.postal_code:
            address += ' {}'.format(self.postal_code)
        if self.country:
            address += ' {}'.format(self.country)
        return address


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
