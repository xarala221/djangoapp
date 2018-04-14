# Generated by Django 2.0.4 on 2018-04-14 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_page_video_embed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='nav_color',
            field=models.CharField(default='#000000', max_length=7),
        ),
        migrations.AlterField(
            model_name='page',
            name='video_embed',
            field=models.TextField(blank=True, null=True),
        ),
    ]
