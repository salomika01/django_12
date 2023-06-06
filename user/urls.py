from django.urls import path
from user.views import user_view

urlpatterns = [
    path('', user_view, name='user_view'),
]
