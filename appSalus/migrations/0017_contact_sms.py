# Generated by Django 5.0.2 on 2024-04-09 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appSalus', '0016_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='sms',
            field=models.TextField(blank=True, max_length=9000, null=True),
        ),
    ]
