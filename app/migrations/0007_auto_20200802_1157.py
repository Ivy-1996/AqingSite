# Generated by Django 2.2 on 2020-08-02 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20200802_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='avatar',
            field=models.ImageField(upload_to='upload/'),
        ),
    ]