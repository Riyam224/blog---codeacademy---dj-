# Generated by Django 3.0.8 on 2020-07-20 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='body',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
