from django.urls import path
from .views import phone_list, phone_show, phone_new, phone_edit, phone_delete


urlpatterns = [
    path('', phone_list, name="phone_list"),
    path('phone_show/<int:id>/', phone_show, name="phone_show"),
    path('phone_new/', phone_new, name="phone_new"),
    path('phone_edit/<int:id>/', phone_edit, name="phone_edit"),
    path('phone_delete/<int:id>/', phone_delete, name="phone_delete"),
]