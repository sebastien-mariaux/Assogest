from django.urls import path
from .views import OrganizationsListView, OrganizationDetailView

app_name = 'nonprofits'

urlpatterns = (
    path('', OrganizationsListView.as_view(), name='organizations'),
    path('<slug:slug>/', OrganizationDetailView.as_view(), name='organization-detail'),
)
