# Generated by Django 4.2.1 on 2023-05-27 20:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('g_detect', '0003_alter_volunteer_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteer',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
