# Generated by Django 5.1.11 on 2025-06-26 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_role_role_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='name',
            field=models.CharField(choices=[('Donor', 'Donor'), ('Parent', 'Parent'), ('School Admin', 'School Admin'), ('Community Agent', 'Community Agent')], max_length=50, unique=True),
        ),
    ]
