# Generated by Django 5.0.2 on 2024-04-11 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appSalus', '0020_kontakt_salus_delete_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='LiniTakim_salus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone', models.CharField(blank=True, max_length=50, null=True)),
                ('date', models.CharField(blank=True, max_length=50, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, max_length=60, null=True)),
                ('sms', models.TextField(blank=True, max_length=2000, null=True)),
            ],
        ),
    ]
