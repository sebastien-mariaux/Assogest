from django.urls import path
from .views import OrganizationsListView, OrganizationDetailView

app_name = 'organization'

urlpatterns = (
    path('', OrganizationsListView.as_view(), name='organization-list'),
    path('<slug:slug>/', OrganizationDetailView.as_view(), name='organization-detail'),
)
