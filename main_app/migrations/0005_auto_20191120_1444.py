# Generated by Django 2.2.7 on 2019-11-20 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20191120_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clinic',
            name='picture',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
