from xml.etree.ElementInclude import include
from django.urls import re_path, path
from .views import RegisterView

urlpatterns = [
    path('accounts/register/', RegisterView.as_view(), name='register'),
]
