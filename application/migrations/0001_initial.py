# Generated by Django 2.1.15 on 2021-06-16 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consumer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LoginID', models.CharField(max_length=20, verbose_name='LineID')),
                ('Name', models.CharField(max_length=10, verbose_name='姓名')),
                ('Sex', models.BooleanField(default=True)),
                ('email', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]
