# Create your views here.
from django.db.models import Count
from django.views.generic import ListView, DetailView, View
from .models import Organization, Membership
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.core.exceptions import PermissionDenied
from django.utils.translation import gettext_lazy as _


class OrganizationsListView(ListView, LoginRequiredMixin):
    model = Organization
    paginate_by = 10
    ordering = ['name']

    def get_queryset(self):
        return Organization.objects.annotate(
            members_count=Count('members')
        ).order_by('-created_at')

    # TODO: if only one organization, redirect to organization detail view


class OrganizationDetailView(LoginRequiredMixin, DetailView):
    model = Organization
    slug_field = 'slug'
    slug_url_arg = 'slug'

    def get_queryset(self):
        return Organization.objects.annotate(
            members_count=Count('members')
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['events'] = self.object.events.order_by('start_time')[:5]
        context['active_tab'] = 'overview'
        context['is_admin'] = self.object.memberships.filter(member=self.request.user.member, is_admin=True).exists()
        return context


class OrganizationAdminView(LoginRequiredMixin, View):
    template_name = 'organization/organization_admin.html'

    def get_organization(self):
        return get_object_or_404(Organization, slug=self.kwargs['slug'])

    def check_admin_access(self, organization, user):
        try:
            membership = organization.memberships.get(member=user.member)
            if not membership.is_admin:
                raise PermissionDenied(
                    _("You must be an administrator to access this page.")
                )
        except Membership.DoesNotExist:
            raise PermissionDenied(
                _("You must be a member of the organization to access this page.")
            )

    def get(self, request, *args, **kwargs):
        organization = self.get_organization()
        self.check_admin_access(organization, request.user)

        context = {
            'organization': organization,
            'is_admin': True
        }
        return render(request, self.template_name, context)
