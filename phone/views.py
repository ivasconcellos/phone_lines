from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Phone
from .forms import PhoneForm


def phone_list(request):
    content = request.GET.get('content', None)
    if content:
        phones = Phone.objects.filter(phone_number__icontains=content) | Phone.objects.filter(department__icontains=content) | Phone.objects.filter(sponsor__icontains=content)
    else:
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
        phone = form.save(commit=False)
        phone.created_for = request.user
        phone.save()

        messages.success(request, "Ramal cadastrado com sucesso!")

        return redirect('phone_list')
    return render(request, 'phone_form.html', {'form': form})


@login_required
def phone_edit(request, id):
    phone = get_object_or_404(Phone, pk=id)

    form = PhoneForm(request.POST or None, instance=phone)

    if form.is_valid():
        phone = form.save(commit=False)
        phone.created_for = request.user
        phone.save()

        messages.success(request, "Ramal atualizado com sucesso!")

        return redirect('phone_list')

    return render(request, 'phone_form.html', {'form': form})


@login_required
def phone_delete(request, id):
    phone = get_object_or_404(Phone, pk=id)
    phone.delete()
    return redirect('phone_list')
