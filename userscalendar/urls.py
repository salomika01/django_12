from django.urls import path
from userscalendar import date_view

urlpatterns = [
    path('', date_view, name='date_view'),
]