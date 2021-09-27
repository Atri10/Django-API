from django.db import models
import re
from rest_framework.exceptions import ValidationError


class FormUser(models.Model):
    name = models.CharField(max_length=300, blank=False, null=False)
    birth = models.DateField(null=False)
    email = models.EmailField(null=False)
    phone = models.CharField(max_length=15, blank=False, null=False)

    def __str__(self):
        return self.name

    def clean(self):
        """
        Format : +91 XXXXXXXXX where X belongs to [0-9]
        """
        if len(self.phone) > 15 or re.search('[a-zA-Z]', self.phone):
            raise ValidationError({'phone': "Incorrect Phone Number"})

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)
