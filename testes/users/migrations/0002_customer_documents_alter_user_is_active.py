# Generated by Django 4.1.2 on 2022-10-20 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="customer",
            name="documents",
            field=models.FileField(null=True, upload_to="files"),
        ),
        migrations.AlterField(
            model_name="user",
            name="is_active",
            field=models.BooleanField(
                default=True, help_text="Ativo ou inativo", verbose_name="Status"
            ),
        ),
    ]