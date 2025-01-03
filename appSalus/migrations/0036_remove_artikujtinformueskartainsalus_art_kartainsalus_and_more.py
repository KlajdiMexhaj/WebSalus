# Generated by Django 5.0.2 on 2024-04-24 10:42

from django_ckeditor_5.fields import CKEditor5Field
import django.db.models.deletion
import parler.fields
import parler.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appSalus', '0035_alter_artikujtinformueskartainsalus_art_kartainsalus_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artikujtinformueskartainsalus',
            name='art_KartaInSalus',
        ),
        migrations.RemoveField(
            model_name='artikujtinformueskartainsalus',
            name='name',
        ),
        migrations.CreateModel(
            name='artikujtinformuesKartaInSalusTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='name')),
                ('art_KartaInSalus',  CKEditor5Field(blank=True, null=True, verbose_name='art_KartaInSalus')),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='appSalus.artikujtinformueskartainsalus')),
            ],
            options={
                'verbose_name': 'artikujtinformues karta in salus Translation',
                'db_table': 'appSalus_artikujtinformueskartainsalus_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatableModel, models.Model),
        ),
    ]
