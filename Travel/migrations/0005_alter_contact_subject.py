# Generated by Django 3.2.18 on 2023-03-23 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Travel', '0004_newsletter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='subject',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
