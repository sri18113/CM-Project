# Generated by Django 4.2 on 2024-07-29 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0014_alter_cablematrixmodel_requested_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='cablematrixmodel',
            name='device_installation_completion_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cablematrixmodel',
            name='device_installation_requested_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cablematrixmodel',
            name='device_installation_status',
            field=models.CharField(blank=True, choices=[('Completed', 'Completed'), ('In Progress', 'In Progress'), ('Not Required', 'Not Required'), ('Yet To Work', 'Yet To Work'), ('Not yet Started', 'Not yet Started'), ('Cancelled', 'Cancelled')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='cablematrixmodel',
            name='installation_comment',
            field=models.TextField(blank=True, default='NA'),
        ),
        migrations.AddField(
            model_name='cablematrixmodel',
            name='installation_tickets_closed_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cablematrixmodel',
            name='installation_tickets_requested_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cablematrixmodel',
            name='installation_tickets_requested_id',
            field=models.CharField(blank=True, default='NA', max_length=100),
        ),
        migrations.AddField(
            model_name='cablematrixmodel',
            name='installation_tickets_required',
            field=models.CharField(blank=True, choices=[('EMAIL', 'EMAIL'), ('ESS', 'ESS'), ('ITONS', 'ITONS'), ('AORTS', 'AORTS')], max_length=20, null=True),
        ),
    ]