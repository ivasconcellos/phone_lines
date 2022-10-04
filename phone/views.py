from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Phone
from .forms import PhoneForm


@login_required
def phone_list(request):
    phones = Phone.objects.all()
    return render(request, 'phone_index.html', {'phones': phones})


@login_required
def phone_show(request, id):
    phone = get_object_or_404(Phone, pk=id)
    return render(request, 'phone_show.html', {'phone': phone})


@login_required
def phone_new(request):
    form = PhoneForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('phone_list')
    return render(request, 'phone_form.html', {'form': form})