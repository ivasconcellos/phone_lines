from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Phone


@login_required
def phone_list(request):
    phones = Phone.objects.all()
    return render(request, 'phone_index.html', {'phones': phones})
