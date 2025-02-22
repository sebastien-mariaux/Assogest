# Generated by Django 5.1.4 on 2025-02-09 13:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0004_delete_eventinscription'),
        ('organization', '0002_membership_is_admin_alter_organization_members_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calendarevent',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='organization.organization'),
        ),
        migrations.AlterUniqueTogether(
            name='subscription',
            unique_together={('event', 'member')},
        ),
    ]
