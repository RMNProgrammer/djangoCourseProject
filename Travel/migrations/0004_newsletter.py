# Generated by Django 3.2.18 on 2023-03-19 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Travel', '0003_alter_contact_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
