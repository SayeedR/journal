# Generated by Django 3.1.4 on 2021-04-07 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fileupload', '0005_auto_20210407_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paper',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
