# Generated by Django 5.0.2 on 2024-05-06 11:42

from django_ckeditor_5.fields import CKEditor5Field
import django.db.models.deletion
import parler.fields
import parler.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appSalus', '0043_remove_artikujtinformuesaemc_artaemc_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artikujtinformuesdonnasalus',
            name='art_DonnaSalus',
        ),
        migrations.RemoveField(
            model_name='artikujtinformuesdonnasalus',
            name='name',
        ),
        migrations.CreateModel(
            name='artikujtinformuesDonnaSalusTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('art_DonnaSalus', CKEditor5Field(blank=True, null=True)),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='appSalus.artikujtinformuesdonnasalus')),
            ],
            options={
                'verbose_name': 'artikujtinformues donna salus Translation',
                'db_table': 'appSalus_artikujtinformuesdonnasalus_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatableModel, models.Model),
        ),
    ]
