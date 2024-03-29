# Generated by Django 5.0 on 2024-01-01 17:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="AboutMeSections",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("meta", models.CharField(blank=True, max_length=250, null=True)),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="about_me/"),
                ),
                ("title", models.CharField(max_length=500)),
                ("content", models.TextField()),
                (
                    "status",
                    models.CharField(
                        choices=[("production", "Production"), ("staging", "Staging")],
                        default="staging",
                        max_length=20,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "About Me Sections",
                "db_table": "about_me",
            },
        ),
    ]
