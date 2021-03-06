# Generated by Django 3.1.5 on 2022-06-18 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_auto_20220618_0003'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='salaryByDefault',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='type',
            field=models.CharField(choices=[('full time', 'full time'), ('part time', 'part time'), ('freelance', 'freelance'), ('remote', 'remote')], max_length=50),
        ),
    ]
