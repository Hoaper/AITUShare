# Generated by Django 4.1.2 on 2022-11-03 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Verification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
                ('hash_key', models.CharField(max_length=100)),
                ('status', models.BooleanField()),
            ],
        ),
    ]
