# Generated by Django 5.0.2 on 2024-04-12 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appSalus', '0023_linitakim_salus'),
    ]

    operations = [
        migrations.AddField(
            model_name='specialitet',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
