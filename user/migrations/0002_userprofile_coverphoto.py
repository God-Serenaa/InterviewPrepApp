# Generated by Django 4.1.4 on 2022-12-18 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='coverPhoto',
            field=models.ImageField(default='user/default.png', upload_to='user/image'),
        ),
    ]
