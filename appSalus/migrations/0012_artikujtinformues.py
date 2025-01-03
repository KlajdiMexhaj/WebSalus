# Generated by Django 5.0.2 on 2024-03-13 11:50

from django_ckeditor_5.fields import CKEditor5Field
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appSalus', '0011_specialitet_specialitet_video3_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='artikujtinformues',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='artikujtinformues/')),
                ('art_description', CKEditor5Field(blank=True, null=True)),
                ('departamenti', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='appSalus.departamenti')),
            ],
        ),
    ]
