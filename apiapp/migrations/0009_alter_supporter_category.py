# Generated by Django 4.1.7 on 2023-05-15 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("apiapp", "0008_supporter_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="supporter",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="apiapp.subcategory"
            ),
        ),
    ]
