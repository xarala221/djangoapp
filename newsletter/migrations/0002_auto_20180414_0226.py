# Generated by Django 2.0.4 on 2018-04-14 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='join',
            name='email',
            field=models.EmailField(max_length=200),
        ),
    ]
