# Generated by Django 5.0.2 on 2024-08-26 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appSalus', '0057_checkup_albanostra'),
    ]

    operations = [
        migrations.RenameField(
            model_name='checkup_albanostra',
            old_name='checkup_albanostra',
            new_name='checkup_albanostra_img',
        ),
    ]