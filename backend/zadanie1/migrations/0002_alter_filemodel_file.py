# Generated by Django 5.1.2 on 2024-10-10 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zadanie1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filemodel',
            name='file',
            field=models.FileField(upload_to='files'),
        ),
    ]
