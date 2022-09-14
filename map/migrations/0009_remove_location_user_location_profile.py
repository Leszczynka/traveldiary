# Generated by Django 4.1 on 2022-09-13 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0008_alter_location_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='user',
        ),
        migrations.AddField(
            model_name='location',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='map.profile'),
        ),
    ]
