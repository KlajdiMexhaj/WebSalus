# Generated by Django 5.0.2 on 2024-08-23 07:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appSalus', '0055_albanostra_albanostratranslation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='albanostratranslation',
            old_name='AeMC_text',
            new_name='albanostra_text',
        ),
    ]
