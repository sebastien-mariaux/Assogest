from django.contrib import admin
from .models import CalendarEvent, Subscription


# Register your models here.


class SubscriptionInline(admin.TabularInline):
    model = Subscription
    extra = 0


class CalendarEventAdmin(admin.ModelAdmin):
    model = CalendarEvent
    inlines = [SubscriptionInline]


admin.site.register(CalendarEvent, CalendarEventAdmin)
