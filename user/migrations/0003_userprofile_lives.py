# Generated by Django 4.1.4 on 2022-12-18 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_userprofile_coverphoto'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='lives',
            field=models.CharField(blank=True, max_length=256),
        ),
    ]
