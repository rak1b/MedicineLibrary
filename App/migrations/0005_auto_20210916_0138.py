# Generated by Django 3.2.6 on 2021-09-15 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0004_auto_20210916_0119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='doses',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='side_effect',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='uses',
            field=models.TextField(max_length=1000),
        ),
    ]
