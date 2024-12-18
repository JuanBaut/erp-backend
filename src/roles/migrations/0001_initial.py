# Generated by Django 4.2.14 on 2024-07-29 19:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Permissions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(choices=[('inventory', 'Inventory'), ('transaction', 'Transaction'), ('employee', 'Employee')], max_length=20)),
                ('action', models.CharField(choices=[('create', 'Create'), ('read', 'Read'), ('update', 'Update'), ('delete', 'Delete')], max_length=10)),
            ],
            options={
                'unique_together': {('model', 'action')},
            },
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True)),
                ('permissions', models.ManyToManyField(to='roles.permissions')),
            ],
        ),
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='roles.roles')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
