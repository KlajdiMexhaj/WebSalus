# Generated by Django 5.0.2 on 2024-02-20 12:27

from django_ckeditor_5.fields import CKEditor5Field
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appSalus', '0005_klinikaferti_alter_about_about_imgambjeti_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AeMC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AeMC_text', CKEditor5Field(blank=True, null=True)),
            ],
        ),
    ]
