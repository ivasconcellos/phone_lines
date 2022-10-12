from django.forms import ModelForm
from .models import Phone


class PhoneForm(ModelForm):
    class Meta:
        model = Phone
        fields = ['phone_number', 'phone_type', 'department', 'sponsor', 'active']

        error_messages = {
             "phone_number": {
                "unique": "Já existe ramal cadastrado com esse número!"
            }
        }