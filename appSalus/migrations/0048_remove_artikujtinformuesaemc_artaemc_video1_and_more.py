# Generated by Django 5.0.2 on 2024-05-10 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appSalus', '0047_artikujtinformuesaemc_artaemc_video1_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artikujtinformuesaemc',
            name='artAeMC_video1',
        ),
        migrations.RemoveField(
            model_name='artikujtinformuesaemc',
            name='artAeMC_video2',
        ),
        migrations.RemoveField(
            model_name='artikujtinformuesaemc',
            name='artAeMC_video3',
        ),
        migrations.RemoveField(
            model_name='artikujtinformuesaemc',
            name='artAeMC_video4',
        ),
        migrations.RemoveField(
            model_name='artikujtinformuesaemc',
            name='artAeMC_video5',
        ),
        migrations.RemoveField(
            model_name='artikujtinformuesaemc',
            name='artAeMC_video6',
        ),
    ]
