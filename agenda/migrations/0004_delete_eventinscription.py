# Generated by Django 5.1.4 on 2025-01-09 23:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0003_alter_calendarevent_organization_subscription_event_and_more'),
        ('core', '0004_remove_userorganization_organization_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='EventInscription',
        ),
    ]
