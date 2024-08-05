# Generated by Django 5.0.7 on 2024-08-05 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0016_cablematrixmodel_port_assignment_comment_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cablematrixmodel',
            name='cable_measurement_assignment_comment',
            field=models.TextField(blank=True, default='NA', null=True),
        ),
        migrations.AddField(
            model_name='cablematrixmodel',
            name='cable_measurement_assignment_status',
            field=models.CharField(blank=True, choices=[('Completed', 'Completed'), ('In Progress', 'In Progress'), ('Not Required', 'Not Required'), ('Yet To Work', 'Yet To Work'), ('Not yet Started', 'Not yet Started'), ('Cancelled', 'Cancelled')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='cablematrixmodel',
            name='cable_measurement_tickets_closed_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cablematrixmodel',
            name='cable_measurement_tickets_requested_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cablematrixmodel',
            name='cable_measurement_tickets_requested_id',
            field=models.CharField(blank=True, default='NA', max_length=100),
        ),
        migrations.AddField(
            model_name='cablematrixmodel',
            name='cable_measurement_tickets_required',
            field=models.CharField(blank=True, choices=[('EMAIL', 'EMAIL'), ('ESS', 'ESS'), ('ITONS', 'ITONS'), ('AORTS', 'AORTS')], max_length=20, null=True),
        ),
    ]
