# Generated by Django 4.2 on 2024-07-26 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0012_alter_cablematrixmodel_rrd'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subnavitem',
            name='parent_nav',
        ),
        migrations.AlterField(
            model_name='cablematrixmodel',
            name='requested_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='NavItem',
        ),
        migrations.DeleteModel(
            name='SubNavItem',
        ),
    ]
