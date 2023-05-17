# Generated by Django 4.1.7 on 2023-05-17 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("apiapp", "0010_alter_conversation_title"),
    ]

    operations = [
        migrations.AlterField(
            model_name="message",
            name="sender",
            field=models.CharField(
                choices=[
                    ("client", "client"),
                    ("support", "support"),
                    ("board", "board"),
                ],
                default="client",
                max_length=20,
            ),
        ),
    ]
