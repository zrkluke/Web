# Generated by Django 3.2.4 on 2021-07-10 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0004_auto_20210701_2259'),
    ]

    operations = [
        migrations.AddField(
            model_name='consumer',
            name='test',
            field=models.TextField(null=True),
        ),
    ]
