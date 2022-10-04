from django.urls import path
from .views import phone_list, phone_show


urlpatterns = [
    path('phone_list/', phone_list, name="phone_list"),
    path('phone_show/<int:id>/', phone_show, name="phone_show"),
]