# Generated by Django 4.2 on 2024-07-19 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0007_alter_cablematrixmodel_cable_matrix_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cablematrixmodel',
            name='cable_trace_comment',
            field=models.TextField(blank=True, default='NA', null=True),
        ),
        migrations.AlterField(
            model_name='cablematrixmodel',
            name='requested_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
