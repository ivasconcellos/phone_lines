from django.db import models
from django.contrib.auth.models import User


class PhoneType(models.TextChoices):
    ANALOG = 'Analógico', 'Analógico'
    DIGITAL = 'Digital', 'Digital'

class Phone(models.Model):
    phone_number = models.CharField(max_length=4, verbose_name="Número do ramal", unique=True, blank=False, null=False)
    phone_type = models.CharField(max_length=9, choices=PhoneType.choices, default=PhoneType.DIGITAL, verbose_name="Tipo do telefone", blank=False, null=False)
    department = models.CharField(max_length=255, verbose_name="Setor", blank=False, null=False)
    sponsor = models.CharField(max_length=255, blank=True, verbose_name="Responsável")    
    active = models.BooleanField(default=True, verbose_name="Ativo")
    created_for = models.ForeignKey(User, verbose_name="Cadastrador por", on_delete=models.CASCADE, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Cadastrador em", blank=False, null=False)
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Atualizado em")

    def get_sponsor(self):
        if self.sponsor:
            return self.sponsor
        return "Não registrado!"

    def get_active(self):
        if self.active == True:
            return "Sim"
        return "Não"

    class Meta:
        verbose_name = "Phone"
        verbose_name_plural = "Phones"
        ordering = ['department']

    def __str__(self):
        return f'Ramal: {self.phone_number} | Tipo: {self.phone_type} '