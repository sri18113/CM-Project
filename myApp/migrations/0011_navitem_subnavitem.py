# Generated by Django 4.2 on 2024-07-25 12:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0010_alter_cablematrixmodel_cable_matrix_status_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='NavItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubNavItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
                ('parent_nav', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subitems', to='myApp.navitem')),
            ],
        ),
    ]
