# Generated by Django 3.1.5 on 2022-06-21 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0010_auto_20220621_1246'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='category',
            field=models.CharField(blank=True, choices=[('Erqonomik', 'Erqonomik'), ('Handmade', 'Handmade')], max_length=50, null=True),
        ),
    ]
