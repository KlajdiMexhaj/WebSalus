# Generated by Django 5.0.2 on 2024-05-21 12:59

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appSalus', '0048_remove_artikujtinformuesaemc_artaemc_video1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='linitakim_salus',
            name='published_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
