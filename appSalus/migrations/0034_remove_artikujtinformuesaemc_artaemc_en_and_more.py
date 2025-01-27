# Generated by Django 5.0.2 on 2024-04-24 08:31

from django_ckeditor_5.fields import CKEditor5Field
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appSalus', '0033_artikujtinformuesaemc_artaemc_en_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artikujtinformuesaemc',
            name='artAeMC_en',
        ),
        migrations.RemoveField(
            model_name='artikujtinformuesaemc',
            name='artAeMC_it',
        ),
        migrations.RemoveField(
            model_name='artikujtinformuesaemc',
            name='artAeMC_sq',
        ),
        migrations.RemoveField(
            model_name='artikujtinformuesaemc',
            name='name_en',
        ),
        migrations.RemoveField(
            model_name='artikujtinformuesaemc',
            name='name_it',
        ),
        migrations.RemoveField(
            model_name='artikujtinformuesaemc',
            name='name_sq',
        ),
        migrations.RemoveField(
            model_name='artikujtinformueskartainsalus',
            name='art_KartaInSalus_en',
        ),
        migrations.RemoveField(
            model_name='artikujtinformueskartainsalus',
            name='art_KartaInSalus_it',
        ),
        migrations.RemoveField(
            model_name='artikujtinformueskartainsalus',
            name='art_KartaInSalus_sq',
        ),
        migrations.RemoveField(
            model_name='artikujtinformueskartainsalus',
            name='name_en',
        ),
        migrations.RemoveField(
            model_name='artikujtinformueskartainsalus',
            name='name_it',
        ),
        migrations.RemoveField(
            model_name='artikujtinformueskartainsalus',
            name='name_sq',
        ),
        migrations.AlterField(
            model_name='artikujtinformueskartainsalus',
            name='art_KartaInSalus',
            field=CKEditor5Field(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='artikujtinformueskartainsalus',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
