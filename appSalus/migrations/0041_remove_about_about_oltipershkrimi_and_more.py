# Generated by Django 5.0.2 on 2024-05-06 11:00

import ckeditor.fields
import django.db.models.deletion
import parler.fields
import parler.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appSalus', '0040_remove_specialitet_departamenti'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='about_oltipershkrimi',
        ),
        migrations.RemoveField(
            model_name='about',
            name='about_pershkrimi',
        ),
        migrations.CreateModel(
            name='AboutTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('about_pershkrimi', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('about_oltipershkrimi', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='appSalus.about')),
            ],
            options={
                'verbose_name': 'about Translation',
                'db_table': 'appSalus_about_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatableModel, models.Model),
        ),
    ]
