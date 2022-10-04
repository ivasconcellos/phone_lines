from django.shortcuts import redirect
from django.contrib.auth import logout


def my_logout(request):
    logout(request)
    return redirect('phone_list')