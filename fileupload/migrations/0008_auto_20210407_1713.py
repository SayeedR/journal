# Generated by Django 3.1.4 on 2021-04-07 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fileupload', '0007_auto_20210407_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paper',
            name='files',
            field=models.FileField(default=1, upload_to='files'),
        ),
    ]