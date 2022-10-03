from django.db import models


class PhoneType(models.TextChoices):
    ANALOG = 'Analógico', 'Analógico'
    DIGITAL = 'Digital', 'Digital'

class Phone(models.Model):
    phone_number = models.CharField(max_length=4)
    phone_type = models.CharField(max_length=9, choices=PhoneType.choices, default=PhoneType.DIGITAL)
    department = models.CharField(max_length=255)
    sponsor = models.CharField(max_length=255, blank=True)    
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Phone"
        verbose_name_plural = "Phones"
        ordering = ['department']

    def __str__(self):
        return f'Ramal: {self.phone_number} | Tipo: {self.phone_type} '