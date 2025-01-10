
# Create your views here.
from django.views.generic import ListView, DetailView
from .models import Organization
from django.contrib.auth.mixins import LoginRequiredMixin


class OrganizationsListView(ListView, LoginRequiredMixin):
    model = Organization
    context_object_name = 'organizations'
    paginate_by = 10
    ordering = ['name']

    def get_queryset(self):
        return (
            Organization.objects
            .filter(members=self.request.user.member)
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
            members=self.request.user.member,
            slug=self.kwargs['slug']
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['events'] = self.object.events.order_by('start_time')[:5]
        return context
    