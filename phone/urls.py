from django.urls import path
from .views import phone_list


urlpatterns = [
    path('phone_list/', phone_list, name="phone_list"),
]