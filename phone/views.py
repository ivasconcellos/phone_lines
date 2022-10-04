from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Phone


@login_required
def phone_list(request):
    phones = Phone.objects.all()
    return render(request, 'phone_index.html', {'phones': phones})


def phone_show(request, id):
    phone = get_object_or_404(Phone, pk=id)
    return render(request, 'phone_show.html', {'phone': phone})
