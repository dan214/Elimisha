# Generated by Django 2.0 on 2018-07-25 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='student',
            name='birth_date',
        ),
        migrations.RemoveField(
            model_name='student',
            name='department',
        ),
        migrations.RemoveField(
            model_name='student',
            name='location',
        ),
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='profile',
            name='department',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
