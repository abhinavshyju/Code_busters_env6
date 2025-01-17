# Generated by Django 5.0.1 on 2024-02-07 04:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hospital', '0001_initial'),
        ('users', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='facility',
            name='hosptial',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.hospitalprofile'),
        ),
        migrations.AddField(
            model_name='request',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.employee'),
        ),
        migrations.AddField(
            model_name='request',
            name='hosptial',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.hospitalprofile'),
        ),
        migrations.AddField(
            model_name='request',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
