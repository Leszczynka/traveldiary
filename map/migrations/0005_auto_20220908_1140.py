# Generated by Django 3.2.15 on 2022-09-08 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0004_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='marker',
            name='description',
        ),
        migrations.AddField(
            model_name='marker',
            name='photos',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='marker',
            name='date',
            field=models.DateField(),
        ),
    ]
