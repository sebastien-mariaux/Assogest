from django.urls import path
from .views import OrganizationsView

urlpatterns = (
    path('', OrganizationsView.as_view(), name='organizations'),
)
