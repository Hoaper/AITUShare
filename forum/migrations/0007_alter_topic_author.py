# Generated by Django 4.1.2 on 2022-11-20 06:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0008_profile_first_name_profile_last_name'),
        ('forum', '0006_topic_accepted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='author',
            field=models.ForeignKey(default='DELETED', on_delete=django.db.models.deletion.SET_DEFAULT, to='profiles.profile'),
        ),
    ]
