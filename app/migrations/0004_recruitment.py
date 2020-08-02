# Generated by Django 2.2 on 2020-08-01 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_cases'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recruitment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=56)),
                ('content', models.CharField(max_length=255)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('desc', models.CharField(max_length=256)),
                ('display', models.BooleanField(default=True)),
            ],
        ),
    ]
