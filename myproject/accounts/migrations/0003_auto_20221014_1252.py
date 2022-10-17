# Generated by Django 3.1.8 on 2022-10-14 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20221014_1247'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
            ],
            options={
                'verbose_name': 'Empresa',
                'verbose_name_plural': 'Empresas',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('accounts.user',),
        ),
        migrations.AlterField(
            model_name='user',
            name='type',
            field=models.CharField(choices=[('admin', 'Administrador'), ('customer', 'Cliente'), ('company', 'Empresa')], default='customer', max_length=20),
        ),
    ]
