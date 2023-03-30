# Generated by Django 4.1.7 on 2023-03-30 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiapp', '0003_category_client_conversation_supporter_message_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='account_type',
            field=models.CharField(choices=[('client', 'client'), ('support', 'support'), ('board', 'board')], default='client', max_length=20),
        ),
        migrations.AlterField(
            model_name='message',
            name='sender',
            field=models.CharField(choices=[('client', 'client'), ('support', 'support'), ('board', 'board')], max_length=20),
        ),
    ]
