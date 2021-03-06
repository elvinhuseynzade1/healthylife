# Generated by Django 2.2.7 on 2019-11-20 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clinic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('adrress', models.CharField(max_length=120)),
                ('picture', models.ImageField(upload_to=None)),
                ('tip', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=120)),
                ('name', models.CharField(max_length=120)),
                ('surname', models.CharField(max_length=120)),
                ('clinic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Clinic')),
            ],
        ),
    ]
