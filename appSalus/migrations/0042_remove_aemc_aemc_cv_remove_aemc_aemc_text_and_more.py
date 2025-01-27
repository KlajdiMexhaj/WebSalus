# Generated by Django 5.0.2 on 2024-05-06 11:09

from django_ckeditor_5.fields import CKEditor5Field
import django.db.models.deletion
import parler.fields
import parler.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appSalus', '0041_remove_about_about_oltipershkrimi_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aemc',
            name='AeMC_CV',
        ),
        migrations.RemoveField(
            model_name='aemc',
            name='AeMC_text',
        ),
        migrations.CreateModel(
            name='AeMCTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('AeMC_text', CKEditor5Field(blank=True, null=True)),
                ('AeMC_CV', CKEditor5Field(blank=True, null=True)),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='appSalus.aemc')),
            ],
            options={
                'verbose_name': 'ae mc Translation',
                'db_table': 'appSalus_aemc_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatableModel, models.Model),
        ),
    ]
