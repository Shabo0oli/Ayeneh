# Generated by Django 2.2.3 on 2019-08-09 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='Credit',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='student',
            name='State',
            field=models.CharField(blank=True, max_length=40),
        ),
    ]