# Generated by Django 3.1.5 on 2022-06-17 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_jobs_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='jobs',
            name='type',
            field=models.IntegerField(blank=True, choices=[(1, 'full time'), (2, 'part time')], default=1, null=True),
        ),
    ]
