
# Create your views here.
from django.views.generic import ListView, DetailView
from .models import Organization


class OrganizationsListView(ListView):
    model = Organization
    context_object_name = 'organizations'
    paginate_by = 10
    ordering = ['name']

    def get_queryset(self):
        return (
            Organization.objects
            .filter(users=self.request.user)
            .order_by('name')
        )

    # TODO: if only one organization, redirect to organization detail view


class OrganizationDetailView(DetailView):
    model = Organization
    context_object_name = 'organization'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_queryset(self):
        return Organization.objects.filter(
            users=self.request.user,
            slug=self.kwargs['slug']
        )
