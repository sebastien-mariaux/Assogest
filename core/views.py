
# Create your views here.
from django.views.generic import ListView
from .models import Organization


class OrganizationsView(ListView):
    model = Organization
    context_object_name = 'organizations'
    paginate_by = 10
    ordering = ['name']

    def get_queryset(self):
        return Organization.objects.filter(users=self.request.user)
