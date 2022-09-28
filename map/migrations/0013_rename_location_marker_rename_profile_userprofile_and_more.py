# Generated by Django 4.1 on 2022-09-28 07:59

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('map', '0012_alter_location_date'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Location',
            new_name='Marker',
        ),
        migrations.RenameModel(
            old_name='Profile',
            new_name='UserProfile',
        ),
        migrations.RenameField(
            model_name='marker',
            old_name='name',
            new_name='location',
        ),
    ]
