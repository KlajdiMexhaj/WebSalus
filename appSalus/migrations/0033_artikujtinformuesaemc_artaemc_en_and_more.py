# Generated by Django 5.0.2 on 2024-04-24 08:25

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appSalus', '0032_artikujtinformueskartainsalus_art_kartainsalus_en_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='artikujtinformuesaemc',
            name='artAeMC_en',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='artikujtinformuesaemc',
            name='artAeMC_it',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='artikujtinformuesaemc',
            name='artAeMC_sq',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='artikujtinformuesaemc',
            name='name_en',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='artikujtinformuesaemc',
            name='name_it',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='artikujtinformuesaemc',
            name='name_sq',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
