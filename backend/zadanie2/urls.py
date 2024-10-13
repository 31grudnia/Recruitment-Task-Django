from django.urls import path, include

from .views import check_pesel, PeselCheckView


urlpatterns = [
    path('', check_pesel, name='pesel'),
    path('check-pesel/', PeselCheckView.as_view(), name='check-pesel'),
]
