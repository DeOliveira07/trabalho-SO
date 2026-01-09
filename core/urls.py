from django.urls import path
from . import views

urlpatterns = [
    path('crypto/', views.crypto_example, name='crypto_example'),
]
