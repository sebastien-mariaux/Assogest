from django.contrib import admin
from .models import Organization, Membership,  Member
# Register your models here.


class UserOrganizationInline(admin.TabularInline):
    model = Membership
    extra = 0


class OrganizationAdmin(admin.ModelAdmin):
    model = Organization
    list_display = ['name', 'slug', 'created_at', 'updated_at']
    inlines = [UserOrganizationInline]


class MemberAdmin(admin.ModelAdmin):
    model = Member
    list_display = ['user']
    inlines = [UserOrganizationInline]


class MembershipAdmin(admin.ModelAdmin):
    model = Membership
    list_display = ['member', 'organization', 'is_admin']


admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(Membership, MembershipAdmin)
